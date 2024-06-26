from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.decorators.cache import cache_page

from client.apps import ClientConfig
from client.views import ClientListView, ClientCreateView, ClientUpdateView, ClientDetailView, ClientDeleteView

app_name = ClientConfig.name

urlpatterns = [
    path('', cache_page(60)(ClientListView.as_view()), name='client_list'),
    path('create/', ClientCreateView.as_view(), name='create'),
    path('edit/<int:pk>', ClientUpdateView.as_view(), name='edit'),
    path('view/<int:pk>', ClientDetailView.as_view(), name='view_client'),
    path('delete/<int:pk>', ClientDeleteView.as_view(), name='delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
