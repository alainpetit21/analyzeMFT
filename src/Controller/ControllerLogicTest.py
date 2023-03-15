import pandas as pd


class ControllerLogicTest:

    def __init__(self, strInputProcessedFile: str):
        self.dfMFT = pd.read_csv(strInputProcessedFile)
        self.dfTimeLineFormated = pd.DataFrame(columns=[])


    def do(self):
        print(self.dfMFT)
        print(list(self.dfMFT))


