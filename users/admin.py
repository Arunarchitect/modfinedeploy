from django.contrib import admin
from .models import CustomUser, SubscribedUsers
# Register your models hERE

class SubscribedUsersAdmin(admin.ModelAdmin):
    list_display = ('email', 'name','created_date')



admin.site.register(CustomUser)
admin.site.register(SubscribedUsers, SubscribedUsersAdmin)