from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer
from djoser.conf import settings
from .models import User


class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    class Meta(BaseUserRegistrationSerializer.Meta):
        model = User
        fields = tuple(User.REQUIRED_FIELDS) + (
            settings.LOGIN_FIELD,
            settings.USER_ID_FIELD,
            'password', 'username', 'photo'
        )


"""
Так не работает
class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    class Meta(BaseUserRegistrationSerializer.Meta):
        model = User
        fields = '__all__'
"""
