# discord.py読み込み
import discord
import datetime

# モデルファイル読み込み（MySQL用、まだ使わないのでコメントアウト）
#from model import PublicModel

# 接続に必要なオブジェクトを生成
client = discord.Client()

#### ON_READY_START ####

@client.event
async def on_ready():
    print('Duck: Discordにログインしたよ')

##### ON_READY_END ####

#### ON_MESSAGE_START ####

@client.event
async def on_message(message):
    
    if message.author == client.user:
        return

<<<<<<< HEAD:DiscordBot/main.py
        # JOIN VC
    if message.content == ('金玉燃やすぞ') or message.content == ('全召喚'):
=======
    # ボイスチャットに入る
    if message.content == ('金玉燃やすぞ') or message.content == ('全召喚') or message.content == ('tamago'):
>>>>>>> 2dab760e6a9bafc9205b86afc4769114bd6afaee:DiscordBot/output.py
        vcstate = message.author.voice

        if (not vcstate) or (not vcstate.channel):
            await message.channel.send("金玉どこだよ")

        voicechannel = vcstate.channel
        await voicechannel.connect()
        activity = discord.Activity(
            name='【ケツ穴拡張！？ドスケベマンコRoyal】Solo - Squad 4/3 残糞：残り(一億 人) ', type=discord.ActivityType.watching)

        await client.change_presence(activity=activity)
        await message.channel.send('うるさいうるさいうるさいうるさいうるさいうるさいうるさいうるさい')

    # ボイチャぬける
    if message.content == ('金玉叩き割ったわ'):
        vcclient = message.guild.voice_client

        if not vcclient:
            await message.channel.send('うるさいうるさいうるさいうるさいうるさいうるさいうるさいうるさい')

        await vcclient.disconnect()
        await message.channel.send('うるさいうるさいうるさいうるさいうるさいうるさいうるさいうるさい')

    if message.content == ('atAoki'):
        jstart_dt = datetime.datetime.now()
        jend_dt = datetime.datetime(year=2021, month=2, day=16, hour=14)

        jat_time = jend_dt - jstart_dt
        a_m, a_s = divmod(jat_time.seconds, 60)
        a_h, a_m = divmod(a_m, 60)

        r_jat_time = 'あと' + str(jat_time.days) + '日' + str(a_h) + '時間' + str(a_m) + '分' + str(a_s) + '秒' + str(jat_time.microseconds)
        await message.channel.send(r_jat_time)

#### ON_MESSAGE_END ####


# ゆういちのローカルファイルからトークンを取得
f = open('D:\\Git\\botoken.txt', 'r', encoding='UTF-8')
token = f.read()
print(token)
client.run(token)
f.close()

