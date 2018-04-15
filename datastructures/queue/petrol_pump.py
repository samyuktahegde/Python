class PetrolPump:
    def __init__(self, petrol, distance):
        self.petrol = petrol
        self.distance = distance

def print_tour(array):
    n = len(array)
    start = 0
    end = 1
    current_petrol = array[start].petrol = array[start].distance
    while end != start and current_petrol<0:
        while current_petrol<0 and start!=end:
            current_petrol -=