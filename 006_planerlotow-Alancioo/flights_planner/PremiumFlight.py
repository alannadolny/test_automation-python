from flights_planner.Flight import Flight


class PremiumFlight(Flight):

    def __init__(self, flight_id, from_city, to_city, price, time, max_passengers, departure_date):
        super().__init__(flight_id, from_city, to_city, price, time, max_passengers, departure_date)

    def add_passenger(self, passenger):
        number_of_passengers = len(self.passenger_set)
        if passenger.vip:
            self.passenger_set.add(passenger)
        return len(self.passenger_set) == number_of_passengers + 1

    def remove_passenger(self, passenger):
        number_of_passengers = len(self.passenger_set)
        if passenger.vip and passenger in self.passenger_set:
            self.passenger_set.remove(passenger)
        return len(self.passenger_set) == number_of_passengers - 1