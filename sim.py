from models import Order, Counter
from batching import update_item_map, sort_by_item, efficiency_score
from config import ITEMS, COUNTER_A_LOCATION, COUNTER_B_LOCATION
# import pprint
# import copy

class Simulation:
    def __init__(self, counter_a, counter_b):
        self.counter_a = counter_a
        self.counter_b = counter_b
        self.total_cost_a = 0
        self.total_cost_b = 0
        self.customers_served_a = 0
        self.customers_served_b = 0
    
    def run_counter(self, counter):
        """Simulate one counter serving a queue."""
        update_item_map(counter.queue, counter.item_by_customer)
        counter.item_by_customer = sort_by_item(counter.item_by_customer, counter.location)
        unique_customers = set()  # Track unique customers 

        for item_name, customers in counter.item_by_customer.items():
            cost = abs(ITEMS[item_name] - counter.location)
            qty = sum(customers.values())

            unique_customers.update(customers.keys())

            # Accumulate metrics
            if counter.id == 1:
                self.total_cost_a += cost
            else:
                self.total_cost_b += cost
                
        # Count unique customers at the end 
        if counter.id == 1:
            self.customers_served_a = len(unique_customers)
        else:
            self.customers_served_b = len(unique_customers)


    def get_metrics(self):
        return {
            "counter_a": {
                "total_cost": self.total_cost_a,
                "customers_served": self.customers_served_a,
            },
            "counter_b": {
                "total_cost": self.total_cost_b,
                "customers_served": self.customers_served_b,
            }
        }

# Remove the multi-line comment to test
'''
counter_a_orders = [Order(1, {"Kurkure_chips": 5, "Coffee": 5}), 
                    Order(2, {"Bakery Goods": 1})]
counter_b_orders = copy.deepcopy(counter_a_orders)

# Making instances for the counters
counter_a = Counter(
    id=1,
    location=0+0j,
    queue=counter_a_orders
)
counter_b = Counter(
    id=2,
    location=0+3j,
    queue=counter_b_orders
)

# Simulating those instances
sim = Simulation(counter_a, counter_b)
sim.run_counter(counter_a)
sim.run_counter(counter_b)

batches_a_formatted = {
    item: {
        'customers': list(customers.keys()),
        'total_qty': sum(customers.values()),
        'cost': abs(ITEMS[item] - counter_a.location),
        'efficiency': abs(ITEMS[item] - counter_a.location) / sum(customers.values())
    }
    for item, customers in counter_a.item_by_customer.items()
}
batches_b_formatted = {
    item: {
        'customers': list(customers.keys()),
        'total_qty': sum(customers.values()),
        'cost': abs(ITEMS[item] - counter_b.location),
        'efficiency': abs(ITEMS[item] - counter_b.location) / sum(customers.values())
    }
    for item, customers in counter_b.item_by_customer.items()
}
print("Counter A: ")
pprint.pprint(batches_a_formatted, sort_dicts=False)
print("\nCounter B: ")
pprint.pprint(batches_b_formatted, sort_dicts=False)
print("\n\nStats: ")
pprint.pprint(sim.get_metrics(), sort_dicts=False)
'''

