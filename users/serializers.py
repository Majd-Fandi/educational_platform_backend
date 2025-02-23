# OLD : USERNAME / PASSWORD :

# from rest_framework import serializers
# from django.contrib.auth import get_user_model
# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# CustomUser = get_user_model()

# class CustomUserSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True)

#     class Meta:
#         model = CustomUser
#         fields = ('username', 'password', 'email', 'is_student', 'is_instructor')

#     def create(self, validated_data):
#         user = CustomUser.objects.create_user(
#             username=validated_data['username'],
#             password=validated_data['password'],
#             email=validated_data.get('email', ''),
#             is_student=validated_data.get('is_student', False),
#             is_instructor=validated_data.get('is_instructor', False),
#         )
#         return user

# class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
#     @classmethod
#     def get_token(cls, user):
#         token = super().get_token(user)
#         token['is_student'] = user.is_student
#         token['is_instructor'] = user.is_instructor
#         return token


# ======================================================================================================================

# NEW : EMAIL / PASSWORD 

from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

CustomUser = get_user_model()

class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ('username','email', 'password', 'is_student', 'is_instructor')

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password'],
            is_student=validated_data.get('is_student', False),
            is_instructor=validated_data.get('is_instructor', False),
        )
        return user

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        # Use email instead of username
        attrs['username'] = attrs.get('email')
        return super().validate(attrs)