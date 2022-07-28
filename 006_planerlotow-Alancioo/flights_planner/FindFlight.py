from datetime import datetime


def getDateDiff(first_date, second_date):
    first_datetime_obj = datetime.strptime(first_date, '%Y-%m-%d')
    second_datetime_obj = datetime.strptime(second_date, '%Y-%m-%d')
    return abs(first_datetime_obj - second_datetime_obj)


def compareDate(departure_date, max_date):
    departure_datetime_obj = datetime.strptime(departure_date, '%Y-%m-%d')
    max_datetime_obj = datetime.strptime(max_date, '%Y-%m-%d')
    today_datetime_obj = datetime.strptime(datetime.now().strftime("%Y-%m-%d"), '%Y-%m-%d')
    if max_datetime_obj >= departure_datetime_obj >= today_datetime_obj:
        return True
    else:
        return False


class FindFlight:
    def __init__(self, flight_registry):
        self.flight_registry = flight_registry.registry

    def getFlights(self, from_city, to_city, to_date, max_price):
        return list(filter(lambda x:
                           x.from_city == from_city
                           and x.to_city == to_city
                           and x.price <= max_price
                           and compareDate(x.departure_date, to_date)
                           and len(x.passenger_set) < x.max_passengers,
                           self.flight_registry))

    def getFlightWithTheLowestPrice(self, from_city, to_city):
        lowest_price = float('inf')
        for flight in self.flight_registry:
            if flight.from_city == from_city and flight.to_city == to_city and flight.price < lowest_price:
                lowest_price = flight.price
        return list(filter(lambda x:
                           x.from_city == from_city
                           and x.to_city == to_city
                           and x.price == lowest_price
                           and len(x.passenger_set) < x.max_passengers,
                           self.flight_registry))

    def getFlightWithTheShortestTime(self, from_city, to_city):
        shortest_time = float('inf')
        for flight in self.flight_registry:
            if flight.from_city == from_city and flight.to_city == to_city and flight.time < shortest_time:
                shortest_time = flight.time
        return list(filter(lambda x:
                           x.from_city == from_city
                           and x.to_city == to_city
                           and x.time == shortest_time
                           and len(x.passenger_set) < x.max_passengers,
                           self.flight_registry))

    def getFlightWithTheClosestDepartureDate(self, from_city, to_city, departure_date):
        if len(self.flight_registry) == 0:
            return 'Flight registry is empty'
        else:
            lowest_departure_diff = getDateDiff(departure_date, self.flight_registry[0].departure_date)
        for flight in self.flight_registry:
            if flight.from_city == from_city and flight.to_city == to_city and getDateDiff(departure_date,
                                                                                           flight.departure_date) < lowest_departure_diff:
                lowest_departure_diff = getDateDiff(departure_date, flight.departure_date)
        return list(filter(lambda x:
                           x.from_city == from_city
                           and x.to_city == to_city
                           and getDateDiff(departure_date, x.departure_date) == lowest_departure_diff
                           and len(x.passenger_set) < x.max_passengers,
                           self.flight_registry))
