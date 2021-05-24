from rest_framework import serializers
from catalog.models import Test



class TestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Test
        fields = ['uuid', 'timestamp']
