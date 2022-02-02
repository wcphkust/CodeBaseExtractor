import sys
from Extractor import *

if __name__ == "__main__":
    e = Extractor(sys.argv[1], sys.argv[2])
    e.extractSingleBase("PyGithub/PyGithub")

