from rest_framework import serializers


def not_published(value):
    if value:
        raise serializers.ValidationError(f"Значение поля is_published при создании не может быть True")

