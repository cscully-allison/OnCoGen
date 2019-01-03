from abc import ABC

class DBIntializerInterface(ABC):
    @abstractmethod
    def DefineSchemaAsClass(self):
        pass

    @abstractmethod
    def CreateTables(self):
        pass

    @abstractmethod
    def FormatTable(self, TableInfo):
        pass
