
from rest_framework import serializers
from article.models import Article, Category, Tag, Avatar

from .user_info import UserDescSerializer
from .category import CategorySerializer
from .avatar import AvatarSerializer


class ArticleBaseSerializer(serializers.HyperlinkedModelSerializer):
    author = UserDescSerializer(read_only=True)
    # category 的嵌套序列化字段
    category = CategorySerializer(read_only=True)
    # category 的 id 字段，用于创建/更新 category 外键
    category_id = serializers.IntegerField(write_only=True, allow_null=True, required=False)

    tags = serializers.SlugRelatedField(
        queryset=Tag.objects.all(),
        many=True,
        required=False,
        slug_field='text'
    )
    avatar = AvatarSerializer(read_only=True)
    avatar_id = serializers.IntegerField(
        write_only=True,
        allow_null=True,
        required=False
    )

    # category_id 字段的验证器
    def validate_category_id(self, value):
        if not Category.objects.filter(id=value).exists() and value is not None:
            raise serializers.ValidationError("Category with id {} not exists.".format(value))
        return value

    def to_internal_value(self, data):
        tags_data = data.get('tags')

        if isinstance(tags_data, list):
            for text in tags_data:
                if not Tag.objects.filter(text=text).exists():
                    Tag.objects.create(text=text)

        return super().to_internal_value(data)

    def validate_avatar_id(self, value):
        """验证图片 id 是否存在,不存在则返回验证错误"""
        if not Avatar.objects.filter(id=value).exists() and value is not None:
            raise serializers.ValidationError("Avatar with id {} not exists.".format(value))

        return value


class ArticleSerializer(ArticleBaseSerializer):

    class Meta:
        model = Article
        fields = '__all__'
        extra_kwargs = {'body': {'write_only': True}}


class ArticleDetailSerializer(ArticleBaseSerializer):
    body_html = serializers.SerializerMethodField()
    toc_html = serializers.SerializerMethodField()

    def get_body_html(self, obj):
        return obj.get_md()[0]

    def get_toc_html(self, obj):
        return obj.get_md()[1]

    class Meta:
        model = Article
        fields = '__all__'
