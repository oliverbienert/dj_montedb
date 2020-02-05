from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
import accounts.urls
import montedb.urls
from . import views

# Personalized admin site settings like title and header
admin.site.site_title = "Montehelper Site Admin"
admin.site.site_header = "Montehelper Administration"

urlpatterns = [
    path("", views.HomePage.as_view(), name="home"),
    path("montedb/", include(montedb.urls)),
    path("grappelli/", include('grappelli.urls')),
    path("admin/", admin.site.urls),
    path("rosetta", include('rosetta.urls')),
    path("", include(accounts.urls)),
]

# User-uploaded files like profile pics need to be served in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Include django debug toolbar if DEBUG is on
if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [path("__debug__/", include(debug_toolbar.urls))]
