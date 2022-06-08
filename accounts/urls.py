
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from accounts.views import MainLoginView, RegisterView

app_name = 'account'

urlpatterns = [
    path('login/', MainLoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('log-out', LogoutView.as_view(), name='log-out'),
]