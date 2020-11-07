# この配列に別途追加したいファイル名を追記してください……
readFileNames = ["on_ready.py","on_message.py"]

# パス
controllerPath = "./source/controller/"
headAndAssPath = "./source/core/"

# パス名たちの初期化
readFilePathes = []

# ファイル名をパスにするよ
for fileName in readFileNames:
    fileName = controllerPath + fileName
    readFilePathes.append(fileName)

# 頭とケツにコアな部分を結合
readFilePathes.insert(0,headAndAssPath + "import.py")
readFilePathes.append(  headAndAssPath +  "clientRun.py")

print(readFilePathes)

# 上記ファイルの内容をすべて結合し、実行用のpyファイルを出力します
with open("output.py", "wb") as outfile:
    for f in readFilePathes:
        with open(f, "rb") as infile:
            outfile.write(infile.read())