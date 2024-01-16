from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from drf_yasg.renderers import SwaggerUIRenderer, OpenAPIRenderer

schema_view = get_schema_view(
    openapi.Info(
        title="Django API",
        default_version='v1',
        description="Demo API description",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="sakshi@email.com"),
        license=openapi.License(name="Awesome License"),
        servers=[
            {"url": "http://localhost:8080", "description": "Local Server"},
            {"url": "https://api.example.com", "description": "Production Server"},
        ],
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('master/', include('api.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('swagger/local/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui-local'),
]
