import pytest
from stock_oracle import StockOracle, StockItem

def test_add_stock_item():
    oracle = StockOracle()
    oracle.add_stock_item("sku1", 10, 5)
    assert len(oracle.get_dashboard_data()) == 1
    assert oracle.get_dashboard_data()[0]["sku"] == "sku1"
    assert oracle.get_dashboard_data()[0]["stock_level"] == 10
    assert oracle.get_dashboard_data()[0]["reorder_point"] == 5

def test_load_data():
    oracle = StockOracle()
    data = [{"sku": "sku1", "stock_level": 10, "reorder_point": 5}, {"sku": "sku2", "stock_level": 20, "reorder_point": 10}]
    oracle.load_data(data)
    assert len(oracle.get_dashboard_data()) == 2
    assert oracle.get_dashboard_data()[0]["sku"] == "sku1"
    assert oracle.get_dashboard_data()[0]["stock_level"] == 10
    assert oracle.get_dashboard_data()[0]["reorder_point"] == 5
    assert oracle.get_dashboard_data()[1]["sku"] == "sku2"
    assert oracle.get_dashboard_data()[1]["stock_level"] == 20
    assert oracle.get_dashboard_data()[1]["reorder_point"] == 10

def test_get_reorder_points():
    oracle = StockOracle()
    oracle.add_stock_item("sku1", 10, 5)
    oracle.add_stock_item("sku2", 20, 10)
    assert oracle.get_reorder_points() == {"sku1": 5, "sku2": 10}

def test_get_dashboard_data_performance():
    oracle = StockOracle()
    for i in range(10000):
        oracle.add_stock_item(f"sku{i}", 10, 5)
    import time
    start_time = time.time()
    oracle.get_dashboard_data()
    end_time = time.time()
    assert end_time - start_time < 2

def test_get_dashboard_data_empty():
    oracle = StockOracle()
    assert oracle.get_dashboard_data() == []
