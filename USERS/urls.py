from USERS import views
from django.urls import path
from USERS import views
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
#     TokenVerifyView
# )
from .views import *
urlpatterns = [
    path('register', views.RegisterAPIView.as_view(), name="register"),
    path('login', views.LoginAPIView.as_view(), name="login"),
    path('user', views.AuthUserAPIView.as_view(), name="user"),
    path('<str:user_id>/Advisor/List',AdvisorList.as_view(), name='Advisor_List'),
    path('<str:user_id>/Advisor/<str:advisor_id>/',AdvisorBooking.as_view(),name="Advisor_booking"),
    path('<str:user_id>/Advisor/booking', AdvisorBooked.as_view(), name="Advisor_booked"),
]



