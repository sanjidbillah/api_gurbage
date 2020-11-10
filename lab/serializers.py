from rest_framework import serializers
from .models import MyModel,ChildTable
class userDataSerial(serializers.ModelSerializer):
      class Meta:
            model = MyModel
            fields="__all__"


class userChildSerial(serializers.ModelSerializer):
      class Meta:
            model = ChildTable
            fields="__all__"