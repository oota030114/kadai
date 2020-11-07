import csv
import os

# 検索ソース
source=["ねずこ","たんじろう","きょうじゅろう","ぎゆう","げんや","かなお","ぜんいつ"]
source_b=["ねずこ","たんじろう","きょうじゅろう","ぎゆう","げんや","かなお","ぜんいつ"]


### csv読込み
def readCSV():
    csvFile =input("CSVファイルを指定してください（フルパス） >>> ")
    if os.path.exists(csvFile):
        with open(csvFile) as f:
            listCSV = f.read()
            f.close()
            return listCSV.split(',')

### リスト更新
def updateSource(listCSV, source):    
    index = 0
    while index < len(listCSV):
        if not(listCSV[index] in source):
            source.append(listCSV[index])
        index = index + 1
    return source

### メイン処理
if __name__ == "__main__":
    ###csv読込み
    listCSV = readCSV()
    ###リスト更新
    updateSource(listCSV, source)
    ###更新結果
    print("鬼滅の登場人物の（更新前）⇒",source_b)
    print("鬼滅の登場人物の（更新後）⇒",source)
