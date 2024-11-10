from courses.admin import admin_site
from django.urls import path, re_path, include

urlpatterns = [
    path('', include('courses.urls')),
    path('admin/', admin_site.urls),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
]
