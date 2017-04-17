import urllib.parse
import win32clipboard
import win32con

def getClipboardText():
	win32clipboard.OpenClipboard()
	result = win32clipboard.GetClipboardData(win32con.CF_TEXT)
	win32clipboard.CloseClipboard()
	return result

if __name__ == "__main__":
	input('复制网址，回车')
	url=getClipboardText()
	url=url.decode('utf-8') #transform bytes into str
	url=str(url)[0:] #strip 'http://sc.qq.com/'

	trans_url= urllib.parse.unquote(url)
	with open(r'C:\Users\Administrator\Desktop\微信收藏地址.txt',mode='a',encoding='utf-8') as f:
		f.write(trans_url)
		f.write('\n')
