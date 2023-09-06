from project.trip import Trip

from unittest import TestCase, main


class TripTests(TestCase):
    def setUp(self) -> None:
        self.trip = Trip(50, 5, False)

    def test_constructor(self):
        self.assertEqual(50, self.trip.budget)
        self.assertEqual(5, self.trip.travelers)
        self.assertFalse(self.trip.is_family)

    def test_travelers_setter_to_raise_exception(self):
        with self.assertRaises(ValueError) as ve:
            self.trip.travelers = 0
        expected = 'At least one traveler is required!'
        self.assertEqual(expected, str(ve.exception))

    def test_travelers_change_value(self):
        self.trip.travelers = 1
        self.assertEqual(1, self.trip.travelers)

    def test_is_family_is_set_to_false_in_one_person_trip(self):
        self.trip.travelers = 1
        self.trip.is_family = True
        self.assertFalse(self.trip.is_family)

    def test_is_family_is_set_to_true_for_family_trip(self):
        self.assertFalse(self.trip.is_family)
        self.trip.is_family = True
        self.assertTrue(self.trip.is_family)

    def test_book_a_trip_with_unknown_destination(self):
        expected = 'This destination is not in our offers, please choose a new one!'
        result = self.trip.book_a_trip("Italy")
        self.assertEqual(expected, result)

    def test_book_a_trip_with_not_enough_money(self):
        expected = 'Your budget is not enough!'
        result = self.trip.book_a_trip("Australia")
        self.assertEqual(expected, result)

    def test_book_a_trip_with_non_family_option(self):
        self.trip.budget = 3000
        self.trip.travelers = 5
        expected = f'Successfully booked destination Bulgaria! Your budget left is 500.00'
        result = self.trip.book_a_trip("Bulgaria")
        self.assertEqual(expected, result)
        self.assertEqual({'Bulgaria': 2500}, self.trip.booked_destinations_paid_amounts)

    def test_book_a_trip_with_family_discount(self):
        self.trip.budget = 3000
        self.trip.travelers = 5
        self.trip.is_family = True
        # trip_praise:  3000 - (5 * 500) * 0.9 = 2250
        expected = f'Successfully booked destination Bulgaria! Your budget left is 750.00'
        result = self.trip.book_a_trip("Bulgaria")
        self.assertEqual(expected, result)
        self.assertEqual({'Bulgaria': 2250}, self.trip.booked_destinations_paid_amounts)

    def test_booking_status_if_no_destinations_booked(self):
        expected = "No bookings yet. Budget: 50.00"
        self.assertEqual(expected, self.trip.booking_status())

    def test_booking_status_if_destination_already_booked(self):
        self.trip.budget = 10000
        self.trip.travelers = 1

        self.trip.book_a_trip("New Zealand")
        self.trip.book_a_trip("Bulgaria")

        expected = "Booked Destination: Bulgaria\n" \
                   "Paid Amount: 500.00\n" \
                   "Booked Destination: New Zealand\n" \
                   "Paid Amount: 7500.00\n" \
                   "Number of Travelers: 1\n" \
                   "Budget Left: 2000.00"

        self.assertEqual(expected, self.trip.booking_status())


if __name__ == "__main__":
    main()
