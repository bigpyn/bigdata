#-*-coding:utf-8 -*-
import json				#导入json库
import requests			#导入requests库


def music(search):					#定义一个方法传入搜索参数
	txt=open('music.txt','a+')
	if search=="":
		return
	urls="http://s.music.163.com/search/get/?type=1&s="+search+"&limit=100" 	#网易云音乐接口,取出前100条，可以自定义
	data=requests.get(urls)					#请求这个接口
	data.decode="utf-8"						#请求使用utf-8编码
	datas=json.loads(data.text)					#将json数据转成字典
	songs=datas["result"]["songs"]					#取出里面的songs
	print(songs)
	i=0
	try:
		for musics in songs:
			i+=1
			print(i,musics["audio"],musics["name"],musics["artists"][0]["name"])	#取出歌曲地址和名字，取出歌手信息
			a=str((i,musics["audio"],musics["name"],musics["artists"][0]["name"]))
			txt.write(a+'\n')

	except UnicodeEncodeError:
		pass
search=input("what are you want to search:")
music(search)
print("OK")
