from config import ITEMS
from models import Order

def efficiency_score(item_name: str, item_position: complex, counter_location: complex, item_by_customer: dict) -> float:
    travel_cost = abs(item_position - counter_location)
    # Total quantity of this item across all customers
    total_quantity = sum(item_by_customer[item_name].values())
    # Efficiency: lower is better (cheap + high volume)
    efficiency = travel_cost / total_quantity
    return efficiency


def batch_by_item(queue: list, item_by_customer: dict, counter_location: complex) -> dict:
    # queue is a list of Order objects
    for order in queue:
        for item_name, quantity in order.items.items():
            if item_name not in item_by_customer:
                item_by_customer[item_name] = {}
            item_by_customer[item_name][order.customer_id] = quantity

    sorted_items = sorted(
            item_by_customer.items(),
            key=lambda x: efficiency_score(x[0], ITEMS[x[0]], counter_location, item_by_customer)
            )

    return dict(sorted_items) # because item_by_customer is dict, dict preserves insertion order
