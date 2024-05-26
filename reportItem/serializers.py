from reportItem.models import ReportItem
# from contacts.models import Contact
from rest_framework import serializers

class ReportItemCreationSerializer(serializers.ModelSerializer):

    class Meta:
        model=ReportItem
        fields=['id','report','value','test_name',]

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
    
    def create(self,value,test_name,report):
        reportItem=ReportItem.objects.create_report_item(
            report=report,
            value=value,
            test_name=test_name
        )
        return reportItem
    