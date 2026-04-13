from models import Order
from batching import batch_by_item

# Create orders
orders = [
        Order(1, {"chips": 2, "cold_drink": 1}),
        Order(2, {"biscuits": 1}),
]

# Use batching
result = batch_by_item(orders, {})
print(result)
