import django.urls

import users.views

urlpatterns = [django.urls.path('', users.views.UserAPIView.as_view())]
