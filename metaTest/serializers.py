from metaTest.models import MetaTest
from rest_framework import serializers

class MetaTestCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model=MetaTest
        fields=['name']

    def validate(self,attrs):
        contact=MetaTest.objects.filter(name=attrs.get('name'))
        if contact:
            message ="Test already exists"
            raise serializers.ValidationError(message)
        return{
            'name':attrs.get('name')
        }
        
    def create(self,validated_data):
        contact=MetaTest.objects.create_meta_test(
            name=validated_data.get('name')
        )
        return contact
    