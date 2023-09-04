class Point():
    def __init__(self, coordinateX, coordinateY):
        self.x = coordinateX
        self.y = coordinateY

p = Point(2, 5)
print(p.x)
print(p.y)

class Flight():
    def __init__(self, capacity) :
        self.capacity = capacity
        self.passegers = []
    
    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passegers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passegers)
    

flight = Flight(2)

print(flight.capacity)
print(flight.passegers)
people = ["Lakhwinder", "Lucky", "Lakhveer", "Queen"]

for person in people:
    success =   flight.add_passenger(person)
    if success:
        print(f"Added {person} to flight successfully.")
    else:
        print(f"No available seat for {person}")


print(flight.passegers)