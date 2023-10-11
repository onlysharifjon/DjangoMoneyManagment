# import models
from .models import UserRegistration, MoneyManagment

# import serializer in rest_framework


from rest_framework import serializers


class Money_monthly_serializer(serializers.ModelSerializer):
    class Meta:
        model = UserRegistration
        #field username
        fields = ['username']

class Money_monthly_serializer_send(serializers.ModelSerializer):
    class Meta:
        model = MoneyManagment
        fields = '__all__'
