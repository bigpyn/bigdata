ubuntu下python2.76

windows Python 2.79, chrome37 firefox35通过

代码是在别人(cddn有人提问)基础上改的, 主要改动了parsedata和sendmessage这2个函数.

改代码参考下面了这段文档. 主要是第5条, 发送的数据长度分别是 8bit和 16bit和 64 bit(即 127, 65535,和2^64-1)三种情况 

发送和收取是一样的, 例如

1.长度小于125时(由于使用126, 127用作标志位.)

2. 数据长度在128-65525之间时, Payload Length位设为126, 后面额外使用16bit表示长度(前面的126不再是长度的一部分)

3.数据长度在65526-2^64-1之间时, Payload Length位设为127, 后面额外使用64bit表示长度(前面的127不再是长度的一部分)

Fin (bit 0): determines if this is the last frame in the message. This would be set to 1 on the end of a series of frames, or in a single-frame message, it would be set to 1 as it is both the first and last frame.
RSV1, RSV2, RSV3 (bits 1-3): these three bits are reserved for websocket extensions, and should be 0 unless a specific extension requires the use of any of these bytes.
Opcode (bits 4-7): these four bits deterimine the type of the frame. Control frames communicate WebSocket state, while non-control frames communicate data. The various types of codes include:

x0: continuation frame; this frame contains data that should be appended to the previous frame
x1: text frame; this frame (and any following) contains text
x2: binary frame; this frame (and any following) contains binary data
x3 - x7: non-control reserved frames; these are reserved for possible websocket extensions
x8: close frame; this frame should end the connection
x9: ping frame
xA: pong frame
xB - xF: control reserved frames
Mask (bit 8): this bit determines whether this specific frame uses a mask or not.
Payload Length (bits 9-15, or 16-31, or 16-79): these seven bytes determine the payload length. If the length is 126, the length is actually determined by bits 16 through 31 (that is, the following two bytes). If the length is 127, the length is actually determined by bits 16 through 79 (that is, the following eight bytes).
Masking Key (the following four bytes): this represents the mask, if the Mask bit is set to 1.
Payload Data (the following data): finally, the data. The payload data may be sent over multiple frames; we know the size of the entire message by the payload length that was sent, and can append data together to form a single message until we receive the message with the Fin flag. Each consecutive payload, if it exists, will contain the 0 “continuation frame” opcode.


服务器

[python] view plain copy 在CODE上查看代码片派生到我的代码片
#coding=utf8  
#!/usr/bin/python  
  
  
import struct,socket  
import hashlib  
import threading,random  
import time  
import struct  
from base64 import b64encode, b64decode  
  
  
connectionlist = {}  
g_code_length = 0  
g_header_length = 0  
  
  
def hex2dec(string_num):  
    return str(int(string_num.upper(), 16))  
  
  
  
  
def get_datalength(msg):  
    global g_code_length  
    global g_header_length      
      
    print (len(msg))  
    g_code_length = ord(msg[1]) & 127  
    received_length = 0;  
    if g_code_length == 126:  
        #g_code_length = msg[2:4]  
        #g_code_length = (ord(msg[2])<<8) + (ord(msg[3]))  
        g_code_length = struct.unpack('>H', str(msg[2:4]))[0]  
        g_header_length = 8  
    elif g_code_length == 127:  
        #g_code_length = msg[2:10]  
        g_code_length = struct.unpack('>Q', str(msg[2:10]))[0]  
        g_header_length = 14  
    else:  
        g_header_length = 6  
    g_code_length = int(g_code_length)  
    return g_code_length  
          
def parse_data(msg):  
    global g_code_length  
    g_code_length = ord(msg[1]) & 127  
    received_length = 0;  
    if g_code_length == 126:  
        g_code_length = struct.unpack('>H', str(msg[2:4]))[0]  
        masks = msg[4:8]  
        data = msg[8:]  
    elif g_code_length == 127:  
        g_code_length = struct.unpack('>Q', str(msg[2:10]))[0]  
        masks = msg[10:14]  
        data = msg[14:]  
    else:  
        masks = msg[2:6]  
        data = msg[6:]  
  
  
    i = 0  
    raw_str = ''  
  
  
    for d in data:  
        raw_str += chr(ord(d) ^ ord(masks[i%4]))  
        i += 1  
  
  
    print (u"总长度是：%d" % int(g_code_length))      
    return raw_str    
  
  
def sendMessage(message):  
    global connectionlist  
      
    message_utf_8 = message.encode('utf-8')  
    for connection in connectionlist.values():  
        back_str = []  
        back_str.append('\x81')  
        data_length = len(message_utf_8)  
  
  
        if data_length <= 125:  
            back_str.append(chr(data_length))  
        elif data_length <= 65535 :  
            back_str.append(struct.pack('b', 126))  
            back_str.append(struct.pack('>h', data_length))  
            #back_str.append(chr(data_length >> 8))  
            #back_str.append(chr(data_length & 0xFF))  
            #a = struct.pack('>h', data_length)  
            #b = chr(data_length >> 8)  
            #c = chr(data_length & 0xFF)  
        elif data_length <= (2^64-1):  
            #back_str.append(chr(127))  
            back_str.append(struct.pack('b', 127))  
            back_str.append(struct.pack('>q', data_length))  
            #back_str.append(chr(data_length >> 8))  
            #back_str.append(chr(data_length & 0xFF))        
        else :  
                print (u'太长了')          
        msg = ''  
        for c in back_str:  
            msg += c;  
        back_str = str(msg)   + message_utf_8#.encode('utf-8')      
        #connection.send(str.encode(str(u"\x00%s\xFF\n\n" % message))) #这个是旧版  
        #print (u'send message:' +  message)  
        if back_str != None and len(back_str) > 0:  
            print (back_str)  
            connection.send(back_str)  
  
  
def deleteconnection(item):  
    global connectionlist  
    del connectionlist['connection'+item]  
  
  
class WebSocket(threading.Thread):#继承Thread  
  
  
    GUID = "258EAFA5-E914-47DA-95CA-C5AB0DC85B11"  
  
  
    def __init__(self,conn,index,name,remote, path="/"):  
        threading.Thread.__init__(self)#初始化父类Thread  
        self.conn = conn  
        self.index = index  
        self.name = name  
        self.remote = remote  
        self.path = path  
        self.buffer = ""  
        self.buffer_utf8 = ""  
        self.length_buffer = 0  
    def run(self):#重载Thread的run  
        print('Socket%s Start!' % self.index)  
        headers = {}  
        self.handshaken = False  
  
  
        while True:  
            if self.handshaken == False:  
                print ('Socket%s Start Handshaken with %s!' % (self.index,self.remote))  
                self.buffer += bytes.decode(self.conn.recv(1024))  
  
  
                if self.buffer.find('\r\n\r\n') != -1:  
                    header, data = self.buffer.split('\r\n\r\n', 1)  
                    for line in header.split("\r\n")[1:]:  
                        key, value = line.split(": ", 1)  
                        headers[key] = value  
  
  
                    headers["Location"] = ("ws://%s%s" %(headers["Host"], self.path))  
                    key = headers['Sec-WebSocket-Key']  
                    token = b64encode(hashlib.sha1(str.encode(str(key + self.GUID))).digest())  
  
  
                    handshake="HTTP/1.1 101 Switching Protocols\r\n"\  
                        "Upgrade: websocket\r\n"\  
                        "Connection: Upgrade\r\n"\  
                        "Sec-WebSocket-Accept: "+bytes.decode(token)+"\r\n"\  
                        "WebSocket-Origin: "+str(headers["Origin"])+"\r\n"\  
                        "WebSocket-Location: "+str(headers["Location"])+"\r\n\r\n"  
  
  
                    self.conn.send(str.encode(str(handshake)))  
                    self.handshaken = True    
                    print ('Socket %s Handshaken with %s success!' %(self.index, self.remote))    
                    sendMessage(u'Welcome, ' + self.name + ' !')    
                    self.buffer_utf8 = ""  
                    g_code_length = 0                      
  
  
            else:  
                global g_code_length  
                global g_header_length  
                mm=self.conn.recv(128)  
                if len(mm) <= 0:  
                    continue  
                if g_code_length == 0:  
                    get_datalength(mm)  
                #接受的长度  
                self.length_buffer = self.length_buffer + len(mm)  
                self.buffer = self.buffer + mm  
                if self.length_buffer - g_header_length < g_code_length :  
                    continue  
                else :  
                    self.buffer_utf8 = parse_data(self.buffer) #utf8                  
                    msg_unicode = str(self.buffer_utf8).decode('utf-8', 'ignore') #unicode  
                    if msg_unicode=='quit':  
                        print (u'Socket%s Logout!' % (self.index))  
                        nowTime = time.strftime('%H:%M:%S',time.localtime(time.time()))  
                        sendMessage(u'%s %s say: %s' % (nowTime, self.remote, self.name+' Logout'))                        
                        deleteconnection(str(self.index))  
                        self.conn.close()  
                        break #退出线程  
                    else:  
                        #print (u'Socket%s Got msg:%s from %s!' % (self.index, msg_unicode, self.remote))  
                        nowTime = time.strftime(u'%H:%M:%S',time.localtime(time.time()))  
                        sendMessage(u'%s %s say: %s' % (nowTime, self.remote, msg_unicode))    
                    #重置buffer和bufferlength  
                    self.buffer_utf8 = ""  
                    self.buffer = ""  
                    g_code_length = 0  
                    self.length_buffer = 0  
            self.buffer = ""  
  
  
class WebSocketServer(object):  
    def __init__(self):  
        self.socket = None  
    def begin(self):  
        print( 'WebSocketServer Start!')  
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
        self.socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)  
        self.socket.bind(("127.0.0.1",12345))  
        self.socket.listen(50)  
  
  
        global connectionlist  
  
  
        i=0  
        while True:  
            connection, address = self.socket.accept()  
  
  
            username=address[0]       
            newSocket = WebSocket(connection,i,username,address)  
            newSocket.start() #开始线程,执行run函数  
            connectionlist['connection'+str(i)]=connection  
            i = i + 1  
  
  
if __name__ == "__main__":  
    server = WebSocketServer()  
    server.begin()  

客户端 
测试了chrome37, firefox35

[html] view plain copy 在CODE上查看代码片派生到我的代码片
<!DOCTYPE html>  
<html>  
<head>  
    <title>WebSocket</title>  
  
    <style>  
        html, body {  
            font: normal 0.9em arial, helvetica;  
        }  
  
        #log {  
            width: 440px;  
            height: 200px;  
            border: 1px solid #7F9DB9;  
            overflow: auto;  
        }  
  
        #msg {  
            width: 330px;  
        }  
    </style>  
  
    <script>  
        var socket;  
  
        function init() {  
            var host = "ws://127.0.0.1:12345/";  
            try {  
                socket = new WebSocket(host);  
                socket.onopen = function (msg) {  
                    log('Connected');  
                };  
                socket.onmessage = function (msg) {  
                    log(msg.data);  
                };  
                socket.onclose = function (msg) {  
                    log("Lose Connection!");  
                };  
            }  
            catch (ex) {  
                log(ex);  
            }  
            $("msg").focus();  
        }  
  
        function send() {  
            var txt, msg;  
            txt = $("msg");  
            msg = txt.value;  
            if (!msg) {  
                alert("Message can not be empty");  
                return;  
            }  
            txt.value = "";  
            txt.focus();  
            try {  
                socket.send(msg);  
            } catch (ex) {  
                log(ex);  
            }  
        }  
  
        window.onbeforeunload = function () {  
            try {  
                socket.send('quit');  
                socket.close();  
                socket = null;  
            }  
            catch (ex) {  
                log(ex);  
            }  
        };  
  
  
        function $(id) {  
            return document.getElementById(id);  
        }  
        function log(msg) {  
            $("log").innerHTML += "<br>" + msg;  
        }  
        function onkey(event) {  
            if (event.keyCode == 13) {  
                send();  
            }  
        }  
    </script>  
  
</head>  
  
  
<body onload="init()">  
<h3>WebSocket</h3>  
<br><br>  
  
<div id="log"></div>  
<input id="msg" type="textbox" onkeypress="onkey(event)"/>  
<button onclick="send()">发送</button>  
</body>  
  
</html>  

参考:用Python实现一个简单的WebSocket服务器

由于使用125, 126, 127用作标志位.
