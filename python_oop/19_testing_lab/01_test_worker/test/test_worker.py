
from project.worker import Worker

from unittest import TestCase, main


class WorkerTests(TestCase):
    def setUp(self):
        self.worker = Worker("TestWorker", 100, 80)

    def test_worker_initialized_correctly(self):
        """
        Test if the worker is initialized with
        the correct name, salary, and energy
        """
        self.assertEqual("TestWorker", self.worker.name)
        self.assertEqual(100, self.worker.salary)
        self.assertEqual(80, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_worker_energy_incremented_after_rest(self):
        """
        Test if the worker's energy is incremented
        after the rest method is called
        """
        self.assertEqual(80, self.worker.energy)
        self.worker.rest()
        self.assertEqual(81, self.worker.energy)

    def test_worker_tries_to_work_without_energy(self):
        """
        Test if an error is raised if the worker
        tries to work with negative energy or equal to 0
        """
        self.worker.energy = 0
        with self.assertRaises(Exception) as ex:
            self.worker.work()

        expected = "Not enough energy."
        self.assertEqual(expected, str(ex.exception))

        self.worker.energy = -1
        with self.assertRaises(Exception) as ex:
            self.worker.work()

        expected = "Not enough energy."
        self.assertEqual(expected, str(ex.exception))

    def test_worker_money_increased_after_work(self):
        """
        Test if the worker's money is increased
        by his salary correctly after the work method is called
        """
        self.assertEqual(0, self.worker.money)
        self.worker.work()
        self.worker.work()
        self.assertEqual(2 * self.worker.salary, self.worker.money)

    def test_worker_energy_decreased_after_work(self):
        """
        Test if the worker's energy is decreased
        after the work method is called
        """
        self.worker.energy = 1
        self.worker.work()
        self.assertEqual(0, self.worker.energy)
        with self.assertRaises(Exception):
            self.worker.work()

    def test_worker_get_info_method(self):
        """
        Test if the get_info method returns
        the proper string with correct values
        """
        self.worker.work()
        self.worker.work()
        expected = f"TestWorker has saved {2 * self.worker.salary} money."
        self.assertEqual(expected, self.worker.get_info())


if __name__ == "__main__":
    main()
