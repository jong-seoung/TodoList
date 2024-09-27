from rest_framework import serializers

from todo.models import Todo, Alarm


class TodoSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    nickname = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Todo
        fields = ["id", "author", "nickname", "content", "deadline_data", "is_finished", "created_at", "updated_at"]

    def get_nickname(self, obj):
        return obj.author.profile.nickname

    def get_optimized_queryset():
        return Todo.objects.all()
    

class AlarmSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Alarm
        fields = ['sender', 'content', 'created_at', 'is_read']
