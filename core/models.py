from django.db import models


def csv_directory_path(instance, filename):
	# file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
	return 'csv/{0}'.format(filename)


class CSV(models.Model):
	csv_file				= models.FileField(blank=True,upload_to=csv_directory_path)