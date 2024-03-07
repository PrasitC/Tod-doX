from rest_framework import serializers
from .models import Task
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        
        exclude = ['user']
        
    def save(self, **kwargs):
        kwargs['user'] = self.context['request'].user
        return super().save(**kwargs)





class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields= ('username',  'email' , 'id')
        
        
        
        

class RegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model =User
        fields = ('username', 'email', 'id', 'password')
        extra_kwargs={'password':{
            'write_only' : True
        }}

    def create(self, validated_data):
        print(validated_data)
        
        user = User.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password'],
        )
        return user #super().create(validated_data)




class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
     

    def validate(self, attrs):
        user = authenticate(**attrs)
        if user and user.is_active:
        
            return user
        raise ValidationError("incorrect password")
