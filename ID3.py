import numpy as np
import pandas as pd
import math

class node:
    def __init__(self, label):
        self.label=label
        self.branch={}

def entropy(data):
    total_ex=len(data)
    p_ex=len(data.loc(data['PlayTennis']=='Yes'))
    n_ex=total_ex-p_ex
    en=0
    if(p_ex>0):
        en=-(p_ex/float(total_ex))*(math.log(p_ex,2)-math.log(total_ex,2))
    if(n_ex>0):
        en+=-(n_ex/float(total_ex))*(math.log(n_ex,2)-math.log(total_ex,2))
    return en

def gain(data, attrib, en):
    values=set(data[attrib])
    gain=en
    for value in values:
        gain-=len(data.loc[data[attrib]==value])/float(len(data))*entropy(data.loc[data[attrib]==value])
    return gain

def get_attr(data):
    attrib=""
    en=entropy(data)
    maxgain=0
    for attr in data.columns[:len(data.columns)-1]:
        g=gain(data, attr, en)
        if maxgain<g:
            maxgain=g
            attrib=attr
    return attrib

def decision_tree(data):
    