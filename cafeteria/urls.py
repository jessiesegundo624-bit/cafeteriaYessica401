from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register(r"usuarios", UsuariosViewSet)
router.register(r"pedido", PedidoViewSet)
router.register(r"productos", ProductoViewSet)
router.register(r"pago", PagoViewSet)
router.register(r"roles", RolesViewSet)
router.register(r"detallepedido", DetallePedidoViewSet)
router.register(r"categoria", CategoriaViewSet)
router.register(r"cafeteria", CafeteriaViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
]