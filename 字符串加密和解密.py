#!/usr/bin/env python
# coding: utf-8

# In[5]:


#编写函数实现字符串加密和解密，循环使用指定密钥，采用简单的异或算法

def crypt(scource,key):
    from itertools import cycle #itertools 是python的迭代器模块，itertools提供的工具相当高效且节省内存
    result = ''                 #使用这些工具，能够创建自己定制的迭代器用于高效率的循环-无限迭代器，
    temp = cycle(key)           #itertools包自带三个可以无限迭代的迭代器。
    for ch in scource:
        result=result + chr(ord(ch) ^ ord(next(temp)))
    return result
source = 'Shandong Institude of Business and Technology'
key = 'Dong Fuguo'

print('Before Encrypted:'+source)
encrypted=crypt(source,key)
print('After Encrypte'+encrypted)
decrypted=crypt(encrypted,key)
print('After Decrpted:'+decrypted)


# In[ ]:




