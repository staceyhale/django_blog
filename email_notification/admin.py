from django.contrib import admin

from email_notification.models import Contact, EmailSubscription


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'subject', 'profile', 'email', 'content', 'is_answered')
    list_display_links = ('id', 'subject', 'profile', 'email')
    list_filter = ('is_answered',)
    search_fields = ('user', 'is_answered', 'email')
    readonly_fields = ('subject', 'profile', 'email', 'content',)


@admin.register(EmailSubscription)
class EmailSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('email',)
