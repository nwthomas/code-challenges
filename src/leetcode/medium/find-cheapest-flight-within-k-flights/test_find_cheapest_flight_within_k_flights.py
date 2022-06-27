from find_cheapest_flight_within_k_flights import find_cheapest_price
import unittest

class TestFindCheapestPrice(unittest.TestCase):
    def test_finds_cheapest_flight_in_list_of_flights(self):
        number_of_nodes = 4
        flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
        source = 0
        destination = 3
        allowed_stops = 1

        result = find_cheapest_price(number_of_nodes, flights, source, destination, allowed_stops)
        self.assertEqual(result, 700)

if __name__ == "__main__":
    unittest.main()