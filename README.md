# AdonillaTestRepository
試しにみんなでなんか開発しようぜ

# このリポジトリの仕様について（！！UPDATED！！）

* どゆこと？

2020/11/08に大型アップデートを行いました。
前回と仕様が大幅に変わったのでチェック必須。

* どうすればいいの？

基本的に、アドンイラ開発部門メンバーの皆さんが作業するのは、次のフォルダの内になると思います。

```DiscordBot -> source -> controller```


例えば、ログイン時に何かしらの処理を追加したいのであれば、そのフォルダの中にある```on_ready.py```を、

メッセージに対しレスポンスを返したいのであれば```on_message.py```を編集する、ということになります。

各自、自身の環境でデバッグし、動作した内容を丸々コピペ追記すればこちらでも動く、という算段になります。

*

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
