from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db import models
from django.conf import settings
from django.db import models
from django.conf import settings

class LoanApplication(models.Model):
    # Link to the user dynamically
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    # Personal Details
    gender = models.CharField(max_length=10)
    marital_status = models.CharField(max_length=10)
    dependents = models.IntegerField()
    education = models.CharField(max_length=20)
    Married = models.CharField(max_length=5)
    self_employed = models.CharField(max_length=5)
    
    # Employment Details
    employee_type = models.CharField(max_length=50)
    industrial_sector = models.CharField(max_length=50)
    
    # Financial Details
    applicant_income = models.FloatField()
    coapplicant_income = models.FloatField()
    existing_monthly_EMIs = models.FloatField()
    monthly_household_expenses = models.FloatField()
    total_value_of_assets = models.FloatField()
    
    # Loan Details
    loan_amount = models.FloatField()
    loan_amount_term = models.FloatField()
    loan_purpose = models.CharField(max_length=50)
    credit_history = models.IntegerField(default=0)
    property_area = models.CharField(max_length=20)
    
    # Extra Fields for Verification
    aadhar_number = models.CharField(max_length=12 , default="000000000000")
    pan_number = models.CharField(max_length=10, default="XXXXXXXXXX")
    
   
    
    # Application status
    status = models.CharField(max_length=20, default='Pending')
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.loan_amount}"

