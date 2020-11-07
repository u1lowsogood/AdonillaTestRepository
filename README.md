# AdonillaTestRepository
試しにみんなでなんか開発しようぜ

# このリポジトリの仕様について（！！UPDATED！！）

## どゆこと？

2020/11/08に大型アップデートを行いました。
前回と仕様が大幅に変わったのでチェック必須。

## どうすればいいの？

基本的に、アドンイラ開発部門メンバーの皆さんが作業するのは、次のフォルダの内になると思います。

```DiscordBot -> source -> controller```


```controllerフォルダ```内にあるファイルは全て、@client.event毎に分割されています

例えば、ログイン時に何かしらの処理を追加したいのであれば、そのフォルダの中にある```on_ready.py```を、
メッセージに対し何かしらのレスポンスを返したいのであれば```on_message.py```を編集する、ということになります。
各自、自身の環境でデバッグし、動作した内容を丸々コピペ追記すればこちらでも動く、という算段になります。


## 鯖主（ゆういち）はどうやってこのBOT動かすの

```DiscordBot```ファイルの中にある```execute.py```を実行すると、以下のファイルが一つにまとまります。

```DiscordBot -> source -> controller```の中身ファイル（各イベントに対する処理が描いてあるぞ！）
```DiscordBot -> source -> core```の中身（```import.py``` ```clienrRun.py```）

上記ファイルを無理やり１つのファイルに結合し、出力された```output.py```を実行することによって、BOTが動作します。
正直言ってやり方としては最悪だと思いますが、そういう所なので笑

## モジュール入れたい・・・入れたくない？

```DiscordBot -> source -> core -> import.py``` にimport文を追記してください。

## 横文字ズラァアアアアッｗｗｗｗｗｗｗｗｗｗ

レポジトリ：作業領域  
アドンイラ：秘密結社の通称  

# アドンイラプッシャー備忘録
* ローカルリポジトリを作成
```bash
git init
```

* リモートリポジトリ「AdonillaTestRepository」に参加（既に参加してる場合は不要）
```bash
git remote add origin https://github.com/u1lowsogood/AdonillaTestRepository.git
```

* リモートリポジトリからファイルを落としてくる（pushの前に必ずこれをやること）
```bash
git pull https://github.com/u1lowsogood/AdonillaTestRepository.git master
```

* ローカルリポジトリにファイルを追加
```bash
git add [ファイル名].txt
git commit -m "説明文"
```

* ローカルリポジトリのファイルをリモートリポジトリ「AdonillaTestRepository」に送信！
```bash
git push origin master
```
