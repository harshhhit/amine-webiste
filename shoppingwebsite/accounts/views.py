from django.shortcuts import render


def login_page(request):
    """
    Render the login page.
    """
    return render(request, 'accounts/login.html')
# Create your views here.
