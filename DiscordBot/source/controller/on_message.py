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

    #スケベ単語辞書
    dumbdic = {
            "あ":"アナル","い":"インポ","う":"ウンコ","え":"エロ","お":"オマンコ",
            "か":"カントン","き":"金玉","く":"クリトリス","け":"ケツ","コ":"コンドーム",
            "さ":"ザーメン","し":"尺八","す":"スカルファック","せ":"セックス","そ":"ソープランド",
            "た":"勃","ち":"膣","つ":"ツルマン","て":"手マン","と":"十月十日",
            "な":"ナチス","に":"妊娠着床","ぬ":"ヌーブラ","ね":"ネオナチ","の":"濃密",
            "は":"ハメ","ひ":"卑猥","ふ":"ブス専","へ":"変態","ほ":"ホモ",
            "ま":"マンコ","み":"実","む":"ムラムラ","め":"メス犬","も":"盛りマン",
            "や":"ヤリサー","ゆ":"ゆういちろう","よ":"嫁",
            "ら":"乱交","り":"凌辱","る":"ルナルナ","れ":"レイプ","ろ":"ロリ",
            "わ":"和姦","を":"ヲタサー","ん":"ンジャメナ"
            }

    #躁アナル 実装者:Yuichi
    #コードパクリ元: Pencily
    if message.content[0:2] == "ue":
        if len(message.content) < 4:
            await message.channel.send("膣膣膣膣膣膣膣膣膣膣膣膣膣膣")
        else:
            uestr = message.content[3:]
            await message.channel.send(uestr.translate(str.maketrans(dumbdic)))

    #鬱アナル 実装者:Yuichi
    #コードパクリ元: Pencily
    if message.content[0:2] == "eu":
        if len(message.content) < 4:
            await message.channel.send("膣膣膣膣膣膣膣膣膣膣膣膣膣膣")
        else:
            uestr = message.content[3:]
            for k,v in dumbdic.items():
                uestr = uestr.replace(v, k)
            await message.channel.send(uestr)

    #aiコマンド変換用辞書
    ai_dictionary = {
        "き":"かい", "し":"さい", "ち":"たい", "に":"ない", 
        "ひ":"はい", "み":"まい", "り":"らい", "ぎ":"がい", "じ":"ざい", 
        "ぢ":"だい", "び":"ばい", "ぴ":"ぱい", "い":"あい"
    }
    #い行変換コマンド 実装者:Pencily
    #3文字目は半角空白でないと実行されません
    if message.content[0:2] == "ai":
        #変換内容がない(aiコマンドのみ)の場合は実行されません
        if len(message.content) < 3:
            await message.channel.send("変換内容を入力してください")
        elif message.content[2] != " ":
            await message.channel.send("コマンドと本文の間に半角空白を挿入してください")
        else:
            aistr = message.content[3:]
            await message.channel.send(aistr.translate(str.maketrans(ai_dictionary)))

    #デコーダー 仕様は上記と同じ
    if message.content[0:2] == "ia":
        if len(message.content) < 3:
            await message.channel.send("デコード内容を入力してください")
        elif message.content[2] != " ":
            await message.channel.send("コマンドと本文の間に半角空白を挿入してください")
        else:
            iastr = message.content[3:]
            for iato, iafrom in ai_dictionary.items():
                iastr = iastr.replace(iafrom, iato)
            await message.channel.send(iastr)

    #たまご or tamago or eggを含む文章に:egg:のリアクションをつけます 実装者:Pencily
    if "たまご" in message.content or "tamago" in message.content or "egg" in message.content:
        await message.add_reaction("\U0001F95A")

#### ON_MESSAGE_END ####
