#!/usr/local/bin/python3.2
import urllib.request,io,os,sys
 
req = urllib.request.Request("http://www.google.com")
 
f = urllib.request.urlopen(req)
 
s = f.read()
 
s = s.decode('utf8','ignore')
 
mdir = sys.path[0]+'/'
 
file = open(mdir+'admin6.html','a',1,'utf8')
 
file.write(s)
file.close()
