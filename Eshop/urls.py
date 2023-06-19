from django.contrib import admin
from django.urls import path  , include
from django.conf.urls.static import static
from . import settings #settings에 접근하기 위해 import시켜줌.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include('store.urls')) #store디렉토리 안에 있는 urls.을 포함시킨다.(include)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#static() 함수는 장고 내장함수 이다.
#미디어 파일 제공을 위한 URL패턴 설정 역할 즉 미디어 파일(정적 파일)을 서빙하기 위한 URL 패턴을 설정하는 코드이다.
