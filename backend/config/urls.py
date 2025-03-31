import django.conf
import django.conf.urls.static
import django.urls

import rest_framework.routers

import tasks.views
import users.views

router = rest_framework.routers.DefaultRouter()
router.register(
    prefix='users',
    viewset=users.views.UserViewSet,
    basename='users',
)
router.register(
    prefix='users/(?P<uid>[0-9]+)/tasks',
    viewset=tasks.views.TaskViewSet,
    basename='tasks',
)

media_urlpatterns = django.conf.urls.static.static(
    django.conf.settings.MEDIA_URL,
    document_root=django.conf.settings.MEDIA_ROOT,
)

urlpatterns = [
    django.urls.path('api/', django.urls.include(router.urls)),
] + media_urlpatterns
