import json
import pandas as pd

data = {'Text Source': [],
        'Prop 65': [],
        'REACH': [],
        'ROHS': [],
        'Responsible Minerals': [],
        'SDS': [],
        'None': []
        }

df = pd.DataFrame(data, columns=['Text Source', 'Prop 65', 'REACH', 'ROHS', 'Responsible Minerals', 'SDS', 'None'])

with open('doc_class_output.manifest', 'r') as manifest:
    data = manifest.read().split('\n')
    for d in data:
        if d != "":
            input = json.loads(d)

            text = input['source']
            classifications = input['Document-Classification']

            p65 = 0
            reach = 0
            rohs = 0
            rm = 0
            sds = 0
            none = 0

            if 0 in classifications:
                p65 = 1
            if 1 in classifications:
                reach = 1
            if 2 in classifications:
                rohs = 1
            if 3 in classifications:
                rm = 1
            if 4 in classifications:
                sds = 1
            if 5 in classifications:
                none = 1

            df = df.append({'Text Source': text,
                            'Prop 65': p65,
                            'REACH': reach,
                            'ROHS': rohs,
                            'Responsible Minerals': rm,
                            'SDS': sds,
                            'None':  none
                            },
                           ignore_index=True)

df.to_csv("doc-class-output.csv", index=False)


