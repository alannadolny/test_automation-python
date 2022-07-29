from behave import *
from flights_planner.EconomyFlight import EconomyFlight
from flights_planner.BusinessFlight import BusinessFlight
from flights_planner.PremiumFlight import PremiumFlight
from flights_planner.FindFlight import FindFlight
from flights_planner.FlightRegistry import FlightRegistry

use_step_matcher("re")


@given("there are different flights")
def step_impl(context):
    context.economy_flight = EconomyFlight("1", 'Warsaw', 'Paris', 10, 60, 10, '2023-01-01')
    context.business_flight = BusinessFlight("2", 'Warsaw', 'Paris', 10, 60, 10, '2023-02-01')
    context.premium_flight = PremiumFlight("3", 'Berlin', 'Paris', 10, 40, 15, '2023-01-01')
    context.flight_registry = FlightRegistry()
    context.flight_registry.addFlight(context.economy_flight)
    context.flight_registry.addFlight(context.business_flight)
    context.flight_registry.addFlight(context.premium_flight)


@when("you have specified cities and not limiting date and price")
def step_impl(context):
    context.find_flights = FindFlight(context.flight_registry)
    context.get_flights = context.find_flights.getFlights('Warsaw', 'Paris', '2030-01-01', 1000)


@then("you can find flights between appropriate cities")
def step_impl(context):
    assert len(context.get_flights) == 2
    assert context.get_flights[
               0] == context.economy_flight
    assert context.get_flights[
               1] == context.business_flight


@given("there are flights with the same cities but with different price")
def step_impl(context):
    context.economy_flight = EconomyFlight("1", 'Warsaw', 'Paris', 15, 60, 10, '2023-01-01')
    context.business_flight = BusinessFlight("2", 'Warsaw', 'Paris', 20, 60, 10, '2023-02-01')
    context.premium_flight = PremiumFlight("3", 'Warsaw', 'Paris', 11, 40, 15, '2023-01-01')
    context.flight_registry = FlightRegistry()
    context.flight_registry.addFlight(context.economy_flight)
    context.flight_registry.addFlight(context.business_flight)
    context.flight_registry.addFlight(context.premium_flight)


@when("you have specified price and not limiting cities and date")
def step_impl(context):
    context.find_flights = FindFlight(context.flight_registry)
    context.get_flights = context.find_flights.getFlights('Warsaw', 'Paris', '2030-01-01', 14)


@then("you can find flights with cost lower than specified price")
def step_impl(context):
    assert len(context.get_flights) == 1
    assert context.get_flights[
               0] == context.premium_flight


@given("there are flights with different date but with the same cities and price")
def step_impl(context):
    context.economy_flight = EconomyFlight("1", 'Warsaw', 'Paris', 15, 60, 10, '2022-12-10')
    context.business_flight = BusinessFlight("2", 'Warsaw', 'Paris', 15, 60, 10, '2022-11-01')
    context.premium_flight = PremiumFlight("3", 'Warsaw', 'Paris', 15, 40, 15, '2022-11-11')
    context.flight_registry = FlightRegistry()
    context.flight_registry.addFlight(context.economy_flight)
    context.flight_registry.addFlight(context.business_flight)
    context.flight_registry.addFlight(context.premium_flight)


@when("you have specified date and not limiting cities and price")
def step_impl(context):
    context.find_flights = FindFlight(context.flight_registry)
    context.get_flights = context.find_flights.getFlights('Warsaw', 'Paris', '2022-11-12', 1000)


@then("you can find flights in appropriate period")
def ste_impl(context):
    assert len(context.get_flights) == 2
    assert context.get_flights[
               0] == context.business_flight
    assert context.get_flights[
               1] == context.premium_flight


@given("there are flights between the same places, but with different prices")
def ste_impl(context):
    context.economy_flight = EconomyFlight("1", 'Warsaw', 'Paris', 10, 60, 10, '2022-12-10')
    context.business_flight = BusinessFlight("2", 'Warsaw', 'Paris', 8, 60, 10, '2022-11-01')
    context.premium_flight = PremiumFlight("3", 'Warsaw', 'Paris', 12, 40, 15, '2022-11-11')
    context.flight_registry = FlightRegistry()
    context.flight_registry.addFlight(context.economy_flight)
    context.flight_registry.addFlight(context.business_flight)
    context.flight_registry.addFlight(context.premium_flight)


@when("you chose cities and searching for lowest price")
def ste_impl(context):
    context.find_flights = FindFlight(context.flight_registry)
    context.get_flight_with_the_lowest_price = context.find_flights.getFlightWithTheLowestPrice('Warsaw', 'Paris')


@then("you can find flight with the lowest price between appropriate cities")
def ste_impl(context):
    assert len(context.get_flight_with_the_lowest_price) == 1
    assert context.get_flight_with_the_lowest_price[
               0] == context.business_flight


@given("there are flights between the same places, but only two flights have the same price")
def ste_impl(context):
    context.economy_flight = EconomyFlight("1", 'Warsaw', 'Paris', 10, 60, 10, '2022-12-10')
    context.business_flight = BusinessFlight("2", 'Warsaw', 'Paris', 8, 60, 10, '2022-11-01')
    context.premium_flight = PremiumFlight("3", 'Warsaw', 'Paris', 8, 40, 15, '2022-11-11')
    context.flight_registry = FlightRegistry()
    context.flight_registry.addFlight(context.economy_flight)
    context.flight_registry.addFlight(context.business_flight)
    context.flight_registry.addFlight(context.premium_flight)


@then("you can find more than one flight with the lowest price between appropriate cities")
def ste_impl(context):
    assert len(context.get_flight_with_the_lowest_price) == 2
    assert context.get_flight_with_the_lowest_price[
               0] == context.business_flight
    assert context.get_flight_with_the_lowest_price[
               1] == context.premium_flight


@given("there are flights between the same places, but with different flying time")
def ste_impl(context):
    context.economy_flight = EconomyFlight("1", 'Warsaw', 'Paris', 10, 60, 10, '2022-12-10')
    context.business_flight = BusinessFlight("2", 'Warsaw', 'Paris', 8, 55, 10, '2022-11-01')
    context.premium_flight = PremiumFlight("3", 'Warsaw', 'Paris', 8, 40, 15, '2022-11-11')
    context.flight_registry = FlightRegistry()
    context.flight_registry.addFlight(context.economy_flight)
    context.flight_registry.addFlight(context.business_flight)
    context.flight_registry.addFlight(context.premium_flight)


@when("you chose cities and searching for the shortest flying time")
def ste_impl(context):
    context.find_flights = FindFlight(context.flight_registry)
    context.get_flight_with_the_shortest_time = context.find_flights.getFlightWithTheShortestTime('Warsaw', 'Paris')


@then("you can find flight with the shortest flying time")
def ste_impl(context):
    assert len(context.get_flight_with_the_shortest_time) == 1
    assert context.get_flight_with_the_shortest_time[
               0] == context.premium_flight


@given("there are flights between the same places, two with the same flying time")
def ste_impl(context):
    context.economy_flight = EconomyFlight("1", 'Warsaw', 'Paris', 10, 40, 10, '2022-12-10')
    context.business_flight = BusinessFlight("2", 'Warsaw', 'Paris', 8, 55, 10, '2022-11-01')
    context.premium_flight = PremiumFlight("3", 'Warsaw', 'Paris', 8, 40, 15, '2022-11-11')
    context.flight_registry = FlightRegistry()
    context.flight_registry.addFlight(context.economy_flight)
    context.flight_registry.addFlight(context.business_flight)
    context.flight_registry.addFlight(context.premium_flight)


@then("you can find more than one flight with the shortest flying time")
def ste_impl(context):
    assert len(context.get_flight_with_the_shortest_time) == 2
    assert context.get_flight_with_the_shortest_time[
               0] == context.economy_flight
    assert context.get_flight_with_the_shortest_time[
               1] == context.premium_flight

@given("there are flights between the same places, one has the same date as you need")
def ste_impl(context):
    context.economy_flight = EconomyFlight("1", 'Warsaw', 'Paris', 10, 60, 10, '2022-12-10')
    context.business_flight = BusinessFlight("2", 'Warsaw', 'Paris', 8, 55, 10, '2022-11-01')
    context.premium_flight = PremiumFlight("3", 'Warsaw', 'Paris', 8, 40, 15, '2022-11-11')
    context.flight_registry = FlightRegistry()
    context.flight_registry.addFlight(context.economy_flight)
    context.flight_registry.addFlight(context.business_flight)
    context.flight_registry.addFlight(context.premium_flight)


@when("you search for the flight with the closest departure date to given date")
def ste_impl(context):
    context.find_flights = FindFlight(context.flight_registry)
    context.get_flight_with_the_closest_departure_date = context.find_flights.getFlightWithTheClosestDepartureDate('Warsaw', 'Paris', '2022-12-10')


@then("you can find flight with exactly the same date as you have given")
def ste_impl(context):
    assert len(context.get_flight_with_the_closest_departure_date) == 1
    assert context.get_flight_with_the_closest_departure_date[
               0] == context.economy_flight

@given("there are flights between the same places, two dates have the same diff from given date")
def ste_impl(context):
    context.economy_flight = EconomyFlight("1", 'Warsaw', 'Paris', 10, 60, 10, '2022-12-10')
    context.business_flight = BusinessFlight("2", 'Warsaw', 'Paris', 8, 55, 10, '2022-12-12')
    context.premium_flight = PremiumFlight("3", 'Warsaw', 'Paris', 8, 40, 15, '2022-11-11')
    context.flight_registry = FlightRegistry()
    context.flight_registry.addFlight(context.economy_flight)
    context.flight_registry.addFlight(context.business_flight)
    context.flight_registry.addFlight(context.premium_flight)


@when("you search for the flights with the closest departure date to given date")
def ste_impl(context):
    context.find_flights = FindFlight(context.flight_registry)
    context.get_flight_with_the_closest_departure_date = context.find_flights.getFlightWithTheClosestDepartureDate('Warsaw', 'Paris', '2022-12-11')


@then("you can find flights with the diff from given date")
def ste_impl(context):
    assert len(context.get_flight_with_the_closest_departure_date) == 2
    assert context.get_flight_with_the_closest_departure_date[
               0] == context.economy_flight
    assert context.get_flight_with_the_closest_departure_date[
               1] == context.business_flight