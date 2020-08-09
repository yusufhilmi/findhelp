from rest_framework import serializers

from findhelp.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "name", "url"]

        extra_kwargs = {
            "url": {"view_name": "api:user-detail", "lookup_field": "username"},
            "username": {"read_only": True}
        }
    
    # def save(self):
    #     user = User(
    #         email=self.validated_data['email'],
    #         username=self.validated_data['username'],
    #     )