from rest_framework import serializers
from .models import CompanyDetails, PaymentMode, ProductMeasurementMap
from .models import Product,MeasurementMaster

# class VendorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Vendor
#         fields = ['id', 'name']

class CompanyDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyDetails
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    # This will return the full URL (http://...)
    image = serializers.ImageField(use_url=True, required=False)

    class Meta:
        model = Product
        fields = ['id', 'name', 'gender', 'price', 'image', 'is_active']        

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
