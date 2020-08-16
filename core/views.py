from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import CSV
from .dataframe import *

def home(request):
	return render(request, 'core/sam_home1.html')


def display_chart(request):
	return render(request, 'core/chartsPage.html')


def chart(request):
	dict_fin = {
		'type' : 'column',
		'title' : 'Student Data',
		'catogeries' :['Jan', 'Feb', 'March', 'April', 'June', 'July'],
		'series' : [{
					'name' : 'Attendance',
					'data' : [3, 1, 4, 1, 7, 2],
						'color' : 'blue'} , 
						
					{'name' : 'Students Enrolled',
					'data' : [1, 3, 5, 7, 4, 2],
						'color' : 'green'},

					{   'name' : 'Test Scores',
					'data' : [1, 3, 5, 7, 4, 2],
						'color' : 'red'}
							]
	}

	# dict_fin = {
	# 	'type' : 'pie',
	# 	'title' : 'attendace',
	# 	'data' :[['May', 37.5],
	# ['Nov', 12.5],
	# ['Jun', 12.5],
	# ['Jan', 12.5],
	# ['Dec', 12.5],
	# ['Feb', 12.5]],
	# }

	return render(request, 'core/chart.html', { "dataset": dict_fin })


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
		# messages.success(request, 'Uploaded!')

		return redirect('display-chart')
		
	else:
		return render(request, 'core/csv_upload.html')