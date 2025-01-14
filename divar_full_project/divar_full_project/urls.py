
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('ads/', include('ads.urls')),
    path('payments/', include('payments.urls')),
]
