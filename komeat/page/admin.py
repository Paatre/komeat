from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import UserProfile

# Register your models here.


class MemberUserAdmin(UserAdmin):
    UserAdmin.list_display += ('is_member',)

    def is_member(self, obj):
        user = User.objects.get(pk=obj.id)
        return user.groups.filter(name='member').exists()

    is_member.boolean = True


admin.site.unregister(User)
admin.site.register(User, MemberUserAdmin)
admin.site.register(UserProfile)
