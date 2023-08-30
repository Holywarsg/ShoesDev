from rest_framework import serializers
from .models import Shoes, Color, ShoeSize, Brand, Sex, Season

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'

class ShoeSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoeSize
        fields = '__all__'

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class SexSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sex
        fields = '__all__'

class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = '__all__'

class ShoesSerializer(serializers.ModelSerializer):
    color = ColorSerializer()
    shoe_size = ShoeSizeSerializer()
    brand = BrandSerializer()
    sex = SexSerializer()
    season = SeasonSerializer()

    class Meta:
        model = Shoes
        fields = '__all__'
