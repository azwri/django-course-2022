from rest_framework.serializers import ModelSerializer
from .models import Flower


class FlowerSerializer(ModelSerializer):
    class Meta:
        model = Flower
        fields = '__all__'
