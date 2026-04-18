from rest_framework import serializers
from .models import CompanyDetails, PaymentMode, ProductMeasurementMap
from .models import Product,MeasurementMaster


class CompanyDetailsSerializer(serializers.ModelSerializer):
    logo = serializers.SerializerMethodField()

    class Meta:
        model = CompanyDetails
        fields = '__all__'

    def get_logo(self, obj):
        if obj.logo:
            request = self.context.get('request')
            return request.build_absolute_uri(obj.logo.url)
        return "https://tailorweb-1.onrender.com/media/company_logos/logo.png"
    
class ProductSerializer(serializers.ModelSerializer):
    # This will return the full URL (http://...)
    image = serializers.ImageField(use_url=True, required=False)

    class Meta:
        model = Product
        fields = ['product_id', 'name', 'gender', 'price', 'image', 'is_active']        

class MeasurementMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeasurementMaster
        fields = '__all__'

class ProductMeasurementMapSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductMeasurementMap
        fields = '__all__'        

class PaymentModeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMode
        fields = '__all__'
