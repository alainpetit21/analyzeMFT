from Controller.ControllerLogicTest import ControllerLogicTest
from analyzemft import mftsession
import os


if __name__ == "__main__":
    strFileMFT = "./data/mft.raw"
    strFileProcessed = "./data/mft.raw.out.csv"

    if not os.path.exists(strFileProcessed):
        session = mftsession.MftSession()
        session.mft_options(["-f", strFileMFT, "-o", strFileProcessed])
        session.open_files()
        session.process_mft_file()

    objScript = ControllerLogicTest(strFileProcessed)
    objScript.do()
