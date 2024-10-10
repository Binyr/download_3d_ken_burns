import os
from tqdm import tqdm
import threading

with open("file_name.txt") as f:
    names = f.readlines()
    names = [x.strip() for x in names]

def runs(names, tid):
    for name in tqdm(names, desc=f"tid: {tid}"):
        if os.path.exists(name):
            continue
        cmd = f"wget https://u355171-sub1:m4DDxuwJzm3Fy9vn@u355171-sub1.your-storagebox.de/{name}"
        print(cmd)
        os.system(cmd)
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


    
