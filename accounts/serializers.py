from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from accounts.models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ["id", "username", "email", "is_superuser", "password"]
        read_only_fields = ["id"]
        extra_kwargs = {"password": {"write_only": True}}

    username = serializers.CharField(
        max_length=150,
        validators=[
            UniqueValidator(
                queryset=Account.objects.all(),
                message="A user with that username already exists.",
            )
        ],
    )

    email = serializers.EmailField(
        max_length=100,
        validators=[
            UniqueValidator(
                queryset=Account.objects.all(),
                message="user with this email already exists.",
            )
        ],
    )

    is_superuser = serializers.BooleanField(required=False)

    def create(self, validated_data):
        is_superuser = validated_data.get("is_superuser", False)
        if is_superuser:
            return Account.objects.create_superuser(**validated_data)
        return Account.objects.create_user(**validated_data)
