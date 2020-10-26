#import なんかインポートして

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

    return ''
