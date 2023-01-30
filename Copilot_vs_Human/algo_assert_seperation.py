
import os

def read_write_assert(test_path, ans_path):
    i=1
    try:
        with open(test_path, 'r') as f:
            for ln in f:
                ln = ln.lstrip(' ')
                if ln.startswith("assert"):
                    test_string = ln[7:]
                    split_test = test_string.split('==')
                    input = split_test[0]
                    output = split_test[1]


                    f = open(ans_path+"/input_"+str(i)+".txt", "w")
                    f.write(input.lstrip(' '))
                    f.close()

                    f = open(ans_path+"/output_"+str(i)+".txt", "w")
                    f.write(output.lstrip(' '))
                    f.close()
                    i+=1
    except:
        print("File not found: "+test_path)


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
        ans_path = os.path.join(CODE_DIR , "ans")
        test_path = os.path.join(CODE_DIR , "test_sort.py" )
        read_write_assert(test_path, ans_path)
