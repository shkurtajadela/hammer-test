from django.contrib import admin
from django.urls import path, include
from user.views import verification_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('user.urls')),
    path('', verification_page)
]
