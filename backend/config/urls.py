import django.contrib
import django.urls

import users.urls

urlpatterns = [
    django.urls.path('api/user/', django.urls.include(users.urls)),
    django.urls.path('admin/', django.contrib.admin.site.urls),
]
