from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views
router = DefaultRouter() # amader router

router.register('', views.ChefViewset) # router er antena
urlpatterns = [
    path('', include(router.urls)),
]