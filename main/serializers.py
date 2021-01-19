from rest_framework import serializers


class MySerializer(serializers.Serializer):
    username = serializers.CharField(max_length=20)
    spent_money = serializers.IntegerField()
    gems = serializers.CharField()