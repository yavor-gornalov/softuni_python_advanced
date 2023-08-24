from abc import ABC, abstractmethod


class BaseWorker(ABC):
    @staticmethod
    @abstractmethod
    def work():
        pass


class Manager:

    def __init__(self):
        self.worker = None

    def set_worker(self, worker: BaseWorker):
        if not isinstance(worker, BaseWorker):
            raise AssertionError(f"`worker` must be of type {self.__class__.__name__}")
        self.worker = worker

    def manage(self):
        self.worker.work()


class Worker(BaseWorker):
    @staticmethod
    def work():
        print("I'm working!!")


class SuperWorker(BaseWorker):
    @staticmethod
    def work():
        print("I work very hard!!!")


worker = Worker()
manager = Manager()
manager.set_worker(worker)
manager.manage()
super_worker = SuperWorker()
try:
    manager.set_worker(super_worker)
    manager.manage()
except AssertionError:
    print("manager fails to support super_worker....")
