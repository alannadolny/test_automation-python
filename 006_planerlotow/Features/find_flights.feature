Feature: Finding Flights
  The company allows users to find flights between chosen cities,
  in specific time period and with appropriate price limit.

  Scenario: Specified cities, not limiting date and price
    Given there are different flights
    When you have specified cities and not limiting date and price
    Then you can find flights between appropriate cities

  Scenario: Specified price, not limiting cities and date
    Given there are flights with the same cities but with different price
    When you have specified price and not limiting cities and date
    Then you can find flights with cost lower than specified price

  Scenario: Specified date, not limiting cities and price
    Given there are flights with different date but with the same cities and price
    When you have specified date and not limiting cities and price
    Then you can find flights in appropriate period

  Scenario: All kind of flights, all of them have different price
    Given there are flights between the same places, but with different prices
    When you chose cities and searching for lowest price
    Then you can find flight with the lowest price between appropriate cities

  Scenario: All kind of flights, two of them have the same price
    Given there are flights between the same places, but only two flights have the same price
    When you chose cities and searching for lowest price
    Then you can find more than one flight with the lowest price between appropriate cities

  Scenario: All kind of flights, all of them have different flying time
    Given there are flights between the same places, but with different flying time
    When you chose cities and searching for the shortest flying time
    Then you can find flight with the shortest flying time

  Scenario: All kind of flights, but only two of them have the same flying time
    Given there are flights between the same places, two with the same flying time
    When you chose cities and searching for the shortest flying time
    Then you can find more than one flight with the shortest flying time

  Scenario: All kind of flights, all departure dates are different
    Given there are flights between the same places, one has the same date as you need
    When you search for the flight with the closest departure date to given date
    Then you can find flight with exactly the same date as you have given

  Scenario: All kind of flights, all departure dates are close to each other
    Given there are flights between the same places, two dates have the same diff from given date
    When you search for the flights with the closest departure date to given date
    Then you can find flights with the diff from given date