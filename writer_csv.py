import csv
def save2csv(file_name=None,header=None,data=None):
	if file_name is None or isinstance(file_name,str) is False:
		raise Exception('保存csv文件名不能为空，并且必须为字符串类型')
	if file_name.endswith('.csv') is False:
		file_name +='.csv'
	file_obj = open(file_name,'w',encoding='utf8',newline='')
	#file_obj.write(codecs.BOM_UTF8)
	writer = csv.writer(file_obj)
	if data is None or isinstance(data,(tuple,list)) is False:
		raise Exception('保存csv文件失败，数据为空或者不是数据类型')
	if header is not None and isinstance(header,(tuple,list)) is True:
		writer.writerow(header)
	for row in data:
		#print(row)
		writer.writerow(row)

#save2csv('111',({'k','v'}),['1','2','3','4'])
save2csv('111',({'k','v'}),({'保存','件失'},{'数据为','或者'}))
#Python写csv文件
