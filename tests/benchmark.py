import json
from subprocess import call
import os

# create directories for summary files and output files if they don't exist
if not os.path.exists("data/log"):
    os.mkdir("data/log")

if not os.path.exists("data/output"):
    os.mkdir("data/output")

# for pct between 0.0 and 1.0
for p in map(lambda x: x/10.0,range(0,11)):
    #for frac between 0.0 and 1.0
    for f in map(lambda x: x/10.0,range(0,11)):
        # print pct and frac
        print("pct: " + str(p) + " frac: " + str(f))
        # name summary files
        hum_sum_file = "data/log/humanseqs_{0}_{1}.json".format(p, f)
        nonhum_sum_file = "data/log/nonhumanseqs_{0}_{1}.json".format(p, f)
        # run decontam over human seqs
        call(["decontaminate.py", "--forward-reads", "data/humanseqs.fastq", "--organism", "human", "--pct", str(p), "--frac", str(f), "--output-dir", "data/output/", "--summary-file", hum_sum_file])
        # run decontam over nonhuman seqs
        call(["decontaminate.py", "--forward-reads", "data/nonhumanseqs.fastq", "--organism", "human", "--pct", str(p), "--frac", str(f), "--output-dir", "data/output/", "--summary-file", nonhum_sum_file])
        # from human seqs summary file, read and print number of true positive ("true" in data) and false negatives ("false" in data)  
        # from nonhuman seqs summary file, read and print number of false positives ("true" in data) and true negatives ("false" in data)
        message = ["tru ", "fal ", "tru "]
        for i, file in enumerate([hum_sum_file, nonhum_sum_file]):
            with open(file) as f:
                res = json.loads(f.read())
                mes = message[i] + "pos: "
                if "true" in res["data"]:
                    print(mes + str(res["data"]["true"]))
                else:
                    print(mes + "0")    
                mes = message[i+1] + "neg: "
                if "false" in res["data"]:
                    print(mes + str(res["data"]["false"]))
                else:
                    print(mes + "0")
