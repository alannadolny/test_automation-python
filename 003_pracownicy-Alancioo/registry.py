import seller
import physical_worker
import office_worker
import exceptions


class Registry:
    def __init__(self):
        self.workers = []

    def addWorker(self, worker):
        if isinstance(worker, (seller.Seller, physical_worker.PhysicalWorker, office_worker.OfficeWorker)):
            self.workers.append(worker)
            return self.workers
        else:
            raise exceptions.InappropriateWorkerType

    def deleteWorker(self, workerId):
        self.workers = list(filter(lambda worker: worker.workerId != workerId, self.workers))
        return self.workers

    def addManyWorkers(self, workersList):
        if all(isinstance(worker, (seller.Seller, physical_worker.PhysicalWorker, office_worker.OfficeWorker)) for
               worker in workersList):
            self.workers += workersList
            return self.workers
        else:
            raise exceptions.InappropriateWorkerTypeInList

    def getSortedWorkers(self):
        if len(self.workers) == 0:
            return "Lack of employees"
        else:
            sortedWorkers = sorted(
                sorted(sorted(self.workers, key=lambda worker: worker.lastName), key=lambda worker: worker.age),
                key=lambda worker: worker.experience, reverse=True)
            workerList = list(map(lambda worker: f"{worker.firstName} {worker.lastName}", sortedWorkers))
            return workerList

    def getWorkersByCity(self, city):
        workersList = list(filter(lambda worker: worker.companyAddress.city == city, self.workers))
        if not workersList:
            return "No employee works in this city"
        else:
            return list(map(lambda worker: f"{worker.firstName} {worker.lastName}", workersList))

    def getWorkersWithValue(self):
        def values(worker):
            if isinstance(worker, office_worker.OfficeWorker):
                return f"{worker.firstName} {worker.lastName}, value: {worker.experience * worker.iq}"
            if isinstance(worker, physical_worker.PhysicalWorker):
                return f"{worker.firstName} {worker.lastName}, value: {worker.experience * (worker.strength / worker.age)}"
            if isinstance(worker, seller.Seller):
                match worker.effectiveness:
                    case 'low':
                        effectivenessValue = 60
                    case 'mid':
                        effectivenessValue = 90
                    case 'high':
                        effectivenessValue = 120

                return f"{worker.firstName} {worker.lastName}, value: {worker.experience * effectivenessValue}"

        workersWithValue = list(map(lambda worker: values(worker), self.workers))
        return workersWithValue
