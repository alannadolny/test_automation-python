from abc import ABC, abstractmethod
from flights_planner.Exceptions import InappropriateTimeException, InappropriatePrice, MaxPassengersShouldBeHigherThan0, InappropriateDate
from re import fullmatch


class Flight(ABC):

    def __init__(self, flight_id, from_city, to_city, price, time, max_passengers, departure_date):
        self.__flight_id = flight_id
        self.__passenger_set = set()
        self.__from_city = from_city
        self.__to_city = to_city
        self.price = price
        self.time = time
        self.max_passengers = max_passengers
        self.departure_date = departure_date

    @property
    def max_passengers(self):
        return self.__max_passengers

    @max_passengers.setter
    def max_passengers(self, p):
        if p <= 0:
            raise MaxPassengersShouldBeHigherThan0
        else:
            self.__max_passengers = p

    @property
    def departure_date(self):
        return self.__departure_date

    @departure_date.setter
    def departure_date(self, p):
        if fullmatch('^202[1-9]-(0[1-9]|1[0-2])-(0[1-9]|[1-3][0-9])', p) is None:
            raise InappropriateDate
        else:
            self.__departure_date = p

    @property
    def time(self):
        return self.__time

    @time.setter
    def time(self, p):
        try:
            if int(p) <= 0:
                raise InappropriateTimeException
            else:
                self.__time = p
        except ValueError:
            raise InappropriateTimeException

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, p):
        try:
            if int(p) <= 0:
                raise InappropriatePrice
            else:
                self.__price = p
        except ValueError:
            raise InappropriatePrice

    @property
    def to_city(self):
        return self.__to_city

    @property
    def from_city(self):
        return self.__from_city

    @property
    def flight_id(self):
        return self.__flight_id

    @property
    def passenger_set(self):
        return self.__passenger_set

    @passenger_set.setter
    def passenger_set(self, value):
        self.__passenger_set = value

    @abstractmethod
    def add_passenger(self, passenger):
        pass

    @abstractmethod
    def remove_passenger(self, passenger):
        pass

    def __repr__(self):
        return repr(
            f'Flight id: {self.flight_id},'
            f' from: {self.from_city},'
            f' to: {self.to_city},'
            f' price: {self.price},'
            f' flight time: {self.time} min,'
            f' departure date: {self.departure_date},'
            f' available seats: {self.max_passengers - len(self.passenger_set)}')
