import email
from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from UserApp.models import CatDog, FinancialAccount, User
from django.contrib.auth.hashers import make_password, check_password
from UserApp.models import UserType


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class AuthSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    email = serializers.EmailField()

    def validate(self, attrs):
        users = User.objects.filter(email=attrs['email'])
        if users.exists():
            pwd_valid = check_password(
                attrs['password'],
                users.values('password')[0]['password']
            )
            if pwd_valid:
                attrs['password'] = users.values('password')[0]['password']
                return attrs
            else:
                raise serializers.ValidationError(
                    'كلمة المرور غير صحيحة',
                    'password'
                )
        else:
            raise serializers.ValidationError(
                detail='الحساب غير موجود يمكنك انشاء حساب جديد'
            )

    def update(self, instance, validated_data):
        return User.objects.filter(email=validated_data['email']).update(validated_data)


class UserTypeSerializer(serializers.Serializer):
    class Meta:
        model = UserType
        fields = '__all__'


class FinancialAccountSerializer(serializers.ModelSerializer):
    class Mete:
        models = FinancialAccount
        fields = "__all__"

class CatDogSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatDog
        fields = "__all__"
