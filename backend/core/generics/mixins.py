import typing

import rest_framework.request
import rest_framework.response
import rest_framework.views


class URLKwargsMixin:
    """
    Mixin which connects url parameter's name with model's primary key name.

    Attributes
    ----------
    pk_url_kwarg_names: str
        name of the url parameter which represents model's pk.

    .. note:
        if you don't want object lookup to be performing
        with the "pk" name, then you can specify the "lookup_field"
        attribute inside your class.
    """

    # methods which are used in rest_framework model mixins
    _MIXIN_METHODS = (
        'retrieve',
        'create',
        'partial_update',
        'destroy',
    )

    # name of url parameter which should be used
    # to lookup for a model's primary key
    pk_url_kwarg_name = None

    def __getattribute__(self, item: str) -> typing.Any:
        # getting class of an inheritor and its mro
        mro = getattr(super().__getattribute__('__class__'), '__mro__')

        # searching this class to access to _MIXIN_METHODS attribute
        mixin_methods = None
        for cls_ in mro:
            mixin_methods = getattr(cls_, '_MIXIN_METHODS', None)
            if mixin_methods:
                break

        attr = super().__getattribute__(item)
        # wrap attr if it's callable which was produced
        # by one of the rest_framework model mixins,
        # the wrapper updates self.kwargs attribute
        # to fake that self.lookup_field parameter
        # was passed through the url
        return self._wrap_mixin_method(attr) if item in mixin_methods else attr

    def _wrap_mixin_method(self, fn: typing.Callable) -> typing.Callable:

        def __wrapper__(request: rest_framework.request.Request,
                        *args: typing.Any,
                        **kwargs: typing.Any
                        ) -> rest_framework.response.Response:
            assert self.pk_url_kwarg_name is not None, (
                'pk_url_kwarg_name attribute must be set to '
                'be able to extract pk from the url parameters'
            )

            uid = request.query_params.get(self.pk_url_kwarg_name, None)
            # lookup_field is used by rest_framework for
            # creating a connection between URLConf parameters
            # and model's primary key, we artificially adding
            # a key with this name to make
            # rest_framework.generics.GenericAPIView.get_object()
            # not raise if this parameter was not actually passed
            # and to get it returning the object that we need
            self.kwargs.update({self.lookup_field: uid})

            return fn(self, request, *args, **kwargs)

        return __wrapper__
