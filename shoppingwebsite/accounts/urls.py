from django.contrib import admin
from django.urls import path
from accounts.views import login_page



urlpatterns = [
    path('acoount/', login_page, name="login"),  # ← typo in 'account'
]