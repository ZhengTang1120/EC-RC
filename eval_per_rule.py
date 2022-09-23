import json
import scorer
from collections import defaultdict
import random
import operator
p=0
n=0
ds = list()
golds = list()
predictions = dict()
predictions_first = list()
rules = defaultdict(dict)
j = json.load(open('src/main/resources/data/dev.json'))
# t = open('/Users/zheng/Downloads/CoreNLP-dc9ccccbe28091aa915887c6bec611559d4d29d2/t_train/output.txt').readlines()
# # o = json.load(open('output_02_dev_best_model.json'))
# tagging = open('tagging_dev.txt').readlines()
# train_rule = open('dev_new_chunk_pruned.txt').readlines()
# dev_m = open('dev_new_chunk_pruned.txt').readlines()

# top_dev = ["t_4592", "t_4653", "org:top_members/employees_2", "org:city_of_headquarters_1", "t_3914", "per:employee_of_2", "t_530", "t_590", "t_123", "per:date_of_death_1", "per:city_of_death_1", "t_1063"]
# top_train = ["t_1155", "t_4592", "t_3914", "t_4123", "t_10", "t_744", "t_530", "t_1063", "t_123", "t_590", "t_3471", "t_4748", "t_4653", "t_4445", "t_3935", "t_4543", "t_4678", "t_680", "t_664"]

# train = {'per:employee_of': ['t_1155', 't_1154', 't_1441', 't_1464', 't_1444', 't_1440', 't_1236', 't_2443', 't_1438', 't_1456', 't_1891', 't_1443', 't_2460', 't_2448', 't_1276', 't_1471', 't_1532', 't_2199', 't_1465', 't_2001', 't_1244', 't_2449', 't_1237', 't_1194', 'per:employee_of_2', 'per:employee_of_1', 't_1266', 'per:employee_of_3', 't_1649', 'per:employee_of_4', 't_1238', 't_2512', 't_1619', 't_1452', 't_1484', 't_2455', 't_2474', 't_1457', 't_1239', 't_2444', 't_1448', 't_1439', 't_2477', 't_2476', 't_2445', 't_2452', 't_2446', 't_1180', 't_2551'], 'per:title': ['t_4592', 't_4601', 't_4609', 't_4602', 't_4603', 't_4605', 't_4610', 'per:title_1', 'per:title_2', 'per:title_3', 't_4598'], 'org:website': ['t_3914', 't_3917'], 'org:top_members/employees': ['t_4123', 't_4194', 't_4122', 't_4053', 't_4050', 't_4124', 't_4128', 't_4099', 't_4125', 't_4195', 't_4052', 't_4098', 't_4044', 't_4201', 't_4126', 't_4207', 't_4051', 't_4073', 't_4198', 't_4127', 't_4197', 't_4294', 't_4135', 't_4210', 't_4105', 't_4200', 't_4071', 't_4048', 't_4108', 't_4139', 't_4080', 't_4100', 'org:top_members/employees_2', 'org:top_members/employees_1', 't_4070', 'org:top_members/employees_3', 't_4208', 't_4131', 't_4147', 't_4219', 't_4206', 't_4054', 't_4212', 't_4144', 't_4148', 't_4129', 't_4072', 't_4082', 't_4199', 't_4213', 't_4046', 't_4157'], 'org:city_of_headquarters': ['t_10', 't_1', 't_43', 't_6', 't_9', 't_12', 't_7', 't_20', 'org:city_of_headquarters_1', 't_11'], 'org:stateorprovince_of_headquarters': ['t_744', 't_734', 't_737', 't_735', 't_836', 't_743', 't_777', 'org:stateorprovince_of_headquarters_1', 't_745', 't_835'], 'org:alternate_names': ['t_530', 't_534', 't_541', 't_531'], 'per:spouse': ['t_1063', 't_1070', 't_896', 't_1069', 't_897', 't_1062', 't_1074', 't_1059', 'per:spouse_2', 'per:spouse_1', 't_899', 'per:spouse_3_reverse', 'per:spouse_3', 't_1060', 'per:spouse_1_reverse'], 'org:country_of_headquarters': ['t_123', 't_134', 't_132', 't_133', 't_129', 't_131', 't_165', 'org:country_of_headquarters_1', 't_224', 'org:country_of_headquarters_3', 'org:country_of_headquarters_2', 't_128'], 'per:age': ['t_590', 't_591', 't_619', 't_618', 't_596', 't_593'], 'per:stateorprovince_of_birth': ['t_4005'], 'per:date_of_death': ['t_4579', 't_4587', 't_4570', 't_4580', 'per:date_of_death_1', 'per:date_of_death_3'], 'per:children': ['t_3802', 't_3804', 't_3807', 't_3899', 't_3801', 't_3895', 't_3805', 'per:children_3_1', 'per:children_1', 't_3820', 'per:children_3_2'], 'org:parents': ['t_3471', 't_3496', 't_3514', 't_3469'], 'per:schools_attended': ['t_265', 't_245', 't_246', 't_278', 't_268', 't_279', 't_267'], 'per:countries_of_residence': ['t_4748', 't_4755'], 'per:origin': ['t_4653', 't_4656', 't_4652', 't_4658', 'per:origin_1_n', 'per:origin_4_n', 't_4663'], 'per:siblings': ['t_368', 't_366', 't_367', 't_362', 't_373', 't_370'], 'per:other_family': ['t_3579', 't_3594', 't_3557'], 'per:parents': ['t_4445', 't_4444', 't_4446', 't_4418', 't_4439', 't_4447', 't_4437', 't_4407', 't_4443', 't_4528', 't_4410', 't_4537'], 'per:cities_of_residence': ['t_3935', 't_3954', 't_3973', 't_3936', 't_3942', 't_3940', 't_3950', 't_3961'], 'org:founded_by': ['t_451', 't_450', 'org:founded_by_1', 'org:founded_by_2', 't_457', 't_446', 't_449'], 'per:cause_of_death': ['t_4543', 't_4545', 't_4548'], 'per:date_of_birth': ['t_462', 't_465', 't_463', 't_461', 't_464'], 'per:stateorprovince_of_death': ['per:stateorprovince_of_death_1', 'per:stateorprovince_of_death_1_extend'], 'per:stateorprovinces_of_residence': ['t_4678', 't_4679', 't_4681'], 'org:subsidiaries': ['t_680', 't_678', 't_685', 't_684', 't_703', 't_705'], 'per:city_of_death': ['t_4350', 'per:city_of_death_1'], 'per:city_of_birth': ['t_664', 't_672', 't_675'], 'org:member_of': ['t_3467', 't_3459'], 'per:religion': ['t_483', 'per:religion_2', 't_472', 't_482'], 'per:charges': ['t_521', 't_490', 't_495', 't_487', 't_524', 't_494', 't_511'], 'per:alternate_names': ['t_655', 't_625', 't_636', 't_642'], 'org:number_of_employees/members': ['t_4379', 't_4399', 't_4389'], 'per:member_of': ['t_3517', 't_3524', 't_3526'], 'org:shareholders': ['t_4319'], 'org:founded': ['t_729'], 'org:political/religious_affiliation': ['t_3775', 't_3778'], 'org:dissolved': ['t_1099'], 'org:members': ['t_4624']}
# dev = {'per:title': ['t_4592', 't_4601', 't_4603', 't_4609', 't_4602', 'per:title_3', 'per:title_2', 'per:title_1', 't_4598'], 'per:origin': ['t_4653', 't_4656', 't_4652', 't_4663', 't_4658', 'per:origin_1_n'], 'org:top_members/employees': ['t_4123', 't_4125', 't_4122', 't_4124', 't_4194', 't_4201', 't_4197', 't_4050', 't_4141', 't_4100', 't_4127', 't_4133', 't_4044', 't_4195', 't_4126', 't_4098', 't_4199', 't_4202', 't_4053', 't_4196', 't_4074', 't_4052', 't_4146', 't_4212', 'org:top_members/employees_2', 't_4073', 'org:top_members/employees_3', 't_4102', 't_4099', 'org:top_members/employees_1', 't_4298', 't_4131', 't_4221', 't_4072', 't_4276', 't_4138', 't_4134', 't_4079', 't_4136', 't_4294', 't_4105'], 'org:city_of_headquarters': ['t_10', 't_9', 't_43', 't_7', 't_1', 'org:city_of_headquarters_1', 't_40', 't_12', 't_6'], 'per:city_of_birth': ['t_664', 't_672'], 'org:website': ['t_3914'], 'org:subsidiaries': ['t_703', 't_713', 't_704', 't_715', 't_682'], 'per:employee_of': ['t_1201', 't_1602', 't_1239', 't_1452', 'per:employee_of_1', 'per:employee_of_2', 't_1440', 'per:employee_of_4', 't_1154', 't_2450', 'per:employee_of_3', 't_1451', 't_2391', 't_1438', 't_1180', 't_2445', 't_1238', 't_2460', 't_1189'], 'org:alternate_names': ['t_530', 't_534'], 'per:country_of_death': ['t_883', 'per:country_of_death_1', 't_870'], 'per:cause_of_death': ['t_4543', 't_4540', 't_4545', 't_4550', 't_4548'], 'per:children': ['t_3802', 't_3801', 'per:children_1', 'per:children_3_1', 't_3791', 't_3805', 't_3807', 't_3804', 't_3785', 't_3895', 't_3812'], 'per:cities_of_residence': ['t_3935', 't_3964', 't_3954', 't_3945', 't_3938'], 'per:stateorprovince_of_birth': ['t_4005'], 'per:age': ['t_590', 't_591', 't_596', 't_593', 't_612', 't_619'], 'org:stateorprovince_of_headquarters': ['t_744', 't_836', 't_743', 't_734', 't_737', 't_777', 't_735', 't_746', 'org:stateorprovince_of_headquarters_1'], 'org:country_of_headquarters': ['t_123', 't_134', 't_131', 't_132', 't_133', 'org:country_of_headquarters_1', 't_129', 't_224', 't_130', 't_162'], 'per:date_of_death': ['t_4571', 't_4579', 't_4587', 'per:date_of_death_1', 't_4580', 't_4589'], 'per:city_of_death': ['t_4338', 'per:city_of_death_1', 't_4351', 't_4350'], 'per:spouse': ['t_1063', 't_1074', 'per:spouse_1_reverse', 't_899', 'per:spouse_3_reverse', 'per:spouse_1', 't_1069', 'per:spouse_3', 't_1062'], 'per:date_of_birth': ['t_465', 't_462'], 'per:stateorprovince_of_death': ['t_582', 'per:stateorprovince_of_death_1', 'per:stateorprovince_of_death_1_extend', 't_583'], 'per:siblings': ['t_366'], 'per:countries_of_residence': ['t_4767', 't_4793', 't_4758', 't_4786', 't_4800'], 'org:parents': ['t_3471', 't_3474', 't_3486'], 'org:founded_by': ['t_446', 't_453', 'org:founded_by_3', 'org:founded_by_1'], 'per:stateorprovinces_of_residence': ['t_4679', 't_4678'], 'per:alternate_names': ['t_625'], 'per:charges': ['t_521', 't_491', 't_493', 't_487', 't_496', 't_515', 't_520', 't_497', 't_498'], 'org:number_of_employees/members': ['t_4402', 't_4389', 't_4379'], 'per:parents': ['t_4418', 't_4445', 't_4444', 't_4438', 't_4446', 't_4436', 't_4437'], 'per:religion': ['t_483'], 'per:schools_attended': ['t_245'], 'org:shareholders': ['t_4319'], 'org:political/religious_affiliation': ['t_3777'], 'per:member_of': ['t_3517', 't_3524'], 'per:other_family': ['t_3596']}


# top1 = []
# top5 = []
# top10 = []

# for l in train:
#   top1 += train[l]

# top = [i for i in top1 if ':' not in i]

# pruned = open('train_new.txt').readlines()
rm = json.load(open('relation_mapping.json'))
for i, item in enumerate(open('dev_exp1r.txt')):
    item = item.strip()
    # item2 = train_rule[i].strip()
    label = j[i]['relation']
    # label = rm[label] if label in rm else label
    golds.append(label)
    # if item.split('|')[0].split('\t')[-1] in top:
    #   print (tagging[i].strip())
    # elif t[i].strip() != 'no_relation' and eval(t[i].strip())[0][-1] in top:
    #   print (tagging[i].strip())
    # else:
    #   print ("no_relation\t[]")

#     td_rules)
    # p = item.split('\t')[0] #if item.split('|')[0].split('\t')[-1] in top else 'no_relation'
    # if p not in ['per:employee_of', 'per:countries_of_residence', 'per:cities_of_residence', 'per:cause_of_death', 'per:charges']:
    # if t[i].strip() != 'no_relation':
    #     p = eval(t[i].strip())[0][0]
    # else:
    #     p = 'no_relation'
#     # r = item.split('|')[0].split('\t')[-1] if item.split('|')[0].split('\t')[-1] in top else 'no_relation'
#     # if p != 'no_relation' and o[i]['gold_tags'] == []:
#     #   tr = (eval(item.split('|')[0].split('\t')[1])[0], eval(item.split('|')[0].split('\t')[1])[1]-1)
#     #   o[i]['gold_tags'] = [1 if x-1 in tr else 0 for x in range(len(o[i]['raw_words']))]
    # if p == 'no_relation':
    #     p = item.split('\t')[0] #if eval(t[i].strip())[0][-1] in top else 'no_relation'
    # if p == 'no_relation':
    #     p = item2.split('\t')[0]
#     #     r = eval(t[i].strip())[0][-1] if eval(t[i].strip())[0][-1] in top else 'no_relation'

# #     if p == label and r in top[:250]:
# #         print (i, ',')
    # p = o[i]['predicted_label']
    # p = rm[p] if p in rm else p
    # predictions_first.append(p)
    for d in item.split('|'):
        d = d.split('\t')
        rule = d[-1]
        if rule+"|"+d[0] not in predictions:
            predictions[rule+"|"+d[0]] = ['no_relation' for x in range(len(j))]
        predictions[rule+"|"+d[0]][i] = d[0]
rules = predictions.keys()
rules.sort()
r = defaultdict(dict)
for rule in rules:
    print (rule)
    prec, recall, f1 = scorer.score_per_label(golds, predictions[rule], rule.split('|')[-1])
    print 
    if prec>=0.6:
      x, y = rule.split('|')
      l = x.split('_')
      if l[-1].isdigit() and l[-2].isdigit():
        if l[-2] in r[y]:
          r[y][l[-2]].append(int(l[-1]))
        else:
          r[y][l[-2]] = [int(l[-1])]
for l in r:
  for i in r[l]:
    r[l][i].sort()
print (json.dumps(r))
# # for i, item in enumerate(open('tagging_train_250.txt')):
# #     golds.append(j[i]['relation'])
# #     predictions_first.append(item.split('\t')[0])

# print (scorer.score(golds, predictions_first, verbose=True))

