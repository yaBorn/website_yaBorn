# 序列化器
from rest_framework import serializers
from media.models import Photo


# 图片序列化器
# 图片在文章上传前先单独上传
class PhotoSerializer(serializers.ModelSerializer):
    # DRF 对图片的处理进行了封装 因此和普通Json接口一样写序列化即可
    url = serializers.HyperlinkedIdentityField(view_name='photo-detail')

    class Meta:
        model = Photo
        fields = '__all__'


# 图片上传完成，将其 id、url 等信息返回到前端
# 前端将图片的信息以嵌套结构表示到文章接口中
# 在适当的时候将其链接到文章数据中
# 见 articleBaseSerializer 文章基础序列化器
