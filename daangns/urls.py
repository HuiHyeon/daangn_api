from django.conf.urls import include, url
from rest_framework import routers
from daangns import views

from django.urls import re_path
from rest_framework_nested import routers as nested_routers

from django.urls import path


post_router = routers.DefaultRouter()
post_router.register(r'posts', views.PostViewSet, basename="post")
comment_router = nested_routers.NestedSimpleRouter(
    post_router, r'posts', lookup="post")
comment_router.register(r'comments', views.CommentViewSet, basename="comment")

urlpatterns = [
    re_path('^', include(post_router.urls)),
    re_path('^', include(comment_router.urls)),
    url('^register', views.CustomRegisterView.as_view()),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]
