from  .usermodel import User
from .projectmodel import Project
from .projectmembersmodel import ProjectMembers
from .listmodel import Lists
from .carddetailsmodel import CardDetails
from .carddetailsmodel import SubCard
from .commentmodel import Comment
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)