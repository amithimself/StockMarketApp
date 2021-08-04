from rest_framework import serializers

from .models import Stock


class StockSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stock
        fields = ['id', 'stock_name']


class StockDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ['id', 'stock_name', 'video_link', 'description']
