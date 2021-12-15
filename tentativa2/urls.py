from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('tentativa2.core.urls', namespace='core')),
    path('accounts/', include('tentativa2.accounts.urls')),  # without namespace
    path('admin/', admin.site.urls),
]
