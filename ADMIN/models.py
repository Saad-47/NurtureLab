from django.db import models
from datetime import datetime, timezone

from django.db.models.expressions import Value
# Create your models here.
from django.utils.text import slugify
from django.utils import timezone
class Advisor(models.Model):
    Advisor_name = models.CharField(max_length=30)
    Advisor_image = models.ImageField(upload_to='advisor/profile_images', default="post-default.jpg", blank=True,null = True)
    Advisor_client = models.CharField(max_length=20, default="None")
    Booking_Id = models.SlugField(max_length=50,default="Not_Booked" ,blank=True,null =True)
    Booking_Time = models.CharField(max_length=100,default=timezone.now,help_text=(
            'format -> YYYY-MM-DD HH:MM:SS'))

    def save(self, *args,**kwargs):
        self.Booking_Id = slugify(str(self.Advisor_client) + str(self.Booking_Time))
        super(Advisor, self).save(*args,**kwargs)

m = Advisor()