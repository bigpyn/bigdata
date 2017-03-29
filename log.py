 # -*-coding:utf-8-*- 
"""
Author：yinshunyao
Date:2017/3/5 0005下午 10:50
"""
# import logging
import os
import time
# 利用第三方系统锁实现文件锁定和解锁
if os.name == 'nt':
	import win32con, win32file, pywintypes
    LOCK_EX = win32con.LOCKFILE_EXCLUSIVE_LOCK
    LOCK_SH = 0  # The default value
    LOCK_NB = win32con.LOCKFILE_FAIL_IMMEDIATELY
    __overlapped = pywintypes.OVERLAPPED()


    def lock(file, flags):
        hfile = win32file._get_osfhandle(file.fileno())
        win32file.LockFileEx(hfile, flags, 0, 0xffff0000, __overlapped)

    def unlock(file):
        hfile = win32file._get_osfhandle(file.fileno())
        win32file.UnlockFileEx(hfile, 0, 0xffff0000, __overlapped)

elif os.name == 'posix':
    from fcntl import LOCK_EX


    def lock(file, flags):
        fcntl.flock(file.fileno(), flags)

    def unlock(file):
        fcntl.flock(file.fileno(), fcntl.LOCK_UN)
else:
    raise RuntimeError("File Locker only support NT and Posix platforms!")
 



class _Logger:
    file_path = ''
    #初始化日志路径

    @staticmethod
    def init():

        if not _Logger.file_path:
            _Logger.file_path = '%s/Log' % os.path.abspath(os.path.dirname(__file__))
        return True


    @staticmethod
    def _write(messge, file_name):
        if not messge:
            return True
        messge = messge.replace('\t', ',')
        file = '{}/{}'.format(_Logger.file_path, file_name)
        while True:
            try:
                f = open(file, 'a+')
                lock(f, LOCK_EX)
                break
            except:
                time.sleep(0.01)
                continue

        # 确保缓冲区内容写入到文件
        while True:
            try:
                f.write(messge + '\n')
                f.flush()
                break
            except:
                time.sleep(0.01)
                continue

        while True:
            try:
                unlock(f)
                f.close()
                return True
            except:
                time.sleep(0.01)
                continue
    
    @staticmethod
    def write(message, file_name, only_print=False):
        if not _Logger.init(): return
        print(message)
        if not only_print:
            _Logger._write(message, file_name)



class Logger:
    def __init__(self, logger_name, file_name=''):
        self.logger_name = logger_name
        self.file_name = file_name
    # 根据消息级别，自定义格式，生成消息

    def _build_message(self, message, level):
        try:
            return '[%s]\t[%5s]\t[%8s]\t%s' \
                   % (time.strftime('%Y-%m-%d %H:%M:%S'), level, self.logger_name, message)
        except Exception as e:
            print('解析日志消息异常：{}'.format(e))
            return ''


    def warning(self, message):
        _Logger.write(self._build_message(message, 'WARN'), self.file_name)

    def warn(self, message):
        _Logger.write(self._build_message(message, 'WARN'), self.file_name)

    def error(self, message):
        _Logger.write(self._build_message(message, 'ERROR'), self.file_name)

    def info(self, message):
        _Logger.write(self._build_message(message, 'INFO'), self.file_name, True)

    def debug(self, message):
        _Logger.write(self._build_message(message, 'DEBUG'), self.file_name)
 
# 循环打印日志测试函数


def _print_test(count):
    logger = Logger(logger_name='test{}'.format(count), file_name='test{}'.format(count % 3))
    key = 0
    while True:
        key += 1
        # print('{}-{}'.format(logger, key))
        logger.debug('%d' % key)
        logger.error('%d' % key)


if __name__ == '__main__':
    from multiprocessing import Pool, freeze_support
    freeze_support()
    # 进程池进行测试
    pool = Pool(processes=20)
    count = 0
    while count < 20:
        count += 1
        pool.apply_async(func=_print_test, args=(count,))
    else:
        pool.close()
        pool.join()
 
