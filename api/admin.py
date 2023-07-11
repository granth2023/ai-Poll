from django.contrib import admin
from .models import Chatbox, Poll, Comment, Member

admin.site.register(Chatbox)
admin.site.register(Poll)
admin.site.register(Comment)
admin.site.register(Member)
