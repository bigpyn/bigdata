#!/usr/bin/env python
# -*- coding:utf-8 -*-
import tornado.ioloop
import tornado.web

IMG_LIST = []
class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html', img_list=IMG_LIST)
    def post(self, *args, **kwargs):
        print(self.get_argument('user'))
        print(self.get_arguments('favor'))
        file_metas = self.request.files["fafafa"]
        # print(file_metas)
        for meta in file_metas:
            # 要上传的文件名
            file_name = meta['filename']
            import os
            with open(os.path.join('statics', 'img', file_name), 'wb') as up:
                up.write(meta['body'])
            IMG_LIST.append(file_name)
        self.write('{"status": 1, "message": "mmmm"}')

settings = {
    'template_path': 'views',
    'static_path': 'statics',
    'static_url_prefix': '/statics/',
}

application = tornado.web.Application([
    (r"/index", IndexHandler),
], **settings)


if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
