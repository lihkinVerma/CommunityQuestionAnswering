
import os
import json
import glob as g
from Constants import CqaConstants
from collections import defaultdict

class QueryDataset:
    def __init__(self):
        pass

    def findDuplicateDocumentsInEachDirectory(self):
        pathToDataset = CqaConstants.pathToDataset
        pwd = os.getcwd()
        OverallPath = pwd + '/' + pathToDataset
        os.chdir(OverallPath)
        listOfDirectories = os.listdir()
        presentPath = os.getcwd()
        directoryToDocumentDict = defaultdict(list)
        overallDocumentsInDirectory = defaultdict(list)
        for directory in listOfDirectories:
            try:
                os.chdir(os.path.join(presentPath, directory))
                lof = g.glob('*.json')
                overallDocumentsInDirectory[directory] = lof
                for file in lof:
                    src, dup = None, None
                    with open(file, 'r') as f:
                        src, dup = f.readline(), f.readline()
                        src, dup = json.loads(src), json.loads(dup)
                    if dup.get('novelty') is False:
                        directoryToDocumentDict[directory].append(file)
                os.chdir(presentPath)
            except Exception as e:
                print("came here for " + directory)
        return directoryToDocumentDict, overallDocumentsInDirectory
