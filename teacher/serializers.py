from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from django.core.mail import send_mail


from .models import Teacher
from school.settings import EMAIL_HOST_USER


User = get_user_model()


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(min_length=6, write_only=True, required=True)

    class Meta:
        model = User
        fields = ['full_name','phone', 'subject', 'username', 'password', 'password2']

    def validate(self, attrs):
        p = attrs.get('password')
        p2 = attrs.pop('password2')

        if p != p2:
            raise serializers.ValidationError('Пароли не совпадают!')
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
        

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    def validate(self, username):
        if not User.objects.filter(username=username).exists():
            raise serializers.ValidationError('Нет такого пользователя')
        print(username)
        return username

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise serializers.ValidationError('Данные введены не корректно')
            attrs['user'] = user
            return attrs

