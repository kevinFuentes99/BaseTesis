from django.urls import path
from seguridad.views import Panel_principal_view
urlpatterns = [
path('', Panel_principal_view.as_view(), name="panel_principal" ),
]