l = [1,2,3,4,5,6,3,4,6,3,4,5,6,23,5,1]
set(l)
print(list(set(l)))
#对list数据，驱虫方式如下:
list_origin = ["aaa","ccc","bbb","aaa","ddd","bbb"]
#进行去重，获得新的列表new_list:
new_list = list(set(list_origin))
print(new_list)
#第二种方法，可以借用dictionary 中不能有重复出现的key的思想即可完成去重的功能:
list_origin = ["aaa","ccc","bbb","aaa","ddd","bbbb"]
#将列表内容添加到字典中:
dict_tmp = {}
for single_value in list_origin:
    dict_tmp[single_value] = ""

print(dict_tmp[single_value])

list1=[1,2,2,3,4,5]
list2 = []
[list2.append(i) for i in list1 if i not in list2]
print(list2)
#字典去重
list1 = [1,2,3,4,5,6,3,4,5]

aa = {}.fromkeys(list1).keys()

print (aa)
#使用itertools去重
import itertools
ids = [1,4,3,3,4,2,3,4,5,6,1]
ids.sort()
it = itertools.groupby(ids)

for k,g in it:
     print (k)


#mailto = ['cc','bbbb','afa','sss','bbbb','cc','shafa']
#b = sorted(list(set(mailto)), key = mailto.index)
#print(b)
