from django.urls import path

from user.views import LoginTestView, RegisterTestView, LogoutTestView

app_name = 'user'

urlpatterns = [
    path('login/', LoginTestView.as_view(), name='login-view'),
    path('logout/', LogoutTestView.as_view(), name='logout-view'),
    path('register/', RegisterTestView.as_view(), name='register-view'),
]
