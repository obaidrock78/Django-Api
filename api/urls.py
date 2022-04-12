
from django.urls import path, include

from api.views import ListApi, ListPerson

app_name = "api"
urlpatterns = [
    path("newapi/", ListApi.as_view(), name="api"),
    path("filter/", ListPerson.as_view(), name="list"),

]
