# import pdb
# pdb.set_trace()

# or
# python -m pdb pdb_example.py


# set break point
# b
# b pdb_example.py:16, i > 50  在i大于50时，设置断点
# tbreak pdb_example.py:16, i > 50 临时断点，执行后就被消除
# disable 1 ，取消第一个断点 
# clear 1 清除

print('start\n\n\n\n')
for i in range(100):
    print(i)
print('end\n\n\n\n')
