from pyexpat import model
from rest_framework import serializers
from .models import Job, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password']


class JobsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'
        # optional_fields = ['summary',]
        read_only_fields = ['created_at', 'id']
