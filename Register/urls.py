from django.urls import path
from Register.views import registration

urlpatterns = [
    path('', registration)
]