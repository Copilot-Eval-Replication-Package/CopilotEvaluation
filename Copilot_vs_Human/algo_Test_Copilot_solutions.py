from basic_framework.core_testing import Tester
from basic_framework.utils import regularize
import os
import sys
import pandas as pd
import shutil



def paths_list(dir_path):
   # dir_path = ques_dir_path + path_hlp 
    path_list = []
    for file_name in os.listdir(dir_path):
        code_path = dir_path + "/" + file_name
        path_list.append(code_path)

    return path_list



def run_code_on_test_cases(CODE_DIR):
    code_path = os.path.join(CODE_DIR, "Correct")
    ans_path = os.path.join(CODE_DIR, "ans")
   

    code_path_list = paths_list(code_path)
    ans_path_list = paths_list(ans_path)
    
 
    for code_path in code_path_list:
        t_f = Tester(ans_path)
        with open(code_path, "r") as f:
            file_name = code_path.split("/")[-1]
            print(file_name)

            try:
                code = f.read()
                t_fs_r = t_f.tv_code(code)
            except:
                print("Error in code:" + file_name)
                continue

            

        if t_f.is_pass(t_fs_r):
            status_fs = "Pass"
            print("Correct code: ", file_name)
        else:
            status_fs = "Fail"
            shutil.copyfile(code_path, os.path.join(CODE_DIR,"Wrong", file_name))
            os.remove(code_path)
                
            print("Wrong code: ", file_name)
            


if __name__ == "__main__":
    DATASET = "CoPilot_on_Algorithm_Design"
    GP_algo = "Sorting_Algorithms"
    algo_name =[ "Bubble_Sort", "Insertion_Sort", "Selection_Sort", "Merge_Sort", "Quick_Sort", "Heap_Sort","Bucket_Sort","Radix_Sort"]
    for algo in algo_name:
        CODE_DIR = os.path.join(
                os.getcwd(),
                DATASET,GP_algo, algo,
                "",
            )
        run_code_on_test_cases(CODE_DIR)
