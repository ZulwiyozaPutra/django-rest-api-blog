from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateUserListView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = {
    url(
        regex=r'^users/',
        view=CreateUserListView.as_view()
    ),
    url(
        regex=r'^auth/',
        view=include(
            arg='rest_framework.urls',
            namespace='rest_framework'
        )
    ),
    url(
        regex=r'^sign-in/',
        view=obtain_auth_token
    ),

}

urlpatterns = format_suffix_patterns(urlpatterns)
