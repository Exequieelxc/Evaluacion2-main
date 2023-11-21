from django.urls import path 
from . import views
from .views import biblioteca_detail
from .views import registrar_proveedor, proveedor_lista, editar_proveedor, eliminar_proveedor

urlpatterns = [
    path('',views.biblioteca,name='biblioteca'),
    path('proveedor',views.proveedor,name='proveedor'),
    path('libros',views.libros,name='libros'),
    path('libros/crear',views.crear,name='crear'),
    path('libros/editar',views.editar,name='editar'),
    path('libros/eliminar/<int:id>',views.eliminar,name='eliminar'),
    path('libros/editar/<int:id>',views.editar,name='editar'),
    path('proveedores/', proveedor_lista, name='lista_proveedores'),
    path('proveedores/registrar/', registrar_proveedor, name='registrar_proveedor'),
    path('editar_proveedor/<int:id>/', views.editar_proveedor, name='editar_proveedor'),
    path('eliminar_proveedor/<int:id>/', eliminar_proveedor, name='eliminar_proveedor'),
    path('biblioteca/', biblioteca_detail, name='biblioteca_detail')
]