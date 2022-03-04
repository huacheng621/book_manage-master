"""
@title: dwhouse-计划部数据接口工程
@author: mantuo (mantuo@efuton.com>)
@create_time: 2022/3/3
@des: datawarehouse服务层
"""
from  rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    """
    书籍序列化
    """
    class Meta:
        model = Book
        fields = "__all__"

