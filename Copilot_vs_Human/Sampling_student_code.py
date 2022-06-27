import pandas as pd
import numpy as np

#change the question number in below path. Then it will be applied to the question. 
path = r'../refactory/data/question_1/summary_student.csv'
read_file = pd.read_csv (path)
sample_result = pd.DataFrame(columns=['rep_rate','avg_time','avg_rps'])

for i in range(1,11):
    sample_dt = read_file.sample(n=23, replace=True)
    #sample_dt.to_csv(r'C:/GH-Dataset/Copilot_Tester/refactory/data/question_1/sample_dt.csv', index=None, header=True)
    sample_dt_sc = sample_dt[sample_dt['Status'].str.contains('success')]

    if len(sample_dt_sc) == len(sample_dt):
        rep_rate= 1.00
    else:
        rep_rate = len(sample_dt_sc)/len(sample_dt)

    avg_time = sample_dt_sc['Total Time'].mean()
    avg_rps = sample_dt_sc['RPS'].mean()

    sample_result = sample_result.append({'rep_rate':rep_rate
                                                  ,'avg_time': avg_time,
                                                  'avg_rps':avg_rps},ignore_index=True)

sample_result.to_csv(path, index=None, header=True)                                                 
print(sample_result)
