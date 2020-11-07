import csv
import os

# 検索ソース
source=["ねずこ","たんじろう","きょうじゅろう","ぎゆう","げんや","かなお","ぜんいつ"]
source_b=["ねずこ","たんじろう","きょうじゅろう","ぎゆう","げんや","かなお","ぜんいつ"]

### csv読込み
def readCSV(csvFile):
    if os.path.exists(csvFile):
        with open(csvFile) as f:
            listCSV = f.read()
            f.close()
            return listCSV.split(',')

### リスト更新
def updateSource(listCSV):    
    index = 0
    while index < len(listCSV):
        if not(listCSV[index] in source):
            source.append(listCSV[index])
        index = index + 1
    return source

### 検索ツール
def search():
    word =input("鬼滅の登場人物の名前を入力してください >>> ")
    chk = word[-4:]
    if (chk == ".csv") or (chk == ".CSV"):
        if (os.path.isfile(word)):
            ###csv読込み
            listCSV = readCSV(word)
            ret  = updateSource(listCSV)
        else:
            ret = "入力したCSVファイルは存在しません。"
    else:
        if not(word in source):
            source.append(word)
        ret = source
    return ret

### メイン処理
if __name__ == "__main__":
    ### 検索ツール
    source = search()
    ###更新結果
    print("鬼滅の登場人物の（更新前）⇒",source_b)
    print("鬼滅の登場人物の（更新後）⇒",source)
