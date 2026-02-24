from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render, redirect
#api views
from rest_framework.viewsets import ModelViewSet
from .serializers import MeasurementMasterSerializer, PaymentModeSerializer, ProductMeasurementMapSerializer, VendorSerializer,ProductSerializer
# Masters 
from .models import PaymentMode, Product,Customer, MeasurementMaster, ProductMeasurementMap,Vendor
#forms
from .forms import PaymentModeForm, ProductForm,CustomerForm,MeasurementMasterForm

import os
from django.conf import settings
from django.http import HttpResponse


class VendorViewSet(ModelViewSet):
    queryset = Vendor.objects.all().order_by('id')
    serializer_class = VendorSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class MeasurementMasterVeiwSet(ModelViewSet):
    queryset = MeasurementMaster.objects.all()
    serializer_class = MeasurementMasterSerializer

class ProductMeasurementMapViewSet(ModelViewSet):
    queryset = ProductMeasurementMap.objects.all()
    serializer_class = ProductMeasurementMapSerializer

class PaymentModeViewSet(ModelViewSet):
    queryset = PaymentMode.objects.all()
    serializer_class = PaymentModeSerializer

class LoginAPIView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response(
                {"error": "Username and password are required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        user = authenticate(username=username, password=password)

        if user is None:
            return Response(
                {"error": "Invalid credentials"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        return Response(
            {
                "message": "Login successful",
                "user_id": user.id,
                "username": user.username
            },
            status=status.HTTP_200_OK
        )

### Masters 


def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list') # Replace with your success URL
    else:
        form = ProductForm()
    
    return render(request, 'create_product.html', {'form': form})

def product_list(request):
    products = Product.objects.all().order_by('-id') # Newest products first
    return render(request, 'product_list.html', {'products': products})

def customer_dashboard(request):
    customers = Customer.objects.all().order_by('-created_at')
    
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_dashboard')
    else:
        form = CustomerForm()

    return render(request, 'customers.html', {
        'customers': customers,
        'form': form
    })


def manage_product_measurements(request):
    products = Product.objects.all()
    measurements = MeasurementMaster.objects.all()
    mappings = ProductMeasurementMap.objects.select_related('product', 'measurement').all()

    if request.method == 'POST':
        prod_id = request.POST.get('product')
        meas_id = request.POST.get('measurement')
        order = request.POST.get('display_order', 0)
        required = request.POST.get('is_required') == 'on'

        ProductMeasurementMap.objects.create(
            product_id=prod_id,
            measurement_id=meas_id,
            display_order=order,
            is_required=required
        )
        return redirect('manage_measurements')

    return render(request, 'manage_measurements.html', {
        'products': products,
        'measurements': measurements,
        'mappings': mappings
    })


def measurement_master_list(request):
    masters = MeasurementMaster.objects.all()
    if request.method == 'POST':
        form = MeasurementMasterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('measurement_master')
    else:
        form = MeasurementMasterForm()
        
    return render(request, 'measurement_master.html', {
        'masters': masters,
        'form': form
    })

# def create_payment_mode(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         if name:
#             PaymentMode.objects.create(name=name)
#             return redirect('payment_mode_list')
#     return render(request, 'create_payment_mode.html')

def payment_mode_list(request):
    modes = PaymentMode.objects.all().order_by('-is_active', 'name')
    
    if request.method == 'POST':
        form = PaymentModeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payment_mode_list')
    else:
        form = PaymentModeForm()
        
    return render(request, 'payment_modes.html', {
        'modes': modes,
        'form': form
    })


def debug_media(request):
    media_root = settings.MEDIA_ROOT
    media_url = settings.MEDIA_URL
    exists = os.path.exists(media_root)
    
    # Try to find 'products/shirt.jpg'
    target_file = os.path.join(media_root, 'products', 'shirt.jpg')
    file_exists = os.path.isfile(target_file)
    
    debug_info = f"""
    <h3>Media Debugger</h3>
    <b>MEDIA_ROOT:</b> {media_root}<br>
    <b>MEDIA_URL:</b> {media_url}<br>
    <b>Folder Exists:</b> {exists}<br>
    <b>Target File (shirt.jpg) Exists:</b> {file_exists}<br>
    <br>
    <b>Full System Path to File:</b> {target_file}
    """
    return HttpResponse(debug_info)