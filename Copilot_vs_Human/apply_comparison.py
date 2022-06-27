import ast
import re
import os
import shutil
from python_comparison import get_significant_subtrees, compare_subtrees
i=6
path = "../refactory/data/question_1/code/copilot_top10/"
#code_path = path  + "run" + str(i) + "/code"
code_path = path  +  "/correct"
com_path = path +"/comp_cor"
def paths_list(dir_path):
    path_list = []
    for file_name in os.listdir(dir_path):
        code_path = dir_path + "/" + file_name
        path_list.append(code_path)
    
    return path_list

path_list = []
path_list = paths_list(code_path)

for i in range(1,2):
    
    for code_path in path_list:
        with open (code_path , "r") as source :
            t1str = source . read ()
            t1str_mod = re.sub(r'(\"{2,3}[\s\n]*)(?:.*?[\s\n]*)*([\n\s]*\"{2,3})', r'', t1str, flags=re.MULTILINE)
            tree1 = ast . parse ( t1str_mod , mode ="exec")
        
        subtree_list1 = get_significant_subtrees ( tree1 )

        comp_path_list = paths_list(com_path)
        similarity =0
        for comp_path in comp_path_list:
            with open (comp_path , "r") as source :
                t2str = source . read ()
                t1str_mod = re.sub(r'(\"{2,3}[\s\n]*)(?:.*?[\s\n]*)*([\n\s]*\"{2,3})', r'', t1str, flags=re.MULTILINE)
                tree2 = ast . parse ( t2str , mode ="exec")
        

            subtree_list2 = get_significant_subtrees ( tree2 )
            similarity = compare_subtrees ( subtree_list1 , subtree_list2 , 10000) [0]
            print (f'The index of similarity between prog1  and prog2 is: { similarity }')
            if similarity ==1:
                break


        if similarity !=1: 
            shutil.copyfile(code_path, os.path.join(com_path, code_path.split("/")[-1]))
                