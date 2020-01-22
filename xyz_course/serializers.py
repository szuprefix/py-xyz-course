# -*- coding:utf-8 -*- 
# author = 'denishuang'
from __future__ import unicode_literals

from xyz_restful.mixins import IDAndStrFieldSerializerMixin
from django_szuprefix.utils.datautils import auto_code
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from . import models


class CourseSerializer(IDAndStrFieldSerializerMixin, serializers.ModelSerializer):
    category_name = serializers.CharField(source="category", read_only=True)
    class Meta:
        model = models.Course

    def validate_code(self, value):
        if value is None:
            value = auto_code(self.validated_data['name'])
        return value


class CourseNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = ('name',)


class CategorySerializer(IDAndStrFieldSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = models.Category


class ChapterSerializer(IDAndStrFieldSerializerMixin, serializers.ModelSerializer):
    course_name = serializers.CharField(source="course", read_only=True)
    class Meta:
        model = models.Chapter
        exclude = ('order_num',)