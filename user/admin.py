from django.contrib import admin

from user.models import UserProfile, CustomUser


admin.site.register(CustomUser)


@admin.register(UserProfile)
class UserAdmin(admin.ModelAdmin):
    save_on_top = True
    save_as = True

    list_display = ('id', 'user', 'bio', 'birth_date')
    fields = ('user', 'bio', 'photo', 'birth_date')
    list_display_links = ('id', 'user',)
