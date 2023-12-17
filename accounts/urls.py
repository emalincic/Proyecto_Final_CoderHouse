from django.contrib.auth.views import LogoutView
from django.urls import path
from accounts.views import editar_avatar_request, editar_request, login_request, register_request

urlpatterns = [
    path('register/', register_request, name="Registro"),
    path('editar/', editar_request, name="Editar"),
    path('avatar/', editar_avatar_request, name="Avatar"),
    path('login/', login_request, name="Login"),
    path('logout/', LogoutView.as_view(template_name="accounts/logout.html"), name="Logout"),
]
