import os
from nltk.translate.bleu_score import sentence_bleu
import pandas as pd
correct_path = "../refactory/data/question_3/code/correct"
wrong_path = "../refactory/data/question_3/code/copilot_top10/wrong"
out_path = r"../refactory/data/question_3/BLEU_score_wrong_2.csv"

bleu_result = pd.DataFrame(columns=['wr_q_id','BLEU_score'])

def paths_list(dir_path):
    path_list = []
    for file_name in os.listdir(dir_path):
        code_path = dir_path  +"/" + file_name
        path_list.append(code_path)
    
    return path_list
    
ref_list = []
ref_list = paths_list(correct_path)

wrong_list = []
wrong_list = paths_list(wrong_path)

reference_code=[]
for code_path in ref_list:
    with open(code_path, "r") as f:
        code = f.read()
        reference_code.append(code.split())


for code_path in wrong_list:
    with open(code_path, "r") as f:
        file_name = code_path.split("/")[-1]
        print(file_name)
        code = f.read()
        split_code_2= code.split()


    blue_score= sentence_bleu(reference_code, split_code_2)
    print(blue_score)
    bleu_result = bleu_result.append({'wr_q_id':file_name ,'BLEU_score': blue_score},ignore_index=True)

    bleu_result.to_csv(out_path, index=None, header=True) 
    print(bleu_result)