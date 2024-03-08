from collections.abc import Iterable
from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError

# Create your models here.

Area_Choice=(    ('top','Top'),
                 ('button','Button'),
                 ('left','left'),
                 ('right','Rignt'))
class Advertisment(models.Model):
    company_name = models.CharField(max_length=255)
    area = models.CharField(max_length=255,choices=Area_Choice,default=1)
    price = models.PositiveIntegerField(null=True,blank=True)
    start_time= models.DateTimeField(default = timezone.now())
    end_time  = models.DateTimeField()




    def is_time_limit_exceed(self):
        if timezone.now() > self.end_time:
            return ({'msg':"time limit exceeded "})
        
    

    def time_remaining(self):
        if timezone.now() > self.end_time:
            return self.end_time - timezone.now()
        else:
            return timezone.timedelta()
        


   

    def save(self, *args, **kwargs):
            if self.start_time is None or self.start_time >= self.end_time:
                raise ValidationError("Start time must be set and before end time.")
            super(Advertisment, self).save(*args, **kwargs)  
    

    def __str__(self) :
        
        return self.company_name