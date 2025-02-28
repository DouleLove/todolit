import django.urls

import users.views

urlpatterns = [
    django.urls.path('<int:uid>/', users.views.UserAPIView.as_view()),
]
