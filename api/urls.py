from django.urls import include, path
from django.contrib import admin
from api.views import logs_palpite, logs_palpite_arquivo

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/logs/arquivo', logs_palpite_arquivo),
    path('api/v1/logs/palpite', logs_palpite),
    path('admin/', admin.site.urls),
]