from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser,classroom


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
class classroomAdmin(admin.ModelAdmin):

    model = classroom
    list_display  = [f.name for f in classroom._meta.fields]

admin.site.register(classroom,classroomAdmin)

# Register your models here.
