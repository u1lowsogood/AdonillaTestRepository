#### ON_MESSAGE_START ####

@client.event
async def on_message(message):
    
    if message.author == client.user:
        return

    # ボイスチャットに入る
    if message.content == ('金玉燃やすぞ') or message.content == ('全召喚') or message.content == ('tamago'):
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

    #い行変換コマンド 実装者:Pencily
    #3文字目は認識しない仕様です
    if message.content[0:2] == "ai":
        #変換内容がない(aiコマンドのみ)の場合はreturnします
        if len(message.content) < 4:
            await message.channel.send("変換内容を入力してください")
        else:
            aistr = message.content[3:]
            aistr_listed = list(aistr)
            for i, x in enumerate(aistr_listed): #正直ここenumerateじゃなくてもいいのかも知れない
                if x == "い":
                    aistr_listed[i] = "あい" #この沼コードスッキリさせる方法あったら教えて下さい
                elif x == "き":
                    aistr_listed[i] = "かい"
                elif x == "し":
                    aistr_listed[i] = "さい"
                elif x == "ち":
                    aistr_listed[i] = "たい"
                elif x == "に":
                    aistr_listed[i] = "ない"
                elif x == "ひ":
                    aistr_listed[i] = "はい"
                elif x == "み":
                    aistr_listed[i] = "まい"
                elif x == "り":
                    aistr_listed[i] = "らい"
                elif x == "ぎ":
                    aistr_listed[i] = "がい"
                elif x == "じ":
                    aistr_listed[i] = "ざい"
                elif x == "ぢ":
                    aistr_listed[i] = "だい"
                elif x == "び":
                    aistr_listed[i] = "ばい"
                elif x == "ぴ":
                    aistr_listed[i] = "ぱい"
            await message.channel.send("".join(aistr_listed))

    #たまご or tamago or eggを含む文章に:egg:のリアクションをつけます 実装者:Pencily
    if "たまご" in message.content or "tamago" in message.content or "egg" in message.content:
        await message.add_reaction("\U0001F95A")

#### ON_MESSAGE_END ####


