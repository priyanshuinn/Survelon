from django.urls import path
from . import views
from .views import POSTSpeed
urlpatterns  = [
    path('post/<int:my_id>', views.post, name = 'post'),
    path('describe', views.overview, name = 'overview'),
    path('Rvedio',views.display,name='real_video'),
    path('stream/',POSTSpeed.as_view(),name='stream'),
    path('show/',views.show,name='show'),
    path('maskload/',views.mask,name='mask'),
    path('mask/',views.load,name='mask_page'),
]