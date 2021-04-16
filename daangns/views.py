from rest_framework import viewsets
from .serializers import *
from .models import *
from rest_framework.filters import SearchFilter

from rest_auth.registration.views import RegisterView
from rest_framework import permissions
from daangns.permissions import IsOwnerOrReadOnly


class CustomRegisterView(RegisterView):
    queryset = User.objects.all()


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    filter_backends = [SearchFilter]
    search_fields = ['category']


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)
