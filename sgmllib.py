from sgmllib import SGMLParser  
#from html.parser import HTMLParser
class GetIdList(SGMLParser):  
    def reset(self):  
        self.IDlist = []  
        self.flag = False  
        self.getdata = False  
        self.verbatim = 0  
        SGMLParser.reset(self)  
          
    def start_div(self, attrs):  
        if self.flag == True:  
            self.verbatim +=1 #进入子层div了，层数加1  
            return  
        for k,v in attrs:#遍历div的所有属性以及其值  
            if k == 'class' and v == 'entry-content':#确定进入了<div class='entry-content'>  
                self.flag = True  
                return  
  
    def end_div(self):#遇到</div>  
        if self.verbatim == 0:  
            self.flag = False  
        if self.flag == True:#退出子层div了，层数减1  
            self.verbatim -=1  
  
    def start_p(self, attrs):  
        if self.flag == False:  
            return  
        self.getdata = True  
          
    def end_p(self):#遇到</p>  
        if self.getdata:  
            self.getdata = False  
  
    def handle_data(self, text):#处理文本  
        if self.getdata:  
            self.IDlist.append(text)  
              
    def printID(self):  
        for i in self.IDlist:  
            print (i)  
  
  
##import urllib2  
##import datetime  
##vrg = (datetime.date(2012,2,19) - datetime.date.today()).days  
##strUrl = 'http://www.nod32id.org/nod32id/%d.html'%(200+vrg)  
##req = urllib2.Request(strUrl)#通过网络获取网页  
##response = urllib2.urlopen(req)  
##the_page = response.read()  
  
the_page ='''''<html> 
<head> 
<title>test</title> 
</head> 
<body> 
<h1>title</h1> 
<div class='entry-content'> 
<div class= 'ooxx'>我是来捣乱的</div> 
<p>感兴趣内容1</p> 
<p>感兴趣内容2</p> 
…… 
<p>感兴趣内容n</p> 
<div class= 'ooxx'>我是来捣乱的2<div class= 'ooxx'>我是来捣乱的3</div></div> 
</div> 
<div class='content'> 
<p>内容1</p> 
<p>内容2</p> 
…… 
<p>内容n</p> 
</div> 
</body> 
</html> 
'''  
lister = GetIdList()  
lister.feed(the_page)  
lister.printID()  
