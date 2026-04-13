from dataclasses import dataclass
from models import Order, Counter
from batching import batch_by_item

# Create orders
orders = [
        Order(1, {"chips": 2, "chocolates": 1}),
        Order(2, {"biscuits": 2}),
]

# Per-counter: just the offset
counter_a = Counter(
    id=1,
    location=0+0j,
    item_offset=0+0j  # no shift
)

counter_b = Counter(
    id=2,
    location=0+3j,
    item_offset=0+3j  # everything shifted by 3i
)

# Use batching
print("Counter A sorted:", batch_by_item(orders, {}, counter_a.item_offset))
print("Counter B sorted:", batch_by_item(orders, {}, counter_b.item_offset))

