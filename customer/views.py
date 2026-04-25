from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordChangeView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login
from .forms import CustomerRegisterForm, CustomerLoginForm

def customer_home(request):
    return render(request, 'customer/customer_home.html')

@login_required(login_url='customer:customer_login')
def customer_dashboard(request):
    return render(request, 'customer/customer_dashboard.html')



from django.shortcuts import render, redirect
from django.views import View
from .forms import CustomerRegisterForm
from django.contrib import messages

from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.views import LoginView
from django.contrib import messages
from .forms import CustomerRegisterForm, CustomerLoginForm

class CustomerRegisterView(View):
    form_class = CustomerRegisterForm
    template_name = 'customer/customer_register.html'

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class()})

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Customer registered successfully!")
            return redirect('customer:customer_login')
        return render(request, self.template_name, {'form': form})

class CustomerLoginView(LoginView):
    form_class = CustomerLoginForm
    template_name = 'customer/customer_login.html'

    def form_valid(self, form):
        user = form.get_user()
        if user.user_type != 'customer':
            messages.error(self.request, "You are not allowed to login here")
            return redirect('customer:customer_login')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('customer:customer_home')


class CustomerResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'customer/password_reset.html'
    email_template_name = 'customer/password_reset_email.html'
    subject_template_name = 'customer/password_reset_subject'
    success_message = "We've emailed you password reset instructions."
    success_url = reverse_lazy('customer:customer_login')

class CustomerChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'customer/change_password.html'
    success_message = "Password successfully changed."
    success_url = reverse_lazy('customer:customer_dashboard')

def customer_logout_view(request):
    auth_logout(request)
    return redirect('/')


from django.shortcuts import render, redirect
from .forms import LoanApplicationForm
from .models import LoanApplication
from django.contrib.auth.decorators import login_required


@login_required
def customer_dashboard(request):

    application = LoanApplication.objects.filter(user=request.user).first()

    if application:

        verified = VerifyID.objects.filter(
            username=request.user.username,
            aadhar_number=application.aadhar_number,
            pan_number=application.pan_number
        ).exists()

        if verified:
            application.verified = True
        else:
            application.verified = False

        application.save()

    return render(request, 'customer/customer_dashboard.html', {'application': application})

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from users.models import VerifyID
from .forms import LoanApplicationForm


@login_required
def apply_loan(request):

    if request.method == 'POST':

        form = LoanApplicationForm(request.POST)

        if form.is_valid():

            username = request.user.username
            aadhar = form.cleaned_data['aadhar_number'].strip()
            pan = form.cleaned_data['pan_number'].strip().upper()

            verified = VerifyID.objects.filter(
                username=username,
                aadhar_number=aadhar,
                pan_number=pan
            ).exists()

            if not verified:
                messages.error(request, "Aadhar or PAN not verified. Please check your details.")
                return render(request, 'customer/apply_loan.html', {'form': form})

            application = form.save(commit=False)

            application.user = request.user

            application.aadhar_number = aadhar
            application.pan_number = pan

            application.verified = True
            application.status = "Pending"

            application.save()
            messages.success(request, "Loan Application Submitted Successfully!")
            return redirect('customer:customer_dashboard')

    else:
        form = LoanApplicationForm()

    return render(request, 'customer/apply_loan.html', {'form': form})