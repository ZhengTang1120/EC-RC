import json
from collections import Counter, defaultdict
from termcolor import colored

model_output = json.load(open('../tacred_tagging/output_bs0ndr_train_best_model_7.json'))

mr = open("../tacred_tagging/dataset/tacred/tagging_rbs0_train.txt").readlines()

j = json.load(open('/home/zheng/Documents/research/tacred_odin/src/main/resources/data/train.json'))

rule_outputs = open("../tacred_odin/train_exp1rf.txt").readlines()

triggers = json.load(open('triggers.json'))

def filter(trigger, ss, se, os, oe, tokens, trigger_words):
    res = [i for i in trigger if i not in range(ss, se+1) and i not in range(os, oe+1) and tokens[i] in trigger_words]
    return res

""" Generate tagging from model output """    
# for i, item in enumerate(model_output):
#     if item['from_prev']:
#         print (item['predicted_label']+"\t"+str(item["gold_tags"]))
#     elif item["predicted_label"]!="no_relation":
#         print (item['predicted_label']+"\t"+str(item["predicted_tags"]))
#     else:
#         print ("no_relation\t[]")
# exit()
""" Count the newly added instances """        
x = defaultdict(list)
n = 0
na = 0
nb = 0
for i, item in enumerate(model_output):
    ss = j[i]['subj_start']
    se = j[i]['subj_end']
    os = j[i]['obj_start']
    oe = j[i]['obj_end']
    p = Counter()
    t = dict()
    for a in rule_outputs[i].strip().split('|'):
        rl = a.split('\t')[0]
        masked = eval(a.split('\t')[1])
        if rl != 'no_relation':
            t[rl] = [k for k in range(masked[0], masked[1]) if k not in range(ss, se+1) and k not in range(os, oe+1)]
        p.update({rl:1})

    if p.most_common(1)[0][0] == 'no_relation' and len(p)!=1:
        predicted_label = p.most_common(2)[1][0]
    else:
        predicted_label = p.most_common(1)[0][0]

    predicted_tags = t.get(predicted_label, [])
    # if predicted_label != "no_relation":
    #     n += 1
    #     if 'no_relation' in mr[i]:
    #         na += 1
    if predicted_label != item['predicted_label'] and 'no_relation' in mr[i]:
        if predicted_label == "no_relation":
            na += 1
        if item['predicted_label'] == "no_relation":
            nb += 1
        n += 1
print (n, na ,nb)
exit()
""" Generate tagging from rule output """    
for i, item in enumerate(model_output):
    
    ss = j[i]['subj_start']
    se = j[i]['subj_end']
    os = j[i]['obj_start']
    oe = j[i]['obj_end']
    p = Counter()
    t = dict()
    for a in rule_outputs[i].strip().split('|'):
        rl = a.split('\t')[0]
        masked = eval(a.split('\t')[1])
        if rl != 'no_relation':
            trigger_words = triggers[a.split('\t')[2]].split('"')
            temp = [k for k in range(masked[0], masked[1])]
            temp = filter(temp, ss, se, os, oe, j[i]['token'], trigger_words)
            if rl not in t:
                t[rl] = temp
            elif len(t[rl]) > len(temp):
                t[rl] = temp
        p.update({rl:1})

    if p.most_common(1)[0][0] == 'no_relation' and len(p)!=1:
        predicted_label = p.most_common(2)[1][0]
    else:
        predicted_label = p.most_common(1)[0][0]

    predicted_tags = t.get(predicted_label, [])

    if item['from_prev']:
        print (item['predicted_label']+"\t"+str(item["gold_tags"]))
    elif predicted_label!="no_relation":
        print (predicted_label+"\t"+str(predicted_tags))
    else:
        print ("no_relation\t[]")

