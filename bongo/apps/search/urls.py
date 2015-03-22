from django.conf.urls import url
from haystack.views import SearchView
from haystack.forms import ModelSearchForm

urlpatterns = [
    url(r'^search/', SearchView(
        form_class=ModelSearchForm
    ), name='haystack_search'),
]