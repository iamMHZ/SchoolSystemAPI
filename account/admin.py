# Register your models here.

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.admin import gettext

from .models import User


class CustomUserAdmin(UserAdmin):
    """Customize the admin page """
    # https://docs.djangoproject.com/en/3.2/topics/auth/customizing/

    ordering = ['id']
    list_display = ['username', ]

    # use for editing a user
    fieldsets = (
        (None, {'fields': ('username', 'password',)}),
        (gettext('Personal Info'), {'fields': ('first_name', 'last_name', 'school_name',)}),
        (
            gettext('Permissions'),
            {'fields': ('is_active', 'is_staff', 'is_superuser', 'is_student', 'is_teacher',)}
        ),
        (gettext('Important dates'), {'fields': ('last_login', 'date_joined',)})
    )

    # use for creating user
    add_fieldsets = (

        (None, {
            'classes': ('wide',),
            'fields': (
                'username', 'first_name', 'last_name', 'school_name',
                'password1', 'password2',
                'is_active', 'is_staff', 'is_superuser',
                'is_student', 'is_teacher',
            ),
        }),

    )


# Another way of customizing django admin page

# class CustomUserAdmin(UserAdmin):
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     model =  User
#     list_display = ['email', 'username',]


admin.site.register(User, CustomUserAdmin)
