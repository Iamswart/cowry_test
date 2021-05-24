from django.urls import path, include
from rest_framework.routers import DefaultRouter
from catalog import views


router = DefaultRouter()
router.register(r'test', views.TestViewSet)

urlpatterns = [
    path('', include(router.urls)),
]