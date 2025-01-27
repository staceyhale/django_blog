from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path("__debug__/", include("debug_toolbar.urls")),
    # path('captcha/', include('captcha.urls')),
    path('', include('blog.urls')),
    path('user/', include('user.urls', namespace='user')),
    path('comments/', include('comments.urls', namespace='comments')),
    path('email/', include('email_notification.urls', namespace='email')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
