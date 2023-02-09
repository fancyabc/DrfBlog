
from rest_framework import serializers
from article.models import Article, Category, Tag

from .user_info import UserDescSerializer
from .category import CategorySerializer


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
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

    class Meta:
        model = Article
        fields = '__all__'
