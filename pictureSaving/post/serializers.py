from rest_framework import serializers

from .models import *

class PostInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        # It is strongly recommended that you explicitly set all fields that should be serialized using the fields attribute
        fields = ['postId',
                  'userId', 
                  'caption',
                  'description',
                  'numberHeart',
                  'numberComment',
                  'dateCreated',
                  'dateModified']
        
class ImageInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        # It is strongly recommended that you explicitly set all fields that should be serialized using the fields attribute
        fields = ['imageId',
                  'postId',
                  'name', 
                  'path',
                  'dateCreated',
                  'dateModified']
        
class HeartInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserHeart
        # It is strongly recommended that you explicitly set all fields that should be serialized using the fields attribute
        fields = ['userId',
                  'postId',
                  'dateCreated']
class CommentInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserComment
        # It is strongly recommended that you explicitly set all fields that should be serialized using the fields attribute
        fields = ['userId',
                  'postId',
                  'content',
                  'dateCreated',
                  'dateModified']
        