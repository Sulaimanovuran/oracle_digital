from django.urls import path
from .views import *

urlpatterns = [
    path('registration/', RegistrationApiView.as_view()),
    path('login/', LoginApiView.as_view()),
    path('logout/', LogOutApiView.as_view()),
]