__all__ = ('UserViewSet',)

import rest_framework.viewsets

import users.models
import users.serializers


class UserViewSet(rest_framework.viewsets.ModelViewSet):
    serializer_class = users.serializers.UserSerializer
    queryset = users.models.User.objects.all()
    lookup_url_kwarg = 'uid'
