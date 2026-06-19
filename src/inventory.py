import json
from dataclasses import dataclass
from typing import List, Dict

@dataclass
class InventoryLevel:
    sku: str
    quantity: int

@dataclass
class ShippingInfo:
    sku: str
    shipping_time: int

def fetch_inventory_levels(api_url: str, skus: List[str]) -> List[InventoryLevel]:
    # Simulate API call with in-memory data
    inventory_data = {
        "sku1": 100,
        "sku2": 50,
        "sku3": 200
    }
    return [InventoryLevel(sku, inventory_data.get(sku, 0)) for sku in skus]

def calculate_optimal_purchase_quantities(inventory_levels: List[InventoryLevel], sales_forecasts: Dict[str, int]) -> Dict[str, int]:
    optimal_quantities = {}
    for level in inventory_levels:
        forecast = sales_forecasts.get(level.sku, 0)
        optimal_quantities[level.sku] = max(0, forecast - level.quantity)
    return optimal_quantities

def fetch_shipping_info(api_url: str, skus: List[str]) -> List[ShippingInfo]:
    # Simulate API call with in-memory data
    shipping_data = {
        "sku1": 3,
        "sku2": 5,
        "sku3": 2
    }
    return [ShippingInfo(sku, shipping_data.get(sku, 0)) for sku in skus]
