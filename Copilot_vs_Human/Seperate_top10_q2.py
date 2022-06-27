import os

path = r"../refactory/data/question_2/code/5run/"
dst_path= r"../refactory/data/question_2/code/copilot_top10/before_merg/"
#change the ext_path into "um" to apply on unique_month function and 
# "cud" to apply on contain_unique_day function.
ext_path= "ud"
token = '======='
chunks = {}
current_chunk = []
i=1

def paths_list(ext_path,ques_dir_path): 
    dir_path = ques_dir_path + ext_path
    path_list = []
    for file_name in os.listdir(dir_path):
        code_path = dir_path + "/" + file_name
        path_list.append(code_path)
    return path_list

path_list = []
path_list = paths_list(ext_path, path)
print(path_list)

for code_path in path_list:
        with open (code_path, "r") as myfile:
            data=myfile.readlines()
            file_name_hlp = code_path.split("/")[-1]
            file_name_hlp = file_name_hlp.split(".")[0]
            print(file_name_hlp)
            for line in data:
                if line.startswith(token):
                    file_name = file_name_hlp + "_"+str(i)
                    i=i+1
                    current_chunk = []
                    #current_chunk.append(line)
                    chunks[file_name] = current_chunk
                else:
                    current_chunk.append(line)

        #print (chunks)

for name, storage in chunks.items():
    print(name)
    with open(os.path.join(dst_path,ext_path, name + '.py'), 'w') as file:
        file.write("".join(storage))
        file.close()