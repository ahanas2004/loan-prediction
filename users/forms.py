from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from . models import UserPredictModel1

from .models import Profile


from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class AdminRegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = 'admin'
        user.is_staff = True
        user.is_superuser = True
        if commit:
            user.save()
        return user

class AdminLoginForm(AuthenticationForm):
    pass



class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email']


class UpdateProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    class Meta:
        model = Profile
        fields = ['avatar', 'bio']



        
from django import forms
from .models import UserPredictModel1

class UserPredictDataForm1(forms.ModelForm):
    class Meta:
        model = UserPredictModel1
        fields = [
            'Gender', 'Dependents', 'Education',
            'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term',
            'Property_Area',
            # Additional fields
            'Marital_status', 'Employee_type', 'Industrial_sector',
            'Existing_monthly_EMIs', 'Monthly_household_expenses',
            'Total_value_of_assets', 'Loan_purpose'
        ]
        widgets = {
            'Gender': forms.Select(choices=[('Male', 'Male'), ('Female', 'Female')]),
            'Married': forms.Select(choices=[('Yes', 'Yes'), ('No', 'No')]),
            'Dependents': forms.TextInput(attrs={'class': 'form-control'}),
            'Education': forms.Select(choices=[('Graduate', 'Graduate'), ('Not Graduate', 'Not Graduate')]),
            'Self_Employed': forms.Select(choices=[('Yes', 'Yes'), ('No', 'No')]),
            'ApplicantIncome': forms.NumberInput(attrs={'class': 'form-control'}),
            'CoapplicantIncome': forms.NumberInput(attrs={'class': 'form-control'}),
            'LoanAmount': forms.NumberInput(attrs={'class': 'form-control'}),
            'Loan_Amount_Term': forms.NumberInput(attrs={'class': 'form-control'}),
            'Property_Area': forms.Select(choices=[('Urban', 'Urban'), ('Rural', 'Rural'), ('Semiurban', 'Semiurban')]),
            # Additional fields can have default input types; customize as needed
            'Marital_status': forms.Select(choices=[('Single','Single'),('Married','Married'),('Divorced','Divorced')]),
            'Employee_type': forms.Select(choices=[('Salaried','Salaried'),('Self-employed','Self-employed')]),
            'Industrial_sector': forms.TextInput(attrs={'class': 'form-control'}),
            'Existing_monthly_EMIs': forms.NumberInput(attrs={'class': 'form-control'}),
            'Monthly_household_expenses': forms.NumberInput(attrs={'class': 'form-control'}),
            'Total_value_of_assets': forms.NumberInput(attrs={'class': 'form-control'}),
            'Loan_purpose': forms.Select(choices=[
                ('Home','Home'), ('Car','Car'), ('Education','Education'), ('Business','Business'), ('Personal','Personal')
            ]),
            'aadhar_number': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Aadhar Number'}),
            'pan_number': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter PAN Number'}),
        }

from django import forms
from .models import VerifyID

class AddIDForm(forms.ModelForm):

    class Meta:
        model = VerifyID
        fields = [ 'username','aadhar_number','pan_number' ]

        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Username'}),
            'aadhar_number': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Aadhar Number'}),
            'pan_number': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter PAN Number'}),
        }


from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'password1', 'password2']
