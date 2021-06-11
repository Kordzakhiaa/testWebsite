from django.urls import path

from ecommerce.views import TestView

app_name = 'ecommerce'

urlpatterns = [
    path('', TestView.as_view(), name='test-view'),
]
