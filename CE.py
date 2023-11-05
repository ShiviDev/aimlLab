import pandas as pd
import numpy as np

data = pd.read_csv('Training_examples.csv')
concept = np.array(data)[1:,1:-1]
print('learning concept is')
print(concept)

target= np.array(data)[1:,-1]
print('target')
print(target)

def learn(concept, target):
    specific_h=concept[0].copy()
    general_h=[['?' for i in range(len(specific_h))] for i in range(len(specific_h))]
    
    for i,h in enumerate(concept):
        if target[i]=='Yes':
            for j in range(len(specific_h)):
                if h[j]!=specific_h[j]:
                    specific_h[j]='?'
                    general_h[j][j]='?'
        elif target[i]=='No':
            for j in range(len(specific_h)):
                if h[j]!=specific_h[j]:
                    general_h[j][j]=specific_h[j]
                