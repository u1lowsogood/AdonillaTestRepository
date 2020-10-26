# discord.py読み込み
import discord

#コントローラ読み込み
from controller import MainController
#モデルファイル読み込み
#from model import MainModel

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('Dack：discordにログインしたよ')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    talk = ''

    # BOTのメッセージは無視する
    if message.author.bot:
        return

    # その他のメッセージだった場合処理
    else:
       discord_id = message.author.id

    #Controllerの
    talk = MainController.MainProgram(discord_id, message)

    #DiscordBotがメッセージ送信
    if talk != (''):
        print('Duck：',talk)
        await message.channel.send(talk)

    

# ゆういちのローカルファイルからトークンを取得
f = open('D:\\Git\\botoken.txt', 'r', encoding='UTF-8')
token = f.read()
print(token)
client.run(token)
f.close()
