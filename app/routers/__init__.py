from .health_check import health_router
from .api.v1.product_router import router as product_router

__all__ = ["health_router", "product_router"]