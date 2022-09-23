import json

file = json.load(open('rules_exp1r.json'))
syntax = True
total = 0

high_prec = {"org:subsidiaries": {"0": [0, 2]}, "per:date_of_birth": {"0": [1, 2, 5, 6]}, "org:city_of_headquarters": {"0": [4, 5, 7, 10, 13, 20]}, "per:age": {"0": [1]}, "per:charges": {"0": [2, 4, 7, 9]}, "per:employee_of": {"0": [4, 5, 21, 27, 37, 38, 63, 71, 72, 75, 81, 87, 96, 113, 125, 129]}, "per:city_of_birth": {"0": [0, 2, 5, 7, 18]}, "per:children": {"0": [21, 23, 25, 28, 29, 48]}, "per:city_of_death": {"1": [23], "0": [0, 4, 12, 16, 23]}, "per:date_of_death": {"0": [2, 3, 4, 9, 10, 13, 16, 17, 22, 24, 25, 29]}, "per:schools_attended": {"0": [0]}, "org:alternate_names": {"0": [1, 2, 9, 11]}, "per:cause_of_death": {"0": [1, 6, 7, 8]}, "per:origin": {"0": [1, 2]}, "per:title": {"0": [0, 6, 7, 12, 17, 18, 19, 20, 21, 25, 29, 33, 42, 44, 45, 46, 50, 57, 62, 65, 76, 78, 82, 88, 89, 90, 91, 96, 97, 99, 103, 104, 107, 109, 110, 111, 113, 118, 119, 120, 121, 123, 124, 125, 127, 133, 134, 146, 149, 158, 165, 168, 169, 180, 189, 190, 201, 204, 208, 219, 220, 228, 249, 250, 253, 259, 260, 262, 264, 265, 266, 267, 270, 272, 275, 279, 287, 291, 298, 303, 306, 308, 309, 310, 311, 315, 317, 318, 320, 321, 328, 329, 330, 331, 333, 335, 339, 343, 345, 346, 353, 362, 363, 367, 377, 378, 390, 391, 395, 396, 399, 400, 403, 405]}, "org:country_of_headquarters": {"0": [2, 5, 8]}, "per:parents": {"0": [13, 29, 30, 34]}, "per:siblings": {"0": [2, 4]}, "org:stateorprovince_of_headquarters": {"0": [4]}, "per:spouse": {"0": [3, 7, 8, 11, 15, 18, 25, 27, 30, 34, 35, 39, 41, 42, 43, 49]}, "org:top_members/employees": {"0": [0, 2, 13, 15, 16, 20, 25, 27, 42, 44, 48, 54, 61, 62, 65, 67, 68, 75, 80, 85, 95, 96, 97, 99, 101, 105, 112, 114, 123, 125, 134, 149, 177, 181, 184, 189, 192, 193, 205, 227, 232]}, "org:founded_by": {"0": [0]}}

triggers = dict()
for relation in file:
    with open('%s_unit.yml'%relation, 'w') as f:
        count = 0
        for trigger in file[relation]:
            rules = [r for r in file[relation][trigger]]
            rl = relation.replace('_slash_', '/')
    
            for rule in rules:
                triggers['%s_0_%d'%(rl, count)] = trigger
                triggers['%s_1_%d'%(rl, count)] = trigger
                try:
                    if syntax and (high_prec is None or (rl in high_prec and count in high_prec[rl].get("0", []))):
                        f.write('''
- name: ${label}_${count}_%d
  label: ${label}
  priority: ${rulepriority}
  pattern: |
    trigger =  %s
    subject: ${subject_type} = %s
    object: ${object_type} = %s\n'''%(count, trigger, ' '.join(rule['subj']), ' '.join(rule['obj'])))
#                     elif syntax == False and (high_prec is None or (rl in high_prec and count in high_prec[rl].get("0", []))):
#                         f.write('''
# - name: ${label}_${count}_%d
#   label: ${label}
#   priority: ${rulepriority}
#   type: token
#   pattern: |
#     @object: ${object_type} (/.+/)*%s(/.+/)* @subject: ${subject_type}'''%(count, trigger))
                    total += 1
                except UnicodeEncodeError:
                    pass
                count += 1
print (json.dumps(triggers))