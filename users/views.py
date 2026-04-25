from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordChangeView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views import View
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import logout as auth_logout
import numpy as np
import joblib
from .forms import RegisterForm, UpdateUserForm, UpdateProfileForm
from .models import UserPredictModel1
from .forms import UserPredictDataForm1
from customer.models import LoanApplication
def home(request):
    return render(request, 'users/home.html')


def adminhome(request):
    return render(request, 'app/adminhome.html')

@login_required(login_url='users-register')


def index(request):
    return render(request, 'app/index.html')
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from .forms import RegisterForm
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .forms import RegisterForm, AdminLoginForm
from django.contrib.auth.models import User


from django.shortcuts import render, redirect
from django.views import View
from .forms import RegisterForm
from django.contrib import messages

from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.views import LoginView
from django.contrib import messages
from .forms import AdminRegisterForm, AdminLoginForm

class AdminRegisterView(View):
    form_class = AdminRegisterForm
    template_name = 'users/register.html'

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class()})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Admin registered successfully!")
            return redirect('users:login')
        return render(request, self.template_name, {'form': form})

class AdminLoginView(LoginView):
    form_class = AdminLoginForm
    template_name = 'users/login.html'

    def form_valid(self, form):
        user = form.get_user()
        if user.user_type != 'admin':
            messages.error(self.request, "You are not allowed to login here")
            return redirect('users:login')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('users:users-home')


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'users/password_reset.html'
    email_template_name = 'users/password_reset_email.html'
    subject_template_name = 'users/password_reset_subject'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('users:users-home')


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'users/change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('users:users-home')


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='users-profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'users/profile.html', {'user_form': user_form, 'profile_form': profile_form})
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .forms import UserPredictDataForm1
from customer.models import LoanApplication
from django.contrib.auth import get_user_model
import google.generativeai as genai
import json

User = get_user_model()

# -----------------------------
# Configure Gemini API
# -----------------------------
GEMINI_API_KEY = "AIzaSyCWUY86ySe1mHJ_P5oA2z_2XwSwIaceLIY"  # Replace with your actual key
genai.configure(api_key=GEMINI_API_KEY)

@login_required
def loan(request):
    """
    Loan prediction view using Gemini LLM for eligibility, reason, and recommendations.
    """
    fields = [
        'Gender', 'Married', 'Dependents', 'Education', 'Self_Employed',
        'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term',
        'Property_Area', 'Marital_status', 'Employee_type', 'Industrial_sector',
        'Existing_monthly_EMIs', 'Monthly_household_expenses', 'Total_value_of_assets',
        'Loan_purpose'
    ]

    if request.method == 'POST':
        form = UserPredictDataForm1(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.timestamp = timezone.now()
            instance.save()

            # Collect form data
            form_data_dict = {field: request.POST.get(field) for field in fields}

            # Build Gemini prompt
            prompt = f"""
You are a financial advisor and loan eligibility expert.

Task:
Analyze the applicant's data below and determine if the loan is eligible.
Provide your response in this exact format:

Prediction:
<Yes / No>

Reason:
<short reasoning if not eligible>

Recommendations:
- <bullet points for user actions to improve eligibility or maintain good status>

Applicant Data:
{json.dumps(form_data_dict, indent=2)}
"""

            try:
                # Gemini 2.5 Flash call
                model = genai.GenerativeModel("gemini-2.5-flash")
                response = model.generate_content([{"text": prompt}])
                text = response.text.strip() if response.text else "No response received."

                # Parse LLM response
                lines = text.splitlines()
                llm_prediction = next((line.replace("Prediction:", "").strip() 
                                       for line in lines if "Prediction:" in line), "Unknown")
                reason = next((line.replace("Reason:", "").strip() 
                               for line in lines if "Reason:" in line), "")
                recommendations = []
                rec_started = False
                for line in lines:
                    if line.startswith("Recommendations:"):
                        rec_started = True
                        continue
                    if rec_started and line.strip().startswith("-"):
                        recommendations.append(line.strip())

            except Exception as e:
                text = f"⚠️ Error: {str(e)}"
                llm_prediction = "Unknown"
                reason = ""
                recommendations = []

            return render(request, 'app/result1.html', {
                'form': form,
                'prediction_text': llm_prediction,
                'reason': reason,
                'recommendations': recommendations,
                'llm_raw_text': text
            })

    else:
        form = UserPredictDataForm1()

    return render(request, 'app/loan.html', {'form': form})

from django.http import JsonResponse
def get_loan_application_by_username(request):
    """
    Returns the latest loan application data for a given username as JSON.
    Handles errors gracefully if user or loan application does not exist.
    """
    username = request.GET.get('username')
    if not username:
        return JsonResponse({'error': 'Username not provided'}, status=400)

    try:
        # Fetch latest loan application for the user
        loan_app = LoanApplication.objects.filter(user__username=username).latest('applied_at')
    except LoanApplication.DoesNotExist:
        return JsonResponse({'error': 'No loan application found for this username'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

    # Map loan application fields to JSON safely
    data = {
        'Gender': getattr(loan_app, 'gender', 0),
        'Married': getattr(loan_app, 'married', 0),
        'Dependents': getattr(loan_app, 'dependents', 0),
        'Education': getattr(loan_app, 'education', 0),
        'Self_Employed': getattr(loan_app, 'self_employed', 0),
        'ApplicantIncome': getattr(loan_app, 'applicant_income', 0),
        'CoapplicantIncome': getattr(loan_app, 'coapplicant_income', 0),
        'LoanAmount': getattr(loan_app, 'loan_amount', 0),
        'Loan_Amount_Term': getattr(loan_app, 'loan_amount_term', 0),
        'Property_Area': getattr(loan_app, 'property_area', 0),
        # New/optional fields
        'Marital_status': getattr(loan_app, 'marital_status', 0),
        'Employee_type': getattr(loan_app, 'employee_type', 0),
        'Industrial_sector': getattr(loan_app, 'industrial_sector', ''),
        'Existing_monthly_EMIs': getattr(loan_app, 'existing_monthly_EMIs', 0),
        'Monthly_household_expenses': getattr(loan_app, 'monthly_household_expenses', 0),
        'Total_value_of_assets': getattr(loan_app, 'total_value_of_assets', 0),
        'Loan_purpose': getattr(loan_app, 'loan_purpose', 0),
    }

    return JsonResponse(data)

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import base64
from io import BytesIO
from django.shortcuts import render

def output(request):
    return render(request,'app/output.html')
def output1(request):
    return render(request,'app/output1.html')

def output10(request):
    return render(request,'app/output10.html')
def output2(request):
    return render(request,'app/output2.html')
def output3(request):
    return render(request,'app/output3.html')

def loan_db(request):
    model = UserPredictModel1.objects.all()
    return render(request, 'app/loan_db.html', {'model': model})




def logout_view(request):  
    auth_logout(request)
    return redirect('/')


from django.shortcuts import render, redirect, get_object_or_404
from customer.models import LoanApplication

# Custom Admin Dashboard View
def admin_dashboard(request):
    loans = LoanApplication.objects.all().order_by('-applied_at')
    return render(request, 'app/admin_dashboard.html', {'loans': loans})

# Approve Loan
def approve_loan(request, loan_id):
    loan = get_object_or_404(LoanApplication, id=loan_id)
    loan.status = 'Accepted'
    loan.save()
    return redirect('users:admin_dashboard')

# Reject Loan
def reject_loan(request, loan_id):
    loan = get_object_or_404(LoanApplication, id=loan_id)
    loan.status = 'Rejected'
    loan.save()
    return redirect('users:admin_dashboard')


from django.shortcuts import render, redirect
from django.contrib import messages
import re

# Import your form and model
from .forms import AddIDForm
from .models import VerifyID
def add_id(request):
    form = AddIDForm()
    if request.method == "POST":
        form = AddIDForm(request.POST)
        if form.is_valid():
            aadhar = form.cleaned_data['aadhar_number'].strip()
            pan = form.cleaned_data['pan_number'].strip().upper()
            username = form.cleaned_data['username'].strip()

            # Field-level validation
            if len(aadhar) != 12 or not aadhar.isdigit():
                form.add_error('aadhar_number', "Aadhar must be exactly 12 digits.")
            if not re.match(r'^[A-Z]{5}[0-9]{4}[A-Z]$', pan):
                form.add_error('pan_number', "PAN must be in format ABCDE1234F.")

            # Duplicate checks
            if not form.errors:
                if VerifyID.objects.filter(aadhar_number=aadhar).exists():
                    form.add_error('aadhar_number', "This Aadhar number already exists.")
                if VerifyID.objects.filter(pan_number=pan).exists():
                    form.add_error('pan_number', "This PAN number already exists.")

            # Save if no errors
            if not form.errors:
                form.save()
                messages.success(request, "ID added successfully!")
                return redirect('users:list_ids')  # <-- redirect to list

    return render(request, 'app/add.html', {'form': form})
  

# Page to display all stored IDs
def list_ids(request):
    all_ids = VerifyID.objects.all()
    return render(request, 'app/list.html', {'all_ids': all_ids})  # <-- template path matches app

    