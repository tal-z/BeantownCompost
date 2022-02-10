from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from managers.forms import LoginForm, PasswordResetForm, PasswordChangeForm, SetPasswordForm

urlpatterns = [
    path('my_sites/', views.my_sites, name='my_sites'),
    path('my_account/', views.my_account, name='my_account'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='managers/auth/login.html',
            authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='managers/auth/logout.html'), name='logout'),
    path('password_change/', auth_views.PasswordChangeView.as_view(
            template_name='managers/auth/password_change.html',
            form_class=PasswordChangeForm), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='managers/auth/password_change_done.html'), name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(
            template_name='managers/auth/password_reset_form.html', 
            email_template_name='managers/auth/password_reset_email.html', 
            subject_template_name='managers/auth/password_reset_subject.txt',
            form_class=PasswordResetForm), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='managers/auth/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
            template_name='managers/auth/password_reset_confirm.html',
            form_class=SetPasswordForm), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='managers/auth/password_reset_complete.html'), name='password_reset_complete'),
]
