import urllib.request,sys

import re
provice=input('输入省名(请使用拼音):');
url="http://qq.ip138.com/weather/"+provice+'/'

wetherhtml=urllib.request.urlopen(url)
result=wetherhtml.read().decode('GB2312')#.encode('utf-8')
print (result)

'''s=<td>
10℃～
2℃
</td>
<td>
7℃～
0℃
</td>
<td>
14℃～
4℃
</td>
<td>
15℃～
5℃
</td>
<td>
15℃～
3℃
</td>'''

#pattern='<td>([0-9]{2}.*?[0-9]{2}.*?)</td>'
pattern='<td>\n(.*\n.*)\n</td>'
temperature=re.findall(pattern,result)#温度
#print(temperature)
for x in temperature:
	print(x.replace('\n',''))
#把温度取出来，比如：5℃～3℃
