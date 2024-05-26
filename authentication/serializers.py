from datetime import timezone
from authentication.models import Gender, User
from report.utils import last_submitted_report
from report.managers import ReportManager
from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

class UserLoginSerializer(serializers.ModelSerializer):
    phone_number = serializers.IntegerField()
    # name = serializers.CharField(max_length=100)
    # email = serializers.EmailField()
    # dob = serializers.DateField()
    # gender = serializers.CharField(max_length=20)
    password = serializers.CharField(max_length=68,min_length=8,write_only=True)
    access_token=serializers.CharField(max_length=255,read_only=True)
    refresh_token=serializers.CharField(max_length=255,read_only=True)

    class Meta:
        model=User
        fields=['phone_number','password','access_token','refresh_token']

    def validate(self, attrs):
        phone_number = attrs.get('phone_number')
        password = attrs.get('password')
        request=self.context.get('request')
        if phone_number and password:
            user = authenticate(request, phone_number=phone_number, password=password)

            if not user:
                message = 'Unable to log in with provided credentials.'
                raise serializers.ValidationError(message, code='authorization')
        else:
            message = 'Must include "phone_number" and "password".'
            raise serializers.ValidationError(message, code='authorization')
        tokens=user.tokens()
        name=user.name
        email=user.email
        dob=user.dob
        gender=user.gender
        lastSubmittedReport=last_submitted_report(user)
        return{
            'name':name,
            'email':email,
            'phone_number':phone_number,
            'dob':dob,
            'gender':gender,
            'access_token':tokens.get('access'),
            'refresh_token':tokens.get('refresh'),
            'lastSubmittedReport':lastSubmittedReport

        }

    def create(self,validated_data):
        return super().create(validated_data)

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68,min_length=8,write_only=True)

    class Meta:
        model=User
        fields=['phone_number','name','password','dob','gender','email']

    def validate(self, attrs):
        return attrs

    def create(self,validated_data):
        user=User.objects.create_user(
            phone_number=validated_data.get('phone_number'),
            name=validated_data.get('name'),
            password=validated_data.get('password'),
            email=validated_data.get('email'),
            dob=validated_data.get('dob'),
            gender=validated_data.get('gender')
        )
        return user

