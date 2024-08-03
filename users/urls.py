from django.urls import path
from . import views
import logging

logger = logging.getLogger(__name__)


urlpatterns = [
    path('', views.index, name='index'),
    # path('sign', views.sign, name='sign'),
    # path('login', views.log, name='login'),
    
]



logger.debug("Loaded URL patterns for app: %s", __name__)
