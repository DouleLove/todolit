import rest_framework.serializers

import tasks.models


class TaskSerializer(rest_framework.serializers.ModelSerializer):

    class Meta:
        model = tasks.models.Task
        fields = '__all__'
