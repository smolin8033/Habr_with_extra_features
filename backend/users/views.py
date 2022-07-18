from djoser.views import UserViewSet as BaseViewSet


class UserViewSet(BaseViewSet):
    http_method_names = ['get', 'post']
    me = None
    activation = None
    resend_activation = None
    set_password = None
    reset_password = None
    reset_password_confirm = None
    set_username = None
    reset_username = None
    reset_username_confirm = None
