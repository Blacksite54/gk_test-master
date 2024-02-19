from django.urls import path
from some_app.views import IndexView

app_name = 'some_app'

urlpatterns = [
    path(r'', IndexView.as_view(), name='index'),
    path(r'^(.*)/$', IndexView.as_view(), name='index'),
]
