from django.contrib import admin
from django.urls import path, include
# import accounts.views import login_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('news.urls'))
    # path('login', login_view)
]
