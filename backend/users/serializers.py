import rest_framework.serializers

import drfkwargs

import users.models


class UserSerializer(rest_framework.serializers.ModelSerializer):

    class Meta:
        model = users.models.User
        fields = rest_framework.serializers.ALL_FIELDS
        extra_kwargs = {
            model.password.field.name: {drfkwargs.WRITE_ONLY: True},
            model.user_permissions.field.name: {drfkwargs.WRITE_ONLY: True},
            model.groups.field.name: {drfkwargs.WRITE_ONLY: True},
        }
