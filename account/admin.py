from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from .models import User


class AccountAdmin(UserAdmin):
	list_display = ('id', 'email', 'username', 'date_joined', 'last_login', 'is_admin', 'is_staff')
	list_display_links = ('id', 'email', 'username')
	search_fields = ('email', 'username',)
	readonly_fields = ('date_joined', 'last_login')
	list_per_page = 25

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()

admin.site.register(User, AccountAdmin)