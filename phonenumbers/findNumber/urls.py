from django.urls import path
from . import views

urlpatterns = [
    path('', views.find_number),
    path('find-number-api/', views.FindNumberDetails.as_view()),
    path('find-numbers-in-text-api/', views.FindNumbersInText.as_view()),
]
