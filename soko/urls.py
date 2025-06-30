
from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static

from core.views import homepage

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', homepage, name='home'),  # 👈 homepage at /
    path('products/', include('products.urls')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('orders/', include('orders.urls')),
    path('payments/', include(('payments.urls', 'payments'), namespace='payments')),


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

