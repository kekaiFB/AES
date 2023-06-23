from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('elements.urls')),
    path('chaining/', include('smart_selects.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    

    import debug_toolbar
    urlpatterns = [ 
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 
# from .views import ErrorHandler

# for code in (400, 403, 404, 500):
#     vars()['handler{}'.format(code)] = ErrorHandler.as_view(error_code=code)

