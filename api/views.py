from django.shortcuts import render
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

# Importaciones de tus modelos y serializers
from tecnicas.models import (
    Tecnica, Carrera, MomentoClase, Pensamiento, 
    TipoAgrupacion, Dificultad, Duracion
)
from .serializers import (
    TecnicaSerializer, CarreraSerializer, MomentoClaseSerializer, 
    PensamientoSerializer, TipoAgrupacionSerializer, 
    DificultadSerializer, DuracionSerializer
)

# --- VISTAS DE CATÁLOGOS (Sin Paginación) ---
# Al poner pagination_class = None, el frontend recibirá la lista completa [{}, {}, ...]
# ideal para llenar los <select> o dropdowns.

class CarreraListAPIView(generics.ListAPIView):
    queryset = Carrera.objects.all()
    serializer_class = CarreraSerializer
    pagination_class = None  # <--- ¡ESTA ES LA CLAVE!

class MomentoClaseListAPIView(generics.ListAPIView):
    queryset = MomentoClase.objects.order_by('orden')
    serializer_class = MomentoClaseSerializer
    pagination_class = None  # <--- Sin paginación

class PensamientoListAPIView(generics.ListAPIView):
    queryset = Pensamiento.objects.all()
    serializer_class = PensamientoSerializer
    pagination_class = None  # <--- Sin paginación

class TipoAgrupacionListAPIView(generics.ListAPIView):
    queryset = TipoAgrupacion.objects.all()
    serializer_class = TipoAgrupacionSerializer
    pagination_class = None  # <--- Sin paginación

class DificultadListAPIView(generics.ListAPIView):
    queryset = Dificultad.objects.order_by('orden')
    serializer_class = DificultadSerializer
    pagination_class = None  # <--- Sin paginación

class DuracionListAPIView(generics.ListAPIView):
    queryset = Duracion.objects.order_by('orden')
    serializer_class = DuracionSerializer
    pagination_class = None  # <--- Sin paginación


# --- VISTA PRINCIPAL DE RESULTADOS (Con Paginación) ---
# Esta vista NO lleva pagination_class = None.
# Usará el valor por defecto de settings.py (PAGE_SIZE = 6).

class TecnicaListAPIView(generics.ListAPIView):
    queryset = Tecnica.objects.all()
    serializer_class = TecnicaSerializer
    
    # Filtros y Búsqueda
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = {
        'carreras__nombre': ['exact', 'in'],
        'momentos__nombre': ['exact', 'in'],
        'duraciones__nombre': ['exact', 'in'],
        'agrupaciones__nombre': ['exact', 'in'],
        'pensamientos__nombre': ['exact', 'in'],
        'dificultades__nombre': ['exact', 'in'],
    }
    search_fields = ['nombre']