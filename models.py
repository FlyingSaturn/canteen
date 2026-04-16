from dataclasses import dataclass, field

@dataclass
class Order:
    customer_id: int
    items: dict[str, int] # orders and their quantities

@dataclass
class Counter:
    id: int
    location: complex
    item_by_customer: dict = field(default_factory=dict)
    queue: list[Order] = None


