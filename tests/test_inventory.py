import pytest
from inventory import fetch_inventory_levels, calculate_optimal_purchase_quantities

def test_fetch_inventory_levels():
    fulfillment_center_id = "fc1"
    skus = ["sku1", "sku2", "sku3"]
    inventory_levels = fetch_inventory_levels(fulfillment_center_id, skus)
    assert inventory_levels == {"sku1": 100, "sku2": 50, "sku3": 200}

def test_fetch_inventory_levels_empty_skus():
    fulfillment_center_id = "fc1"
    skus = []
    inventory_levels = fetch_inventory_levels(fulfillment_center_id, skus)
    assert inventory_levels == {}

def test_calculate_optimal_purchase_quantities():
    inventory_levels = {"sku1": 100, "sku2": 50, "sku3": 200}
    sales_forecasts = {"sku1": 150, "sku2": 100, "sku3": 250}
    optimal_purchase_quantities = calculate_optimal_purchase_quantities(inventory_levels, sales_forecasts)
    assert optimal_purchase_quantities == {"sku1": 50, "sku2": 50, "sku3": 50}

def test_calculate_optimal_purchase_quantities_zero_sales_forecast():
    inventory_levels = {"sku1": 100, "sku2": 50, "sku3": 200}
    sales_forecasts = {"sku1": 0, "sku2": 0, "sku3": 0}
    optimal_purchase_quantities = calculate_optimal_purchase_quantities(inventory_levels, sales_forecasts)
    assert optimal_purchase_quantities == {"sku1": 0, "sku2": 0, "sku3": 0}
