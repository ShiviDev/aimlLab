import numpy as np
import pandas as pd
import math

class node:
    def __init__(self, label):
        self.label=label
        self.branch={}

def entropy(data):
    total_ex=len(data)
    p_ex=len(data.loc[data['PlayTennis']=='Yes'])
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
    root=node("null")
    if entropy(data)==0:
        # ahh, i think here issue
        # 5         Cool   Normal         No
        # 13        Mild     High         No
        # these two cases ge, but i have else statement na, ha but while indexin here, its throwin error cos we aint able to find ig T_Thuh
        if len(data.loc[data[data.columns[-1]]=="Yes"])==len(data):
            root.label='Yes'
        else:
            root.label='No'
    if len(data.columns)==1:
        return
    else:
        attr=get_attr(data)
        root.label=attr
        values=set(data[attr])
        for value in values:
            print("key value ->",data[attr]==value)#see full desicion_tree function once, if everything correct anthaha
            temp_value = data.loc[data[attr]==value].drop(attr,axis=1)
            print("tempvalue ->",temp_value)
            root.branch[value]=decision_tree(temp_value) # i think here only mostlty errbut what T_T, bari empty string '' was passed as key
        return root

def get_rules(root, rule, rules):
    if not root.branch:
        rules.append(rule[:-1]+"=>"+root.label)
        return rules
    for val in root.branch:
        # print(val)
        get_rules(root.branch[val], rule+root.label+"="+str(val)+"^", rules)
    return rules

def test(tree, test_str):
    if not tree.branch:
        return tree.label
    return test(tree.branch[str(test_str[tree.label])], test_str)

data = pd.read_csv("tennis.csv")
tree = decision_tree(data)
rules = get_rules(tree," ",[])
# for rule in rules:
    # print(rule)
test_str = {}
print("Enter the test case input: ")
for attr in data.columns[:-1]:
    test_str[attr] = input(attr+": ")
print(test_str)
print(test(tree, test_str))