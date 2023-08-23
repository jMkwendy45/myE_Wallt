from djoser.serializers import UserCreateSerializer


class CreateUserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields = ['email', 'username', 'password', 'first_name', 'last_name', 'phone_number']
