from rest_framework import serializers
from memopolis.models import Meme, Comment, Tag

class MemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meme
        fields = ['author', 'title', 'tags', 'image', 'date_posted', 'accepted']
        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['author', 'content', 'date_posted', 'belongs_to']
        
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name']