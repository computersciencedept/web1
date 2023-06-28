from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


from django.contrib import admin
from .models import CustomUser
from .forms import UserRegistrationForm
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = UserRegistrationForm
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Other Personal info',
            {
                'fields': (
                    'status',
                )
            }
        )
    )


admin.site.register(CustomUser,CustomUserAdmin)

# Register your models here.
