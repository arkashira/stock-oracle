import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.inventory import fetch_inventory_levels, calculate_optimal_purchase_quantities, fetch_shipping_info, InventoryLevel
import pytest

def test_fetch_inventory_levels():
    api_url = "https://example.com/api"
    skus = ["sku1", "sku2", "sku3"]
    inventory_levels = fetch_inventory_levels(api_url, skus)
    assert len(inventory_levels) == 3
    assert inventory_levels[0].sku == "sku1"
    assert inventory_levels[0].quantity == 100

def test_fetch_inventory_levels_empty_skus():
    api_url = "https://example.com/api"
    skus = []
    inventory_levels = fetch_inventory_levels(api_url, skus)
    assert len(inventory_levels) == 0

def test_calculate_optimal_purchase_quantities():
    inventory_levels = [InventoryLevel("sku1", 100), InventoryLevel("sku2", 50)]
    sales_forecasts = {"sku1": 150, "sku2": 75}
    optimal_quantities = calculate_optimal_purchase_quantities(inventory_levels, sales_forecasts)
    assert optimal_quantities["sku1"] == 50
    assert optimal_quantities["sku2"] == 25

def test_calculate_optimal_purchase_quantities_zero_forecast():
    inventory_levels = [InventoryLevel("sku1", 100), InventoryLevel("sku2", 50)]
    sales_forecasts = {"sku1": 0, "sku2": 0}
    optimal_quantities = calculate_optimal_purchase_quantities(inventory_levels, sales_forecasts)
    assert optimal_quantities["sku1"] == 0
    assert optimal_quantities["sku2"] == 0

def test_fetch_shipping_info():
    api_url = "https://example.com/api"
    skus = ["sku1", "sku2", "sku3"]
    shipping_info = fetch_shipping_info(api_url, skus)
    assert len(shipping_info) == 3
    assert shipping_info[0].sku == "sku1"
    assert shipping_info[0].shipping_time == 3
