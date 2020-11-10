import MySQLdb

# データベースへの接続とカーソルの生成
#host:DBのアドレス
#user:DBのユーザ名
#passwd:DBのパスワード
#charset:文字コード
#####################
connection = MySQLdb.connect(
	host='192.168.19.19',
	user='kokura',
	passwd='bomubomu',
	db='kokura',
	charset="utf8mb4")
cursor = connection.cursor()


#とりまセレクト
def select_user_name(discord_id):
	cursor.execute('SELECT * FROM table WHERE discord_id=%s', (discord_id,))
	if cursor.rowcount == 0:
		return None
	else:
		return cursor.fetchone()


