from django.contrib import admin
from .models import Chatbox, Poll, Comment, User

admin.site.register(Chatbox)
admin.site.register(Poll)
admin.site.register(Comment)
admin.site.register(User)
