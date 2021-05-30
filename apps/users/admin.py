from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from users.models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    pass

# admin.site.register(UserProfile, UserProfileAdmin)

admin.site.register(UserProfile, UserAdmin)


