from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer
from djoser.conf import settings
from .models import User


class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    """
        Наследуется от UserCreateSerializer модуля djoser. Поля,
        определенные в метаклассе, включают в себя все поля родителя
        плюс username и photo(фото профиля)
    """
    class Meta(BaseUserRegistrationSerializer.Meta):
        model = User
        fields = tuple(User.REQUIRED_FIELDS) + (
            settings.LOGIN_FIELD,
            settings.USER_ID_FIELD,
            'username', 'password', 'photo'
        )
