from django.urls import path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions


schema_view = get_schema_view(
    openapi.Info(
        title="Bond Service API",
        default_version='v1',
        description="For creating new user use http://127.0.0.1:8080/api/auth/users/\n"
                    "To get Token use http://127.0.0.1:8080/auth/token/login/\n"
                    "To get JWT Token use http://127.0.0.1:8080/api/token/\n"
                    "For example you can use Postman to GET, POST, PATCH, UPDATE, DELETE BONDS\n"
                    "First, you need to get a token from the endpoints described above.\n"
                    "Then by url http://127.0.0.1:8080/api/bonds/ make all your necessary requests.\n"
                    "Also, to analyze investments, you can use http://127.0.0.1:8080/api/bonds/analyze/",
        contact=openapi.Contact(email="s.sherimkulov@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]