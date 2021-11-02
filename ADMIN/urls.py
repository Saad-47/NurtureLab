from django.urls import path,include
#from .views import AdvisorView
from . import views
from rest_framework import routers
router = routers.DefaultRouter()
router.register('', views.AdvisorView)

urlpatterns = [
    path("",views.apiOverview),
    path("Admin/advisor",include(router.urls)), 
]