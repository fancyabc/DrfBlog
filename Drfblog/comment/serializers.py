from rest_framework import serializers

from comment.models import Comment
from article.serializers.user_info import UserDescSerializer


class CommentSonSerializer(serializers.ModelSerializer):
    """子评论序列化器"""
    url = serializers.HyperlinkedIdentityField(view_name='comment-detail')
    author = UserDescSerializer(read_only=True)

    class Meta:
        model = Comment
        exclude = [
            'comment_p',
            'article'
        ]   # 不需要的字段


class CommentSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='comment-detail')
    author = UserDescSerializer(read_only=True)

    article = serializers.HyperlinkedRelatedField(view_name='article-detail', read_only=True)
    article_id = serializers.IntegerField(write_only=True, allow_null=False, required=True)

    comment_p = CommentSonSerializer(read_only=True)
    comment_p_id = serializers.IntegerField(write_only=True, allow_null=True, required=False)

    def update(self, instance, validated_data):
        validated_data.pop('comment_p_id', None)
        return super().update(instance, validated_data)

    class Meta:
        model = Comment
        fields = '__all__'
        extra_kwargs = {'created': {'read_only': True}}