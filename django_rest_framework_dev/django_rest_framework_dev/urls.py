from django.urls import path
from django.conf.urls import url, include
from django.contrib import admin

from blog.urls import router as blog_router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(blog_router.urls)),
]

