from rest_framework import serializers
from .models import form1

class App1Serializer(serializers.Serializer):
    class Meta:
        model = form1
        fields = '__all__'