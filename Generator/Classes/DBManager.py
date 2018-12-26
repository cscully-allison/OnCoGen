from abc import ABC

DBIntializerInterface(ABC):
    @abstractmethod
    def CreateInitFile(self):
        pass

    @abstractmethod
    def OutputInitFile(self):
        pass

    @abstractmethod
    def CreateTables(self):
        pass

    @abstractmethod
    def FormatTable(self, TableInfo):
        pass

    @abstractmethod
    def OutputBuldTableFile(self):
        pass
