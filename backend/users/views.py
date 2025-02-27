import core.generics
import users.models
import users.serializers


class UserAPIView(core.generics.CRUDAPIView,
                  core.generics.URLKwargsMixin):
    serializer_class = users.serializers.UserSerializer
    queryset = users.models.User.objects.all()
    pk_url_kwarg_name = 'uid'
