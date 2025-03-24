import django.urls

import rest_framework.routers

import users.views

router = rest_framework.routers.DefaultRouter()
router.register('', users.views.UserViewSet)

urlpatterns = [
    django.urls.path('', django.urls.include(router.urls)),
]
