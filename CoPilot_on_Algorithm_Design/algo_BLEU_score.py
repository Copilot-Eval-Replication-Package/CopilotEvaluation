import os
from nltk.translate.bleu_score import sentence_bleu
import pandas as pd

DATASET = "CoPilot_on_Algorithm_Design"
GP_algo = "Binary_Trees"
algo="Data_Structure"

CODE_DIR = os.path.join(
        os.getcwd(),
        DATASET,GP_algo, algo,
        "",
        )

ref_path = os.path.join(CODE_DIR,'ref_code.py')
solution_path = os.path.join(CODE_DIR,'PyScripts',"",)
out_path = os.path.join(CODE_DIR,'BLEU_score.csv')

bleu_result = pd.DataFrame(columns=['code_name','BLEU_score'])

def paths_list(dir_path):
    path_list = []
    for file_name in os.listdir(dir_path):
        code_path = dir_path  +"/" + file_name
        path_list.append(code_path)
    
    return path_list
    

solution_list = []
solution_list = paths_list(solution_path)

reference_code=[]
with open(ref_path, "r") as f:
    code = f.read()
    reference_code.append(code.split())


for code_path in solution_list:
    with open(code_path, "r") as f:
        file_name = code_path.split("/")[-1]
        print(file_name)
        code = f.read()
        split_code_2= code.split()


    blue_score= sentence_bleu(reference_code, split_code_2)
    print(blue_score)
    bleu_result = bleu_result.append({'code_name':file_name ,'BLEU_score': blue_score},ignore_index=True)

    bleu_result.to_csv(out_path, index=None, header=True) 
    print(bleu_result)