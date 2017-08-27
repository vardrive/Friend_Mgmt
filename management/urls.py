from django.conf.urls import url
from django.contrib import admin

from django.conf.urls import url, include
from rest_framework import routers
from management.friends import views
from friendship.views import view_friends, all_users, friendship_add_friend, friendship_accept
from management.friends.views import FriendViewSet, FollowersViewSet, FriendshipRequestViewSet

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
#router.register(r'groups', views.GroupViewSet)
router.register(r'friends/(?P<email>[\w.@+-]+)', views.FriendViewSet, base_name='friends')
router.register(r'followers/(?P<email>[\w.@+-]+)', views.FollowersViewSet, base_name='followers')
router.register(r'friendrequests', views.FriendshipRequestViewSet, base_name='friendrequests')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^friendship/', include('friendship.urls')),
    # url(
    #     regex=r'^friends/(?P<email>[\w.@+-]+)/$',
    #     view=FriendViewSet.list_friends,
    #     name='friends-list',
    # ),

]





