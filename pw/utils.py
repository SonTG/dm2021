import json


def loadData():
    wc = []
    with open("yelp-1000.json", "r") as fp:
        while True:
            line = fp.readline()
            if not line:
                break
            review = json.loads(line)
            text = review["text"]
            wc.append(len(text.split(" ")))
            if len(wc) > 20:
                break
            
    return wc