import ast
import re
import os
from python_comparison import get_significant_subtrees, compare_subtrees
import pandas as pd
DATASET = "CoPilot_on_Algorithm_Design"
GP_algo = "Sorting_Algorithms"
cor_ratio_result = pd.DataFrame(columns=['algo','correct_ratio_t1','correct_ratio_t2'])
output_path = os.path.join(
        os.getcwd(),
        DATASET,GP_algo, "correct_ratio.csv"
        )  


def paths_list(dir_path):
    path_list = []
    for file_name in os.listdir(dir_path):
        code_path = dir_path + "/" + file_name
        path_list.append(code_path)
    
    return path_list


#for sorting algorithms
algo_name =[ "Bubble_Sort", "Insertion_Sort", "Selection_Sort", "Merge_Sort", "Quick_Sort", "Heap_Sort","Bucket_Sort","Radix_Sort"]
#For Gready algorithms
#algo_name=["Activity_Class", "Comparing_Activities","Set_of_activities"]
#algo_name=["Data_Structure", "Inorder_Walk","Min_Max_Values","Successor_Node"]
#algo_name=["BFS_Search", "DAG", "DFS_Search", "Data_Structure", "Strongly_Connected_Vetrices"]
for algo in algo_name:
    CODE_DIR = os.path.join(
        os.getcwd(),
        DATASET,GP_algo, algo,
        "",
        )
    correct_path= os.path.join(CODE_DIR,'Correct')
    wrong_path = os.path.join(CODE_DIR,'Wrong')

    num_list_cor_t1 = 0
    num_list_wrong_t1 = 0
    num_list_cor_t2 = 0
    num_list_wrong_t2 = 0
    
    correct_path_lst = []
    correct_path_lst = paths_list(correct_path)
    for code_path in correct_path_lst:
        with open (code_path , "r") as source :
            file_name = code_path.split("/")[-1]
            num_atempt = file_name.split("_")[1]
            if num_atempt in ["1","2","3"]:
                num_list_cor_t1 +=1
            else:
                num_list_cor_t2 +=1
    
    wrong_path_lst = []
    wrong_path_lst = paths_list(wrong_path)
    for code_path in wrong_path_lst:
        with open (code_path , "r") as source :
            file_name = code_path.split("/")[-1]
            num_atempt = file_name.split("_")[1]
            if num_atempt in ["1","2","3"]:
                num_list_wrong_t1 +=1
            else:
                num_list_wrong_t2 +=1

    #cor_ratio_t1= (num_list_cor_t1/(num_list_cor_t1+num_list_wrong_t1))*100
    #cor_ratio_t2= (num_list_cor_t2/(num_list_cor_t2+num_list_wrong_t2))*100

    cor_ratio_t1= (num_list_cor_t1/30)*100
    cor_ratio_t2= (num_list_cor_t2/30)*100

    cor_ratio_result = cor_ratio_result.append({'algo':algo
                                                  ,'correct_ratio_t1': cor_ratio_t1,
                                                  'correct_ratio_t2':cor_ratio_t2},ignore_index=True)

cor_ratio_result.to_csv(output_path, index=None, header=True)    