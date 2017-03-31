from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader,Context
from .models import user,admin,mp4
import hashlib

# Create your views here.
def index(request):
    return render(request,"music_search.html")




'''
def md5(request):
    def md5(str):
        md5hash=hashlib.md5(str.encode(encoding="utf-8")).hexdigest()
        return md5hash
    if request.POST.get("md5"):
        str=request.POST.get("md5")
        hashmd5=md5(str)
        html=loader.get_template("search.html")
        data=Context({"md5":hashmd5})
        return HttpResponse(html.render(data))
    else:
        return render(request,"search.html")
        '''


def music_search(request):
    import json  # 导入json库
    import requests  # 导入requests库
    def music(search):  # 定义一个方法传入搜索参数
        urls = "http://s.music.163.com/search/get/?type=1&s=" + search + "&limit=200"  # 网易云音乐接口,取出前100条，可以自定义
        data = requests.get(urls)  # 请求这个接口
        data.decode = "utf-8"  # 请求使用utf-8编码
        datas = json.loads(data.text)  # 将json数据转成字典
        songs = datas["result"]["songs"]  # 取出里面的songs
        music_audio=[]
        music_name=[]
        music_art=[]
        for musics in songs:
            music_audio.append(musics['audio'])
            music_name.append(musics['name'])
            music_art.append(musics["artists"][0]["name"])
        musiclist=zip(music_name,music_audio,music_art)
        return musiclist
    if request.POST.get("search"):
        #try:
        search=request.POST.get("search")
        musics=music(search)
        data={"musics":musics}
        datas=Context(data)
        html=loader.get_template("music.html")
        return HttpResponse(html.render(datas))
        #except ConnectionError:
           # return HttpResponse("<center><h1>Time Out</h1></center>")
    else:
        return render(request,"music_search.html")


def download(request):
    if request.GET.get("id"):
        cid=request.GET.get("id")
        html=loader.get_template("player.html")
        data=Context({"cid":cid})
        return HttpResponse(html.render(data))
    else:
        return render(request,"music_search.html")






