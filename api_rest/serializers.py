from rest_framework import serializers

from dashboard.models import Todo

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'