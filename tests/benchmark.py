import json

message = ["true ", "false ", "true "]
for i, file in enumerate(["data/humanseqs.json", "data/nonhumanseqs.json"]):
    with open(file) as f:
        res = json.loads(f.read())
        mes = message[i] + "positives: "
        if "true" in res["data"]:
            print(mes + str(res["data"]["true"]))
        else:
            print(mes + "0")    
        mes = message[i+1] + "negatives: "
        if "false" in res["data"]:
            print(mes + str(res["data"]["false"]))
        else:
            print(mes + "0")
