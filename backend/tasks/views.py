import rest_framework.viewsets

import tasks.serializers


class TaskViewSet(rest_framework.viewsets.ModelViewSet):
    serializer_class = tasks.serializers.TaskSerializer

    def get_queryset(self) -> ...:
        ...
