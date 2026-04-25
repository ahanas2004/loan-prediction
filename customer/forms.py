from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from users.models import CustomUser

class CustomerRegisterForm(UserCreationForm):
    phone_number = forms.CharField(max_length=15, required=True)
    profile_photo = forms.ImageField(required=False)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'phone_number', 'profile_photo', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = 'customer'
        user.is_staff = False
        user.is_superuser = False
        if commit:
            user.save()
        return user

class CustomerLoginForm(AuthenticationForm):
    pass

from django import forms
from .models import LoanApplication

class LoanApplicationForm(forms.ModelForm):

    # Add Aadhar and PAN as extra fields
    aadhar_number = forms.CharField(
        max_length=12,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Aadhar Number'})
    )

    pan_number = forms.CharField(
        max_length=10,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter PAN Number'})
    )

    class Meta:
        model = LoanApplication
        exclude = ['user', 'status', 'applied_at']

        widgets = {

            # Personal Details
            'gender': forms.Select(choices=[('Male','Male'), ('Female','Female')], attrs={'class':'form-control'}),
            'marital_status': forms.Select(choices=[('Single','Single'),('Married','Married'),('Divorced','Divorced')], attrs={'class':'form-control'}),
            'dependents': forms.NumberInput(attrs={'class':'form-control'}),
            'education': forms.Select(choices=[('Graduate','Graduate'),('Not Graduate','Not Graduate')], attrs={'class':'form-control'}),
            'Married': forms.Select(choices=[('Yes','Yes'),('No','No')], attrs={'class':'form-control'}),
            'self_employed': forms.Select(choices=[('Yes','Yes'),('No','No')], attrs={'class':'form-control'}),

            # Employment
            'employee_type': forms.Select(choices=[('Salaried employee','Salaried employee'),('Self employee','Self employee')], attrs={'class':'form-control'}),
            'industrial_sector': forms.Select(choices=[('IT/software','IT/software'),('Business','Business'),('Medical','Medical'),('Real estate','Real estate'),('Logistics','Logistics')], attrs={'class':'form-control'}),

            # Financial Details
            'applicant_income': forms.NumberInput(attrs={'class':'form-control'}),
            'coapplicant_income': forms.NumberInput(attrs={'class':'form-control'}),
            'existing_monthly_EMIs': forms.NumberInput(attrs={'class':'form-control'}),
            'monthly_household_expenses': forms.NumberInput(attrs={'class':'form-control'}),
            'total_value_of_assets': forms.NumberInput(attrs={'class':'form-control'}),

            # Loan Details
            'loan_amount': forms.NumberInput(attrs={'class':'form-control'}),
            'loan_amount_term': forms.NumberInput(attrs={'class':'form-control'}),
            'loan_purpose': forms.Select(choices=[('Debt loan','Debt loan'),('Car loan','Car loan'),('Travel loan','Travel loan'),('House loan','House loan'),('Personal loan','Personal loan')], attrs={'class':'form-control'}),
            'credit_history': forms.Select(choices=[(1,'Good (1)'),(0,'Bad (0)')], attrs={'class':'form-control'}),
            'property_area': forms.Select(choices=[('Urban','Urban'),('Rural','Rural'),('Semiurban','Semiurban')], attrs={'class':'form-control'}),
        }