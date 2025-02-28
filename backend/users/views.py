import django.contrib.auth.hashers

import rest_framework.generics
import rest_framework.serializers

import users.models
import users.serializers


class UserAPIView(rest_framework.generics.RetrieveUpdateDestroyAPIView,
                  rest_framework.generics.CreateAPIView):
    serializer_class = users.serializers.UserSerializer
    queryset = users.models.User.objects.all()
    lookup_url_kwarg = 'uid'

    def perform_create(
        self,
        serializer: rest_framework.serializers.Serializer,
    ) -> None:
        # here the data validation was already done by the serializer,
        # so the user's password is guaranteed to be valid,
        # and we can hash and save it now
        password_hash = django.contrib.auth.hashers.make_password(
            self.request.data['password'],
        )
        serializer.save(password=password_hash)
