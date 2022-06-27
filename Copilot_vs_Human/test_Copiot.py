from random import random
from basic_framework.core_testing import Tester
from basic_framework.utils import regularize
import random
import os
import shutil

#change the question number in below path
ques_dir_path = "../refactory/data/question_5"

#change the run number in below 
num_run= "5"
path_hlp= "/code/copilot_top10/run" + num_run
general_path="/code/copilot_top10"

def paths_list(ques_dir_path,path_hlp):
    dir_path = ques_dir_path + path_hlp + "/code"
    path_list = []
    for file_name in os.listdir(dir_path):
        code_path = dir_path + "/" + file_name
        path_list.append(code_path)
    #random.shuffle(path_list)
    
    return path_list

def dst_paths (action, ques_dir_path,path_hlp):
    if action == 1:
        dir_path = ques_dir_path + path_hlp + "/correct"
    elif action == 0:
        dir_path = ques_dir_path + path_hlp + "/wrong"
    elif action == 11:
        dir_path = ques_dir_path + general_path + "/correct"
    elif action == 10:
        dir_path = ques_dir_path + general_path + "/wrong"
    return dir_path

    
path_list = []
path_list = paths_list(ques_dir_path,path_hlp)

#print(path_list)
t = Tester(ques_dir_path)
code_map = {}
for code_path in path_list:
        with open(code_path, "r") as f:
            file_name = code_path.split("/")[-1]
            print(file_name)
            code = regularize(f.read())
            tr = t.tv_code(code)
            if t.is_pass(tr):
                shutil.copyfile(code_path, os.path.join(dst_paths(1,ques_dir_path,path_hlp), file_name))
                shutil.copyfile(code_path, os.path.join(dst_paths(11,ques_dir_path,path_hlp), file_name))
                code_map[file_name] = code
                print("correct code: ", file_name)
            else:
                 shutil.copyfile(code_path, os.path.join(dst_paths(0,ques_dir_path,path_hlp), file_name))
                 shutil.copyfile(code_path, os.path.join(dst_paths(10,ques_dir_path,path_hlp), file_name))
                 print("Wrong code: ", file_name)
                 print(tr)
                 print(code_path)
