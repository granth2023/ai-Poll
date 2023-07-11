from .models import Poll, Comment, Chatbox, Member
from .serializers import PollSerializer, CommentSerializer, ChatboxSerializer, MemberSerializer
from rest_framework import viewsets, generics
from rest_framework.response import Response

class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
    def perform_create(self, serializer):
        serializer.save()  
    
class ChatboxViewSet(viewsets.ModelViewSet):
    queryset = Chatbox.objects.all()
    serializer_class = ChatboxSerializer
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        comments = instance.comments.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    
class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    
class MemberCreate(generics.CreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    
    def perform_create(self, serializer):
        serializer.save()
    


