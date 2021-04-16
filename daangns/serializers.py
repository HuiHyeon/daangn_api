from rest_framework import serializers
from .models import *

from rest_auth.registration.serializers import RegisterSerializer


class CustomRegisterSerializer(RegisterSerializer):

    email = serializers.EmailField(required=True)
    password1 = serializers.CharField(write_only=True)
    name = serializers.CharField(required=True)
    address = serializers.CharField(required=True)
    manner = serializers.IntegerField(required=True)

    def get_cleaned_data(self):
        super(CustomRegisterSerializer, self).get_cleaned_data()

        return {
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'name': self.validated_data.get('name', ''),
            'address': self.validated_data.get('address', ''),
            'manner': self.validated_data.get('manner', ''),
        }


class CustomUserDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'name', 'address', 'manner')
        read_only_fields = ('email',)


class CommentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Comment
        fields = ('post', 'id', 'author', 'text', 'created_date')


class PostSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'author', 'image', 'title', 'category',
                  'price', 'content', 'created_at', 'updated_at')
