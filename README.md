# AdonillaTestRepository
試しにみんなでなんか開発しようぜ


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
