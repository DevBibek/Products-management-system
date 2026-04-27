from django.urls import path
from .views import log_in,register,log_out
from django.contrib.auth import views
urlpatterns = [
    path('login/',log_in,name="login_p"),
    path('register/',register,name="register_p"),
    path('logout/',log_out,name="logout_p"),
    #forgot password
   path('password_reset/', views.PasswordResetView.as_view(template_name = 'accounts/forgotpassword.html'), name='password_reset'),
   path('password_reset_done/', views.PasswordResetDoneView.as_view(template_name ="accounts/sendlink.html"), name='password_reset_done'),
   path('password_reset_confirm/<uidb64>/<token>/',views.PasswordResetConfirmView.as_view(template_name = "accounts/setpassword.html"), name='password_reset_confirm'),
   path('password_reset_complete/', views.PasswordResetCompleteView.as_view(template_name = "accounts/success.html"), name='password_reset_complete')
]

