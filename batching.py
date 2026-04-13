from models import Order
ITEMS = {
        "biscuits" : 1.5j,
        "bakery_goods" : 0,
        "cash_counter" : 1,
        "chewing_gums" : 4j,
        "chocolates" : -1j,
        "cold_drinks": 7 + 1.5j,
        "hotdog" : 3j,
        "ice-cream" : 4 + 1.5j,
        "kurkure_chips" : 6,
        "lollipop": 0.5 + 4j,
        "makhana": 0.5 + 3j,
        "orbit": 0.6 + 3.5j,
        "phoochka_chips": 0.5,
        "sandwich" : 3j,
        "sanitary_napkins": 4j,
}


def efficiency_score(item_name: str, item_position: complex, counter_location, item_by_customer):
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
