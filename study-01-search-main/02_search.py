
### 検索ツールサンプル
### これをベースに課題の内容を追記してください

# 検索ソース
source=["ねずこ","たんじろう","きょうじゅろう","ぎゆう","げんや","かなお","ぜんいつ"]
source_b=["ねずこ","たんじろう","きょうじゅろう","ぎゆう","げんや","かなお","ぜんいつ"]

### 検索ツール
def search(source):
    word =input("鬼滅の登場人物の名前を入力してください >>> ")
    
    ### ここに検索ロジックを書く
    if not(word in source):
        source.append(word)

    return source

if __name__ == "__main__":
    search(source)
    print("鬼滅の登場人物の（更新前）⇒",source_b)
    print("鬼滅の登場人物の（更新後）⇒",source)
