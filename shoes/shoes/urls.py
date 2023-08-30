from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import ShoesViewSet

# Создание экземпляра DefaultRouter
router = DefaultRouter()
# Регистрация вашего ViewSet с роутером
router.register(r'shoes', ShoesViewSet)
urlpatterns = [
        path('admin/', admin.site.urls),
        # Добавление путей, зарегистрированных в роутере, в общий список путей
        path('api/v1/', include(router.urls)),

    ]
