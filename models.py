from dataclasses import dataclass


@dataclass
class Item:
    name: str
    cost: complex  # position in 2D space

@dataclass
class Order:
    customer_id: int
    items: dict[str, int] # orders and their quantities
    priority: float = 0.0  
    arrival_time: float = 0.0

@dataclass
class Counter:
    id: int
    location: complex
    item_offset: complex
    queue: list[Order] = None
    item_by_customer: dict = {}

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
