
from rest_framework import serializers

from .models import Advisor
class AdvisorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advisor
        fields = ("Advisor_name","Advisor_image")

class AdvisorBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advisor
        fields = ("Booking_Time",)

class AdvisorBookedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Advisor
        fields = ("Advisor_name","Advisor_image","id","Booking_Time","Booking_Id")