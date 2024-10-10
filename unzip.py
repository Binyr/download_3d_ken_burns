import os
from tqdm import tqdm
import threading
import json

with open("file_name.txt") as f:
    names = f.readlines()
    names = [x.strip() for x in names]

Error_file_names = []

def runs(names, tid):
    for name in tqdm(names, desc=f"tid: {tid}"):
        if os.path.exists(name):
            continue
        dir_name = name.split(".")[0]
        cmd = f"cd downloads && unzip -q -n {name} -d {dir_name}"
        # print(cmd)
        r = os.system(cmd)
        if r != 0:
            Error_file_names.append(name)
ck = 16
num_example_per_ck = int(len(names) / ck) + 1
ts = []
for i in range(ck):
    sub_names = names[i*num_example_per_ck:(i+1)*num_example_per_ck]
    t = threading.Thread(target=runs, args=(sub_names, i))
    t.start()
    ts.append(t)

for t in ts:
    t.join()


with open("Error_file_names.json", 'w') as fw:
    fw.write(json.dumps(Error_file_names, indent=2))


    
