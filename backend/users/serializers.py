import typing

import django.contrib.auth.hashers

import rest_framework.serializers

import drfseriperm

import users.ffps
import users.models


class UserSerializer(drfseriperm.PermissionBasedModelSerializerMixin,
                     rest_framework.serializers.ModelSerializer):

    def save(self, **kwargs: typing.Any) -> None:
        password_hash = django.contrib.auth.hashers.make_password(
            self.validated_data['password'],
        )
        super().save(password=password_hash)

    class Meta:
        model = users.models.User
        list_fields_for_permissions = [
            users.ffps.DefaultUserFFP,
            users.ffps.DefaultUserUpdateExtendFFP,
            users.ffps.DefaultUserPostExtendFFP,
            users.ffps.AccountOwnerFFP,
            users.ffps.StaffFFP,
            users.ffps.SuperuserFFP,
        ]
