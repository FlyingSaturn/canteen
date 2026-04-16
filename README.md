# canteen

An spatial optimization system for handling peak crowd @ *my* canteen.

## How to Run

Install Python. Then,

```bash
   pip install flask  # or whatever way pip works in your distro/OS
   cd canteen_project
   python app.py
   # Visit http://localhost:5000
```

## Setup

This canteen has two counters, A (left) and B (right). During the peak hours, the queue is not a FIFO queue, it's more of a blob of human beings  Counter A is filled up at first, because it's the nearest to most of the items out there.  

Shopkeepers here usually follow this algorithm:

1) Start
2) Traverse for one item (following the specific order of the customer)
3) Bring a specific quantity of the same item
4) Repeat Steps 2 to 4 until all the items exhaust
5) Deal with the next customer
6) Repeat Steps 2 to 6 until all the customers exhaust
7) End

The core inertia here is that items are brought at a time from one shelf. That's the core assumption.

## My approach

Akshually, building upon the same core assumption, we can think in terms of items rather than in terms of customers, rather than a single customer in terms of items. We just determine what's the most efficient item to approach ***in terms of the spatial cost and the quantity***. 

Here's what I propose:

1) Start
2) Traverse to the item most efficiently accessible
3) Bring the sum of quantities of the same item, distribute it to the required customers
4) Repeat Steps 2 to 4 until all the items exhaust
5) End

This obviously assumes that a shopkeeper has hands accomodating enough of the same kinds of items, which is not a problem for n <= 10. But even if there are baskets to hold many items, the core assumption of **bringing multiple items from the same section at a time** should be true, so it can be considered an invariant.

## Use of heuristic values

Heuristic values have been used to accurately portray the spatial cost. Here, the values are in complex numbers, rather than simple whole numbers.

An orthogonal axis was considered because vertical motion doesn't make sense to be represented in the same way we are describing horizontal motion. We had to subtract the counter position from the item's heuristic value to get the spatial cost.

## Getting Efficiency for each item

Let `total_qty = Sum of quantities asked by all the customers for this item`.

`Efficiency of accessing the item = Cost of Item / total\_qty`

We are sorting each of the items in an ascending order based on the value of the item's 'accessibility and efficiency' for this particular queue.

## Example

Student X needs 5 packets of Kurkure and 5 cups of coffee
Student Y just needs 1 packet of cake (one of the bakery goods)

Program generates

```
Stats:
{'counter_a': {'total_cost': 6.5, 'customers_served': 2},
 'counter_b': {'total_cost': 12.749585197648479, 'customers_served': 2}}

Counter A:
{'Bakery Goods': {'customers': [2],
                  'total_qty': 1,
                  'cost': 0.0,
                  'efficiency': 0.0},
 'Coffee': {'customers': [1], 'total_qty': 5, 'cost': 0.5, 'efficiency': 0.1},
 'Kurkure_chips': {'customers': [1],
                   'total_qty': 5,
                   'cost': 6.0,
                   'efficiency': 1.2}}

Counter B:
{'Coffee': {'customers': [1],
            'total_qty': 5,
            'cost': 3.0413812651491097,
            'efficiency': 0.6082762530298219},
 'Kurkure_chips': {'customers': [1],
                   'total_qty': 5,
                   'cost': 6.708203932499369,
                   'efficiency': 1.3416407864998738},
 'Bakery Goods': {'customers': [2],
                  'total_qty': 1,
                  'cost': 3.0,
                  'efficiency': 3.0}}
```

Counter A considered passing a single cake as more efficient, in spite of the sheer amount of orders. Counter B was 3 units away from the cake, and it therefore served coffee and Kurkure at first.

Note that X has customer ID 1, while Y has customer ID 2.

## Why this matters

- Catering on an item basis rather than a customer basis clears queues better. 10 people in a queue ordering the 3 same items in an AND manner will make the shopkeeper have 3 * 10 = 30 traversals. Compare that to my approach, which will simply take 3 traversals. It will account for a 90% drop in the number of traversals (considering the shopkeepers are using a basket to carry stuff).
- This is applicable right now, without any technological interference. Shopkeepers can just ask customers during the peak hours: what things they want, and how much of things they want. That simple gesture will significantly reduce traversal.

## Future scope

- This system is scalable. The state of `item_by_customer` is simply updated to better cater for the multiple trips of items. In the real world, the `item_by_customer` dictionary should be concurrently updated everytime the shopkeeper brings an item and sees a new person in the queue.
- Multithreading can allow it to be a living and breathing system, by implementing the real-time generation of a queue. This allows for implementing probabilistic arrival of people based on Poisson distribution.
- Notice that Cup Noodles/Coffee requires a delay separate from the heurisitic values, because water takes a separate amount of time to fill up. This delay, independent of the spatial cost, requires separate consideration.
- After all the orders of a particular customer are fulfilled, for the money, the customer can place another order, this time simply mentioning the cash counter. This can be used in the multithreading system as I mentioned.


