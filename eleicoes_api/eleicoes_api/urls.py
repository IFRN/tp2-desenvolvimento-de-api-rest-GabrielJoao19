from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from urna.views import *


schema_view = get_schema_view(
    openapi.Info(
        title='Urna',
        default_version='v1',
    ),
    public=True,
)

router = DefaultRouter()
router.register(r'eleitores', EleitorViewSet)
router.register(r'candidatos', CandidatoViewSet)
router.register(r'aptidoes-eleitor', AptidaoEleitorViewSet)
router.register(r'registros', RegistroVotacaoViewSet)
router.register(r'votos', VotoViewSet)
router.register(r'eleicoes', EleicaoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('transporte_api/', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
]
