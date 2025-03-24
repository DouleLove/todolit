import rest_framework.request
import rest_framework.views


class IsSuperuser(rest_framework.permissions.BasePermission):

    def has_permission(
        self,
        request: rest_framework.request.Request,
        view: rest_framework.views.APIView
    ) -> bool:
        return bool(request.user and request.user.is_superuser)


class IsAccountOwner(rest_framework.permissions.BasePermission):

    def has_permission(
        self,
        request: rest_framework.request.Request,
        view: rest_framework.views.APIView,
        serializer: rest_framework.serializers.Serializer = None,
    ) -> bool:
        if serializer is not None and serializer.instance:
            user_fetched = serializer.instance
        else:
            try:
                pk = view.kwargs[getattr(view, 'lookup_url_kwarg', 'pk')]
            except KeyError:
                return False

            user_fetched = view.queryset.filter(pk=pk).first()

        return bool(request.user and user_fetched == request.user)
