from django.urls import path

from user.views import LoginTestView, RegisterTestView

app_name = 'user'

urlpatterns = [
    path('login/', LoginTestView.as_view(), name='login-view'),
    path('register/', RegisterTestView.as_view(), name='register-view'),
]
