import django.conf
import django.conf.urls.static
import django.contrib
import django.urls

import users.urls

media_urlpatterns = django.conf.urls.static.static(
    django.conf.settings.MEDIA_URL,
    document_root=django.conf.settings.MEDIA_ROOT,
)

urlpatterns = [
    django.urls.path('api/users/', django.urls.include(users.urls)),
    django.urls.path('admin/', django.contrib.admin.site.urls),
] + media_urlpatterns
