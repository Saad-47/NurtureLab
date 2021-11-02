from rest_framework import serializers
from USERS.models import Users


class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        max_length=128, min_length=6, write_only=True)

    class Meta:
        model = Users
        fields = ('id','username', 'email', 'password','token')

    def create(self, validated_data):
        return Users.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        max_length=128, min_length=6, write_only=True)

    class Meta:
        model = Users
        fields = ('id','email', 'password', 'token')

        read_only_fields = ['token']
