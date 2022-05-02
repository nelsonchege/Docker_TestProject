from rest_framework import serializers
from .models import AccountsTable


class AccountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountsTable
        fields = '__all__'
        extra_kwargs = {"name": {"error_messages": {
            "required": "Give your name"}}}
