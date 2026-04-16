from flask import Flask, render_template, request, jsonify
from models import Order, Counter
from config import ITEMS, COUNTER_A_LOCATION, COUNTER_B_LOCATION
from input_script import generate_orders
from sim import Simulation
import json
 
app = Flask(__name__)
 
@app.route('/')
def index():
    return render_template('index.html')
 
@app.route('/api/simulate', methods=['POST'])
def simulate():
    """Run simulation with given number of customers."""
    try:
        data = request.json
        num_customers = int(data.get('num_customers', 10))
        
        # Generate random orders
        raw_orders = generate_orders(num_customers=num_customers)
        
        # Split between counters
        split_point = len(raw_orders) // 2
        counter_a_orders = [Order(i, raw_orders[i]) for i in range(split_point)]
        counter_b_orders = [Order(split_point + i, raw_orders[split_point + i]) 
                           for i in range(len(raw_orders) - split_point)]

        # Making instances for the counters
        counter_a = Counter(
            id=1,
            location=COUNTER_A_LOCATION,
            queue=counter_a_orders
        )
        counter_b = Counter(
            id=2,
            location=COUNTER_B_LOCATION,
            queue=counter_b_orders
        )
        
        # Simulating those instances
        sim = Simulation(counter_a, counter_b)
        sim.run_counter(counter_a)
        sim.run_counter(counter_b)
        
        # Format batches for JSON
        batches_a_formatted = {
            item: {
                'customers': list(customers.keys()),
                'total_qty': sum(customers.values()),
                'cost': abs(ITEMS[item] - counter_a.location)
            }
            for item, customers in counter_a.item_by_customer.items()
        }
        batches_b_formatted = {
            item: {
                'customers': list(customers.keys()),
                'total_qty': sum(customers.values()),
                'cost': abs(ITEMS[item] - counter_b.location)
            }
            for item, customers in counter_b.item_by_customer.items()
        }

        return jsonify({
            'success': True,
            'metrics': sim.get_metrics(),
            'batches_a': batches_a_formatted,
            'batches_b': batches_b_formatted,
            'num_customers': num_customers
        })

    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400


@app.route('/api/items', methods=['GET'])
def get_items():
    """Return item positions for visualization."""
    items_formatted = {
        name: {
            'real': position.real,
            'imag': position.imag,
            'magnitude': abs(position)
        }
        for name, position in ITEMS.items()
    }
    return jsonify(items_formatted)
 
if __name__ == '__main__':
    app.run(debug=True, port=5000)
