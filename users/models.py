from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

USER_TYPE_CHOICES = (
    ('admin', 'Admin'),
    ('customer', 'Customer'),
)

class CustomUser(AbstractUser):
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='customer')
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    profile_photo = models.ImageField(upload_to='profiles/', default='default.jpg', blank=True, null=True)

    def __str__(self):
        return f"{self.username} ({self.user_type})"


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        from PIL import Image
        img = Image.open(self.avatar.path)
        if img.height > 100 or img.width > 100:
            img.thumbnail((100, 100))
            img.save(self.avatar.path)

            
from django.db import models

class VerifyID(models.Model):
    username = models.CharField(max_length=100)
    aadhar_number = models.CharField(max_length=12)
    pan_number = models.CharField(max_length=10)

    def __str__(self):
        return self.username

class UserPredictModel1(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    Gender = models.IntegerField()
    Married = models.IntegerField(null=True, blank=True)
    Dependents = models.IntegerField()
    Education = models.IntegerField()
    Self_Employed = models.IntegerField(null=True, blank=True)
    ApplicantIncome = models.FloatField()
    CoapplicantIncome = models.FloatField()
    LoanAmount = models.FloatField()
    Loan_Amount_Term = models.FloatField()
    Property_Area = models.IntegerField()
    Marital_status = models.IntegerField(null=True, blank=True)
    Employee_type = models.IntegerField(null=True, blank=True)
    Industrial_sector = models.CharField(max_length=100, null=True, blank=True)
    Existing_monthly_EMIs = models.FloatField(null=True, blank=True)
    Monthly_household_expenses = models.FloatField(null=True, blank=True)
    Total_value_of_assets = models.FloatField(null=True, blank=True)
    Loan_purpose = models.IntegerField(null=True, blank=True)
    Loan_Status = models.CharField(max_length=10)
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        username = self.user.username if self.user else "Anonymous"
        return f"{username} - {self.Loan_Status}"