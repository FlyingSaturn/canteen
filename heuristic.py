from dataclasses import dataclass
from typing import List
 
cost_function = {
        "cash_counter" : "1",
        "biscuits" : "0",
        "sanitary_napkins": "2i",
        "chewing_gums" : "2i",
        "chocolates" : "0",
        "ice-cream" : "1.5 + i",
        "chips" : "3",
        "cold_drinks": "5 + 5i"
}

@dataclass
class Item:
    name: str
    cost: complex  # position in 2D space

@dataclass
class Order:
    customer_id: int
    items: List[str]
    priority: float = 0.0  # epsilon value
    arrival_time: float = 0.0

@dataclass
class Counter:
    id: int
    location: complex
    cost_heuristic: dict  # item -> cost
    queue: List[Order] = None

def shopkeeper(name):
     // Determine which item to choose based on cost  
    // Traverse
    // Come back


//  cost = cost_function.get(name, "Unknown")


def customer():
    // Generate based on queues
    // ask for random items in random quantities or 1
    // 
