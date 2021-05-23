
#---------------------------------------------------------------------------------------------------
# Textual Novelty Detection project for Community Question Answering (CQA)
# Motive - Research
# Research Question - The distinction between related and duplicate questions is a great analogue for novelty vs. redundancy
# Developer - Nikhil Verma, Master of Science in Applied Computing at University of Toronto 2021-22
#---------------------------------------------------------------------------------------------------

import pandas as pd
from QueryDataset import QueryDataset

if __name__ == '__main__':
    queryDataset = QueryDataset.QueryDataset()
    duplicates, overallDocs = queryDataset.findDuplicateDocumentsInEachDirectory()
    countDf = pd.DataFrame(columns = ['QATitle', 'OverallCount', 'duplicateCount'], index = range(len(overallDocs)))
    for id, (k, v) in enumerate(overallDocs.items()):
        countDf.loc[id] = [k, len(v), len(duplicates[k])]
    countDf = countDf.replace(0, 1)
    countDf['%OfDuplicatesInData'] = countDf['duplicateCount'] / countDf['OverallCount'] * 100
    print(countDf)
