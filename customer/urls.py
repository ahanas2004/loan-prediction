from django.urls import path
from . import views
from .views import CustomerRegisterView,CustomerLoginView    

app_name = 'customer'

urlpatterns = [
    path('home/', views.customer_home, name='customer_home'),
    path('dashboard/', views.customer_dashboard, name='customer_dashboard'),
    path('register/', CustomerRegisterView.as_view(), name='customer_register'),
    path('login/', CustomerLoginView.as_view(), name='customer_login'),
    path('logout/', views.customer_logout_view, name='customer_logout'),
    path('apply-loan/', views.apply_loan, name='apply_loan'),
]

