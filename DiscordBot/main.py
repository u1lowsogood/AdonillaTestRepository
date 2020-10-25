# discord.py読み込み
import discord

#コントローラ読み込み
from controller import MainController
#モデルファイル読み込み
#from model import MainModel

print("manko")

# 接続に必要なオブジェクトを生成
client = discord.Client()

print("manko")

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
        talk = MainController.MainProgram(discord_id,message.content)

    print('Duck：',talk)

    #DiscordBotがメッセージ送信
    await message.channel.send(talk)


# Botの起動とDiscordサーバーへの接続
client.run('NzY5ODQxMjg4NTAwNjA5MDQ0.X5U4kg.s46Ul_ayfheAuXKmt0YbXXkdFdw')

