import tornado.ioloop #事件循环
import tornado.web #基本控件

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello world")

def main():
    app = tornado.web.Application([r"/", MainHandler]) #数组里是定义路由
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()

if __name__ == '__main__':
    main()
