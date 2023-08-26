from abc import ABC, abstractmethod
import time


class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass


class Workable(ABC):
    @abstractmethod
    def work(self):
        pass


class AbstractWorker(ABC):
    pass


class Worker(AbstractWorker, Workable, Eatable):

    def work(self):
        print("I'm normal worker. I'm working.")

    def eat(self):
        print("Lunch break....(5 secs)")
        time.sleep(5)


class SuperWorker(AbstractWorker, Workable, Eatable):

    def work(self):
        print("I'm super worker. I work very hard!")

    def eat(self):
        print("Lunch break....(3 secs)")
        time.sleep(3)


class Robot(AbstractWorker, Workable):

    def work(self):
        print("I'm a robot. I'm working....")


class Manager:

    def __init__(self):
        self.worker = None

    def set_worker(self, worker: AbstractWorker):
        if not isinstance(worker, AbstractWorker):
            raise AssertionError(f"`worker` must be of type AbstractWorker")
        self.worker = worker

    def manage(self):
        self.worker.work()

    def lunch_break(self):
        self.worker.eat()


manager = Manager()
manager.set_worker(Worker())
manager.manage()
manager.lunch_break()

manager.set_worker(SuperWorker())
manager.manage()
manager.lunch_break()

manager.set_worker(Robot())
manager.manage()
try:
    manager.lunch_break()
except AttributeError:
    pass
