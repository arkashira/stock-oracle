import json
from dataclasses import dataclass
from typing import List, Dict

@dataclass
class SKU:
    id: str
    quantity: int

@dataclass
class FulfillmentCenter:
    id: str
    inventory: List[SKU]

def fetch_inventory_levels(fulfillment_center_id: str, skus: List[str]) -> Dict[str, int]:
    # Simulate fetching inventory levels from a fulfillment center API
    # In a real implementation, this would be replaced with an actual API call
    inventory_levels = {
        "sku1": 100,
        "sku2": 50,
        "sku3": 200
    }
    return {sku: inventory_levels.get(sku, 0) for sku in skus}

def calculate_optimal_purchase_quantities(inventory_levels: Dict[str, int], sales_forecasts: Dict[str, int]) -> Dict[str, int]:
    optimal_purchase_quantities = {}
    for sku, inventory_level in inventory_levels.items():
        sales_forecast = sales_forecasts.get(sku, 0)
        optimal_purchase_quantity = max(0, sales_forecast - inventory_level)
        optimal_purchase_quantities[sku] = optimal_purchase_quantity
    return optimal_purchase_quantities
