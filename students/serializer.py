from rest_framework import serializers
from .models import My_Course
from Accounts.models import User

class My_Course_Serializer(serializers.ModelSerializer):

    class Meta:
        model = My_Course
        # fields = ('user','my_course','paid','date')
        fields = '__all__'
        depth = 1