from django import template

from email_notification.forms import EmailSubscriptionForm

register = template.Library()


@register.inclusion_tag('email_notification/email_subscription.html')
def get_email_subscription_form_for_posts():
    return {"EmailSubscriptionForm": EmailSubscriptionForm}


@register.inclusion_tag('email_notification/email_subscription_footer.html')
def get_email_subscription_form_footer():
    return {"EmailSubscriptionForm": EmailSubscriptionForm}
