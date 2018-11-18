import unittest
import shutil

from part1c import capacity_satisfied
from part1c import check_user_input

class BookingGoTests(unittest.TestCase):

    def test_minibus_capacity(self):
        self.assertTrue(capacity_satisfied('MINIBUS', 15))
        self.assertTrue(capacity_satisfied('MINIBUS', 16))
        self.assertFalse(capacity_satisfied('MINIBUS', 17))

    def test_people_carrier_capacity(self):
        self.assertTrue(capacity_satisfied('PEOPLE_CARRIER', 5))
        self.assertTrue(capacity_satisfied('PEOPLE_CARRIER', 6))
        self.assertFalse(capacity_satisfied('PEOPLE_CARRIER', 7))

    def test_luxury_people_carrier_capacity(self):
        self.assertTrue(capacity_satisfied('LUXURY_PEOPLE_CARRIER', 5))
        self.assertTrue(capacity_satisfied('LUXURY_PEOPLE_CARRIER', 6))
        self.assertFalse(capacity_satisfied('LUXURY_PEOPLE_CARRIER', 7))

    def test_standard_capacity(self):
        self.assertTrue(capacity_satisfied('STANDARD', 3))
        self.assertTrue(capacity_satisfied('STANDARD', 4))
        self.assertFalse(capacity_satisfied('STANDARD', 5))

    def test_executive_capacity(self):
        self.assertTrue(capacity_satisfied('EXECUTIVE', 3))
        self.assertTrue(capacity_satisfied('EXECUTIVE', 4))
        self.assertFalse(capacity_satisfied('EXECUTIVE', 5))

    def test_luxury_capacity(self):
        self.assertTrue(capacity_satisfied('LUXURY', 3))
        self.assertTrue(capacity_satisfied('LUXURY', 4))
        self.assertFalse(capacity_satisfied('LUXURY', 5))

    def test_working_arguments(self):
        try:
            argv = ['', '3.410632,-2.157533', '3.410632,-2.157533', '3']
            check_user_input(argv)
        except:
            self.fail("Unexpected error raised with working arguments")

    def test_incorrect_argument_length(self):
        argv = ['', '3.410632,-2.157533']
        with self.assertRaises(ValueError):
            check_user_input(argv)

    def test_invalid_passenger_field(self):
        argv = ['', '3.410632,-2.157533', '3.410632,-2.157533', 'HelloIAmNotANumber']
        with self.assertRaises(ValueError):
            check_user_input(argv)

    def test_lat1_out_of_range(self):
        argv = ['', '100.410632,-2.157533', '3.410632,-2.157533', '3']    
        with self.assertRaises(ValueError):
            check_user_input(argv)
        

    def test_lon1_out_of_range(self):
        argv = ['', '3.410632,-180.157533', '3.410632,-2.157533', '3']
        with self.assertRaises(ValueError):
            check_user_input(argv)

    def test_lat2_out_of_range(self):
        argv = ['', '3.410632,-2.157533', '120.410632,-2.157533', '3']
        with self.assertRaises(ValueError):
            check_user_input(argv)

    def test_lon2_out_of_range(self):
        argv = ['', '3.410632,-2.157533', '3.410632,-200.157533', '3']
        with self.assertRaises(ValueError):
            check_user_input(argv)

    def test_too_many_passengers(self):
        argv = ['', '3.410632,-2.157533', '3.410632,-2.157533', '17']
        with self.assertRaises(ValueError):
            check_user_input(argv)

    def test_less_than_one_passenger(self):
        argv = ['', '3.410632,-2.157533', '3.410632,-2.157533', '0']
        with self.assertRaises(ValueError):
            check_user_input(argv)


unittest.TextTestRunner(verbosity=2).run(unittest.TestLoader().loadTestsFromTestCase(BookingGoTests))
shutil.rmtree('__pycache__')