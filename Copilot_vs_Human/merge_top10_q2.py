import os
main_path= "../refactory/data/question_2/code/copilot_top10/before_merg/"

#merg 3 functions into one python code for question2
def path_content(dir,path):
    dir_path = dir + path
    paths_list = []
    for file_name in os.listdir(dir_path):
        code_path = dir_path + file_name
        paths_list.append(code_path)
    return paths_list

ud_paths = path_content(main_path,"ud/")
um_paths = path_content(main_path,"um/")
cud_paths = path_content(main_path,"cud/")


#print(ud_paths)

for i in range(len(ud_paths)):
    txt =[]
    with open(um_paths[i], "r") as f2:
        txt.append(f2.read())
    with open(cud_paths[i], "r") as f3:
        txt.append(f3.read())
    
    with open(ud_paths[i], 'a') as myfile:
        myfile.write(''.join(txt))