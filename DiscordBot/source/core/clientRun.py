# ゆういちのローカルファイルからトークンを取得
f = open('D:\\Git\\botoken.txt', 'r', encoding='UTF-8')
token = f.read()
print(token)
client.run(token)
f.close()

