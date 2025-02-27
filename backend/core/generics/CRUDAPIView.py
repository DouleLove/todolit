__all__ = ('CRUDAPIView',)

import rest_framework.generics


class CRUDAPIView(rest_framework.generics.RetrieveUpdateDestroyAPIView,
                  rest_framework.generics.CreateAPIView):
    pass
