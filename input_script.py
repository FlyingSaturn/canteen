from random import choice, sample
from config import ITEMS


def generate_orders(num_customers=None):
    if num_customers is None:
        num_customers = choice(range(3, 6))
    queue = []

    for i in range(0, num_customers):
        things = {}
        item = choice(range(1, 6))
        unique_picks = sample(list(ITEMS.keys()), item)
        for j in unique_picks:
            things[j] = choice(range(1, 3))
        queue.append(things)
    return queue
