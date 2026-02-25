from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views 

router = DefaultRouter()
router.register(r'vendors', views.VendorViewSet, basename='vendor')
router.register(r'products', views.ProductViewSet, basename='product')
router.register(r'measurementmasters', views.MeasurementMasterVeiwSet, basename='measurementmaster')
router.register(r'productmeasurementmaps', views.ProductMeasurementMapViewSet, basename='productmeasurementmap')
router.register(r'paymentmodes', views.PaymentModeViewSet, basename='paymentmode')

urlpatterns = [
    # 1. HTML Dashboard/Form Routes
    path('product/new/', views.create_product, name='create_product'),
    path('productlist/', views.product_list, name='product_list'),
    path('customers/', views.customer_dashboard, name='customer_dashboard'),
    path('measurements/manage/', views.manage_product_measurements, name='manage_measurements'),
    path('measurements/master/', views.measurement_master_list, name='measurement_master'),
    path('payments/modes/', views.payment_mode_list, name='payment_mode_list'),
    path('test/', views.test_view, name='home'),

    # 2. API Routes (This will now be accessible at http://127.0.0.1:8000/api/products/)
    path('api/', include(router.urls)), 
]