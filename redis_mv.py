import redis
import datetime

class Database:
	def __init__(self):
		self.host = 'localhost'
		self.port = 6379
		self.write_pool = {}
		self.read_pool = []
		
	def write(self,website,city,year,month,day,deal_number):
		try:
			key = '_'.join([website,city,str(year),str(month),str(day)])
			val = deal_number
			r = redis.StrictRedis(host = self.host,port = self.port)
			r.set(key,val)
		except exception:
			print (exception)
			
	def add_write(self,website,city,year,month,day,deal_number):
		key = '_'.join([website,city,str(year),str(month),str(day)])
		val = deal_number
		self.write_pool[key] = val
	
	def batch_write(self):
		try:
			r = redis.StrictRedis(host=self.host,port=self.port)
			r.mset(self.write_pool)
		except exception:
			print(exception)
	
	def read(self,website,city,year,month,day):
		try:
			key = '_'.join([website,city,str(year),str(month),str(day)])
			r = redis.StrictRedis(host=self.host,port = self.port)
			value = r.get(key)
			print (value)
			return value
		except exception:
			print (exception)
	
	def add_read(self,website,city,year,month,day):
			key = '_'.join([website,city,str(year),str(month),str(day)])
			self.read_pool.append(key)
			
	def batch_read(self):
		try:
			r = redis.StrictRedis(host=self.host,port=self.port)
			val = r.mget(self.read_pool)
			print(val)
			return val
		except exception:
			print(exception)

def single_write():
		beg = datetime.datetime.now()
		db = Database()
		for i in range(1,10001):
			db.write('meituan','beijing',i,9,1,i)
		end = datetime.datetime.now()
		print (end-beg)
	
def batch_write():
		beg = datetime.datetime.now()
		db = Database()
		for i in range(1,10001):
			db.add_write('meituan','beijing',i,9,1,i)
		db.batch_write()
		end = datetime.datetime.now()
		print(end-beg)

def single_read():
		beg = datetime.datetime.now()
		db = Database()
		for i in range(1,10001):
			db.read('meituan','beijing',i,9,1)
		db.batch_read()
		end = datetime.datetime.now()
		print (end-beg)

def batch_read():
		beg = datetime.datetime.now()
		db = Database()
		for i in range(1,10001):
			db.add_read('meituan','beijign',i,9,1)
		db.batch_read()
		end = datetime.datetime.now()
		print (end-beg)
			
if __name__ == '__main__':
	#db = Database()
	#db.write('meituan','beijing',2013,9,1,8000)
	#db.read('meituan','beijing',2013,9,1)
	#single_write()
	batch_write()
	#single_read()
	batch_read()
	
		
