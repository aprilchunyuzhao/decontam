import json
from subprocess import call

for p in map(lambda x: x/10.0,range(0,10)):
    for f in map(lambda x: x/10.0,range(0,10)):
        print("pct: " + str(p) + " frac: " + str(f))
        hum_sum_file = "data/log/humanseqs" + "_" + str(p) + "_" + str(f) + ".json"
        nonhum_sum_file = "data/log/nonhumanseqs" + "_" + str(p) + "_" + str(f) + ".json"
        call(["decontaminate.py", "--forward-reads", "data/humanseqs.fastq", "--organism", "human", "--pct", str(p), "--frac", str(f), "--output-dir", "../../fastq_files/output/", "--summary-file", hum_sum_file])
        call(["decontaminate.py", "--forward-reads", "data/nonhumanseqs.fastq", "--organism", "human", "--pct", str(p), "--frac", str(f), "--output-dir", "../../fastq_files/output/", "--summary-file", nonhum_sum_file])
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
