class FlightRegistry:
    def __init__(self):
        self.registry = []

    def addFlight(self, flight):
        self.registry.append(flight)

    def deleteFlight(self, flightId):
        self.registry = filter(lambda x: x.flight_id != flightId, self.registry)

    def __repr__(self):
        return repr(f'Flight registry: {list(map(lambda x: x.flight_id, self.registry))}')
