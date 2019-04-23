from django.urls import path


from kudgel.user.views import CreateUserView, UserDetailView, UserListView, CreateProjectUserView


urlpatterns = [
    path('user/join/', CreateUserView.as_view(), name='new_user'),
    path('user/<slug:slug>/', UserDetailView.as_view(), name='user-detail'),
    path('user/', UserListView.as_view(), name='user-list'),
    path('project/<slug:p_id>/staff/', CreateProjectUserView.as_view(), name='projectsstaff'),
]
