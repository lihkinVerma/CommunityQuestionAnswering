
import pickle
import torch
import torch.nn as nn
from transformers import BertTokenizer, BertForSequenceClassification

# Training

import torch.optim as optim

# Evaluation

from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import seaborn as sns

class BERT(nn.Module):
    def __init__(self):
        super(BERT, self).__init__()

        options_name = "bert-base-uncased"
        self.encoder = BertForSequenceClassification.from_pretrained(options_name)

    def forward(self, text, label):
        loss, text_fea = self.encoder(text, labels=label)[:2]

        return loss, text_fea

device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
print(device)

filename = 'testData.pickle'
with open(filename, 'rb') as f:
    data = pickle.load(f)

train_data = data.get('train_data')
