import rest_framework.serializers

import users.models


class UserSerializer(rest_framework.serializers.ModelSerializer):

    class Meta:
        model = users.models.User
        fields = '__all__'
