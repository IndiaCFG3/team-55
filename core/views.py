from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import CSV

@login_required(login_url="account/login")	
def home(request):
	return render(request, 'core/home.html')


def error_404_view(request, exception):
	return render(request, '404.html')

@login_required(login_url="account/login")
def upload_csv(request):
	if request.method == "POST":
		csv_file = request.FILES['file']
		if not csv_file.name.endswith('.csv'):
			messages.error(request, 'THIS IS NOT A CSV FILE')
			return render(request, 'core/csv_upload.html')
		csv = CSV(csv_file=csv_file)
		csv.save()
		messages.success(request, 'Uploaded!')

		return redirect('home')
		
	else:
		return render(request, 'core/csv_upload.html')