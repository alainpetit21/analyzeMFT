import pandas


class ControllerLogicTest:

    def __init__(self, strInputProcessedFile: str):
        self.dfMFT = pandas.read_csv(strInputProcessedFile)

    def do(self):
        print(self.dfMFT)
        print(list(self.dfMFT))
