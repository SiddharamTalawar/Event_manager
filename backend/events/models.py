from django.db import models

class event(models.Model):
    event_name = models.CharField(max_length=250)
    discription = models.CharField(max_length=500)
    Agenda = models.CharField(max_length=500)
    tags = models.CharField(max_length=150)
    time = models.DateTimeField(null=True,blank=True)
    location = models.CharField(max_length=250)
    image = models.ImageField(null=True,blank=True)
    is_liked = models.BooleanField(default=False)
    #user_id = models.IntegerField(null=True, blank=True)

    def __repr__(self):
        return self.event_name

