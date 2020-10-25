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
    #talk = ''

    # BOTのメッセージは無視する
    #if message.author.bot:
    #    return

    # その他のメッセージだった場合処理
    #else:
    #   discord_id = message.author.id

        #Controllerの
    #    talk = MainController.MainProgram(discord_id,message.content)

    #print('Duck：',talk)

    #DiscordBotがメッセージ送信
    #await message.channel.send(talk)

        # JOIN VC
    if message.content == ('金玉燃やすぞ') or message.content == ('全召喚') or message.content == ('tamago'):
        vcstate = message.author.voice

        if (not vcstate) or (not vcstate.channel):
            await message.channel.send("金玉どこだよ")
            return

        voicechannel = vcstate.channel
        await voicechannel.connect()
        activity = discord.Activity(
            name='【ケツ穴拡張！？ドスケベマンコRoyal】Solo - Squad 4/3 残糞：残り(一億 人) ', type=discord.ActivityType.watching)
        await client.change_presence(activity=activity)
        await message.channel.send('うるさいうるさいうるさいうるさいうるさいうるさいうるさいうるさい')

    # LEAVE VC
    if message.content == ('金玉叩き割ったわ'):
        vcclient = message.guild.voice_client

        if not vcclient:
            await message.channel.send("うるさいうるさいうるさいうるさいうるさいうるさいうるさいうるさい")
            return

        await vcclient.disconnect()
        await message.channel.send('うるさいうるさいうるさいうるさいうるさいうるさいうるさいうるさいうるさいうるさい')


# ゆういちのローカルファイルからトークンを取得
f = open('D:\\Git\\botoken.txt', 'r', encoding='UTF-8')
token = f.read()
print(token)
client.run(token)
f.close()
