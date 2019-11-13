# encoding: utf-8
"""
@version: 1.0
@author: 
@file: serializer
@time: 2019-10-29 23:06
"""
import re
from rest_framework import serializers
from rest_framework.serializers import Serializer


class LinkSerializer(Serializer):
    url = serializers.CharField(max_length=512, required=True)

    def validate_url(self, value):
        regx = re.compile(r'(?i)(http://|https://)?(\w+\.){1,3}(com(\.cn)?|cn|net|info|org|us|tk)\b')
        groups = regx.search(value)
        if groups and groups.group(0):
            return value
        raise serializers.ValidationError("请输入正确的网址")
