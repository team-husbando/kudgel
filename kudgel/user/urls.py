from django.urls import path


from kudgel.user.views import CreateUserView, UserDetailView, UserListView


urlpatterns = [
    path('user/join/', CreateUserView.as_view(), name='new_user'),
    path('user/<slug:slug>/', UserDetailView.as_view(), name='user-detail'),
    path('user/', UserListView.as_view(), name='user-list')
]
