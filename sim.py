from input_script import generate_orders
from models import Order, Counter
from batching import batch_by_item
from config import ITEMS, COUNTER_A_LOCATION, COUNTER_B_LOCATION

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
        counter.item_by_customer = batch_by_item(counter.queue, counter.item_by_customer, counter.location)

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


