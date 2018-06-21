
def pathApp(path, app):
    return Path(str(path) + "\\" + app)

def saveFile(filename, contents):
    with open(filename, mode="w", encoding="utf-8") as f:
        f.write(contents)

def loadJSON(filepath):
    result = ""
    with open(filepath, encoding="utf-8") as f:
        result = load(f)
    return result

def flatten(d):
    res = []
    if isinstance(d, dict):
        for k,v in d.items():
            f = flatten(v)
            res += map(lambda x: [k] + x, f)
        return res
    else:
        return [[d]]