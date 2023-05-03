from rest_framework import serializers
from purchase.models import Purchase


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = '__all__'
