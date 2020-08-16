from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url="account/login")	
def home(request):
	return render(request, 'core/home.html')


def error_404_view(request, exception):
	return render(request, '404.html')