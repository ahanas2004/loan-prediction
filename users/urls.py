from django.urls import path
from .views import home,index, profile, AdminRegisterView,logout_view,AdminLoginView
from . import views
app_name = 'users'
urlpatterns = [
    path('', home, name='users-home'),
    path('adminhome',views.adminhome,name='adminhome'),
    path('register/', AdminRegisterView.as_view(), name='register'),
    path('login/', AdminLoginView.as_view(), name='login'),
    path('profile/', profile, name='users-profile'),
    path('logout_view/',logout_view,name='logout_view'),
    path('index/', index, name='users-index'),

    path('loan/',views.loan,name='loan'),

    path('loan_db',views.loan_db,name='loan_db'),
    path('output',views.output,name='output'),
    path('output1',views.output1,name='output1'),
    path('output2',views.output2,name='output2'),
    path('output3',views.output3,name='output3'),
    path('output10',views.output10,name='output10'),
    path('add-id/',views.add_id,name='add_id'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('approve-loan/<int:loan_id>/', views.approve_loan, name='approve_loan'),
    path('reject-loan/<int:loan_id>/', views.reject_loan, name='reject_loan'),
    path('get-loan-by-username/', views.get_loan_application_by_username, name='get-loan-by-username'),
    path('add/', views.add_id, name='add_id'),
    path('list/', views.list_ids, name='list_ids'),
    ]