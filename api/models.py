from django.db import models
from django.contrib.auth.models import User, AbstractUser

class Chatbox(models.Model):
    chatbox_id = models.CharField(max_length=200)
    
    def __str__(self):
        return self.chatbox_id

class Poll(models.Model):
    VOTING_STATUS_CHOICES = [
        ('open', 'open'),
        ('closed', 'closed'),
    ]

    class Option(models.TextChoices):
        OPTION_A = 'a', 'a'
        OPTION_B = 'b', 'b'

    title = models.CharField(max_length=200)
    option_a_label = models.CharField(max_length=200)
    option_a_votes = models.PositiveIntegerField(default=0)
    option_b_label = models.CharField(max_length=200)
    option_b_votes = models.PositiveIntegerField(default=0)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    chatbox = models.OneToOneField(Chatbox, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    winner = models.CharField(max_length=1, choices=Option.choices, null=True, blank=True)
    voting_status = models.CharField(max_length=10, choices=VOTING_STATUS_CHOICES, default='open')
    duration_minutes = models.IntegerField()
    
    def __str__(self):
        return self.title
        
        
class Comment(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    chatbox = models.ForeignKey(Chatbox, on_delete=models.CASCADE, related_name='comments')
    
    def __str__(self):
        return f"{self.creator} - {self.text}"

class User(AbstractUser):
    verify_password = models.CharField(max_length=128)
    wallet_address = models.CharField(max_length=255) 

    # Add a unique related_name for groups field
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True,
    )

    # Add a unique related_name for user_permissions field
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',
        blank=True,
    )

    def clean(self):
        super().clean()
        if self.password != self.verify_password:
            raise ValidationError("Password and Verify Password fields must match.")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username