# django库
from django.urls import path, include
# rest_framework库
from rest_framework.routers import DefaultRouter
# app
from .views import *


router = DefaultRouter()  # 1.有根路由
router.register(r"userReg", UserRegViewSet, 'userReg')

urlpatterns = [
    path("", include(router.urls)),
]
urlpatterns += router.urls
