from django.contrib import admin

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from art_gallery_web.gallery_auth.models import UserProfile


class ProfileInlineAdmin(admin.StackedInline):
    model = UserProfile
    verbose_name_plural = 'Profile'


class UserAdmin(BaseUserAdmin):
    inlines = (
        ProfileInlineAdmin,
    )
    list_display = ('username', 'email',)
    list_filter = ('username',)


admin.site.register(UserProfile)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
