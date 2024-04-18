
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('ShopDBA/', include('introduce.urls')),
    path('ShopDBA/', include('home.urls')),
    path('admin/', admin.site.urls),
    path('ShopDBA/', include('signin.urls'))
]

#path('home/', include('home.urls')),