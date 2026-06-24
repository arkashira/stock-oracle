import json
from dataclasses import dataclass
from typing import List

@dataclass
class StockItem:
    sku: str
    stock_level: int
    reorder_point: int

class StockOracle:
    def __init__(self):
        self.stock_items = []

    def add_stock_item(self, sku: str, stock_level: int, reorder_point: int):
        self.stock_items.append(StockItem(sku, stock_level, reorder_point))

    def get_dashboard_data(self):
        return [{"sku": item.sku, "stock_level": item.stock_level, "reorder_point": item.reorder_point} for item in self.stock_items]

    def load_data(self, data: List[dict]):
        for item in data:
            self.add_stock_item(item["sku"], item["stock_level"], item["reorder_point"])

    def get_reorder_points(self):
        return {item.sku: item.reorder_point for item in self.stock_items}
