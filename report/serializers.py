from report.models import Report
from rest_framework import serializers

class ReportCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Report
        fields=['id','owner','submited','created_at']

    def validate(self,attrs):
        # request=self.context.get('request')
        # contact=Contact.objects.filter(owner=request.user,phone_number=attrs.get('phone_number'))
        # if contact:
        #     message ="Contact already exists"
        #     raise serializers.ValidationError(message)
        # return{
        #     'phone_number':attrs.get('phone_number'),
        #     'name':attrs.get('name')
        # }
        return attrs
        
    def create(self):
        request=self.context.get('request')
        report=Report.objects.create_contact(
            owner=request.user
        )
        return report
    