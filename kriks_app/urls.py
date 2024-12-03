from django.urls import path
from kriks_app import views 

urlpatterns = [
    path("proveedor",views.inicio_vistaproveedor,name="proveedor"),
    path("registrarProveedor/",views.registrarProveedor,name="registrarProveedor"),
    path("seleccionarProveedor/<id_proveedor>",views.seleccionarProveedor,name="seleccionarProveedor"),
    path("editarProveedor/",views.editarProveedor,name="editarProveedor"),
    path("borrarProveedor/<id_proveedor>",views.borrarProveedor,name=" borrarProveedor"),
]