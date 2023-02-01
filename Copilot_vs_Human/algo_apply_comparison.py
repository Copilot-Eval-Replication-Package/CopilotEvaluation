import ast
import re
import os
from python_comparison import get_significant_subtrees, compare_subtrees
import pandas as pd
DATASET = "CoPilot_on_Algorithm_Design"
GP_algo = "Sorting_Algorithms"

   


def paths_list(dir_path):
    path_list = []
    for file_name in os.listdir(dir_path):
        code_path = dir_path + "/" + file_name
        path_list.append(code_path)
    
    return path_list



algo_name =[ "Bubble_Sort", "Insertion_Sort", "Selection_Sort", "Merge_Sort", "Quick_Sort", "Heap_Sort","Bucket_Sort","Radix_Sort"]
for algo in algo_name:
    CODE_DIR = os.path.join(
        os.getcwd(),
        DATASET,GP_algo, algo,
        "",
        )
    correct_path= os.path.join(CODE_DIR,'Correct')
    output_path = os.path.join(CODE_DIR,'simiparity_comparison.csv')
    similarity_result = pd.DataFrame(columns=['file_1','file_2','similarity'])
    path_list = []
    path_list = paths_list(correct_path)
    for code_path in path_list:
        with open (code_path , "r") as source :
            file_name_1 = code_path.split("/")[-1]
            print("file_1: ",file_name_1)
            t1str = source . read ()
            t1str_mod = re.sub(r'(\"{2,3}[\s\n]*)(?:.*?[\s\n]*)*([\n\s]*\"{2,3})', r'', t1str, flags=re.MULTILINE)
            tree1 = ast . parse ( t1str_mod , mode ="exec")
        
        subtree_list1 = get_significant_subtrees ( tree1 )

       
        for comp_path in path_list:
            with open (comp_path , "r") as source :
                file_name_2 = comp_path.split("/")[-1]
                print("file_2: ",file_name_2)
                t2str = source . read ()
                t1str_mod = re.sub(r'(\"{2,3}[\s\n]*)(?:.*?[\s\n]*)*([\n\s]*\"{2,3})', r'', t1str, flags=re.MULTILINE)
                tree2 = ast . parse ( t2str , mode ="exec")
        

            subtree_list2 = get_significant_subtrees ( tree2 )
            similarity = compare_subtrees ( subtree_list1 , subtree_list2 , 10000) [0]

            similarity_result = similarity_result.append({'file_1':file_name_1
                                                  ,'file_2': file_name_2,
                                                  'similarity':similarity},ignore_index=True)

    similarity_result.to_csv(output_path, index=None, header=True)     
                