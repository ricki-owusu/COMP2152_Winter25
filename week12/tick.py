# Tick class for aggregation
class Tick:
    def __init__(self):
        print("Aggregation: Tick is Created")

    def consume_blood(self):
        print("Tick is consuming blood...")

    def __del__(self):
        print("Aggregation: Tick is Destroyed")