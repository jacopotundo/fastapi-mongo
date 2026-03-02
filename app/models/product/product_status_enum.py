from enum import Enum


class ProductStatus(str, Enum):
    """
    Stato del prodotto nel magazzino.
    
    Equivalente a enum Java in Spring Boot.
    Usato sia negli schemi che nel modello.
    """
    STOCK = "stock"
    OUT_OF_STOCK = "out_of_stock"