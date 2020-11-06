#import なんかインポートして
import datetime

#まいんこんとろーら

def MainProgram(discord_id, message):

        # JOIN VC
    if message.content == ('金玉燃やすぞ') or message.content == ('全召喚') or message.content == ('tamago'):
        vcstate = message.author.voice

        if (not vcstate) or (not vcstate.channel):
            return "金玉どこだよ"

        voicechannel = vcstate.channel

        voicechannel.connect()
        activity = discord.Activity(
            name='【ケツ穴拡張！？ドスケベマンコRoyal】Solo - Squad 4/3 残糞：残り(一億 人) ', type=discord.ActivityType.watching)

        client.change_presence(activity=activity)

        return 'うるさいうるさいうるさいうるさいうるさいうるさいうるさいうるさい'

    # LEAVE VC
    if message.content == ('金玉叩き割ったわ'):
        vcclient = message.guild.voice_client

        if not vcclient:
            return "うるさいうるさいうるさいうるさいうるさいうるさいうるさいうるさい"

        vcclient.disconnect()
        return 'うるさいうるさいうるさいうるさいうるさいうるさいうるさいうるさいうるさいうるさい'

    if message.content == ('atAoki'):
        jstart_dt = datetime.datetime.now()
        jend_dt = datetime.datetime(year=2021, month=2, day=16, hour=14)

        jat_time = jend_dt - jstart_dt
        a_m, a_s = divmod(jat_time.seconds, 60)
        a_h, a_m = divmod(a_m, 60)

        r_jat_time = 'あと' + str(jat_time.days) + '日' + str(a_h) + '時間' + str(a_m) + '分' + str(a_s) + '秒' + str(jat_time.microseconds)
        return r_jat_time

    return ''
