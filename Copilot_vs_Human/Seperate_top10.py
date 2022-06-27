import os

#change question number in both below path to apply it on other questions
path = r"../refactory/data/question_5/code/5run"
dst_path= r"../refactory/data/question_5/code/copilot_top10"

#change q_num to apply on other questions and run_num to apply on other runs
q_num= "5"
run_num= "5"


ext_path= "run"+ run_num + "/code"
file_name_hlp = 'copilot_q' + q_num + '_r' + run_num + '_'
run_file = 'run_' + run_num + '.txt'

token = '======='
chunks = {}
current_chunk = []
i=1

with open (os.path.join(path, run_file), "r") as myfile:
    data=myfile.readlines()

for line in data:
    if line.startswith(token):
        file_name = file_name_hlp + str(i)
        i=i+1
        current_chunk = []
        #current_chunk.append(line)
        chunks[file_name] = current_chunk
    else:
        current_chunk.append(line)

print (chunks)

for name, storage in chunks.items():
    print(name)
    with open(os.path.join(dst_path,ext_path, name + '.py'), 'w') as file:
        file.write("".join(storage))
        file.close()