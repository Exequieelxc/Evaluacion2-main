from django.urls import path 
from . import views
from .views import biblioteca_detail

urlpatterns = [
    path('',views.biblioteca,name='biblioteca'),
    path('nosotros',views.nosotros,name='nosotros'),
    path('libros',views.libros,name='libros'),
    path('libros/crear',views.crear,name='crear'),
    path('libros/editar',views.editar,name='editar'),
    path('libros/eliminar/<int:id>',views.eliminar,name='eliminar'),
    path('libros/editar/<int:id>',views.editar,name='editar'),
    path('biblioteca/', biblioteca_detail, name='biblioteca_detail')
]