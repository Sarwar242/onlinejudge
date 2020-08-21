from rest_framework import serializers
import datetime
from django.utils import timezone
from django.contrib.auth import get_user_model
from rest_framework_jwt.settings import api_settings

jwt_payload_handler                 = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler                  = api_settings.JWT_ENCODE_HANDLER
jwt_response_payload_handler        = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER
expire_delta                        = api_settings.JWT_REFRESH_EXPIRATION_DELTA


User = get_user_model()

class UserRegisterSerializer(serializers.ModelSerializer):
    password                = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    confirm_password        = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    token                   = serializers.SerializerMethodField(read_only=True)
    expires                 = serializers.SerializerMethodField(read_only=True)
    message                 = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'password',
            'confirm_password',
            'token',
            'expires',
            'message',
        ]

    def get_token(self, obj):
        user                = obj
        payload             = jwt_payload_handler(user)
        token               = jwt_encode_handler(payload)
        return token

    def get_expires(self, obj):
        return timezone.now() + expire_delta - datetime.timedelta(seconds=200)

    def get_message(self, obj):
        return 'Thanks you for registering, Please confirm your email before login.'


    def validate_email(self, value):
        email_ck            = User.objects.filter(email__iexact=value)
        if email_ck.exists():
            raise serializers.ValidationError("Email is in use, please try another one!")
        return value

    def validate_username(self,value):
        username_ck         = User.objects.filter(username__iexact=value)
        if username_ck.exists():
            raise serializers.ValidationError("An user with this username already exists, please try another!")
        return value

    def validate(self, data):
        pw1                 = data.get('password')
        pw2                 = data.pop('confirm_password')
        if pw1 != pw2:
            raise serializers.ValidationError("Passwords didn\'t matched!")
        return data

    def create(self, validated_data):
        user = User(
            username        = validated_data.get('username'),
            email           = validated_data.get('email'),
            first_name      = validated_data.get('first_name'),
            last_name       = validated_data.get('last_name'))
        user.set_password(validated_data.get('password'))
        user.is_active = False
        user.save()
        return user