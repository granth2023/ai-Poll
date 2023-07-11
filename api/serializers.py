from rest_framework import serializers
from .models import Poll, Comment, Chatbox, Member


class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = '__all__'
        
class CommentSerializer(serializers.ModelSerializer):
    creator = serializers.PrimaryKeyRelatedField(queryset=Member.objects.all(), write_only=True)
    creator_name = serializers.CharField(source='creator.username', read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'creator', 'creator_name', 'text', 'created_at']
        
class ChatboxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chatbox
        fields = '__all__'
        
class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'