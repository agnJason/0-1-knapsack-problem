
# coding: utf-8

# In[1]:


import pandas as pd
weight = [0,2,2,6,5,4]
value =  [0,6,3,5,4,6]
c = [[]]
#生成i个元素*w个容量的矩阵 若第i个能放到w个容量里，将value[i]+c[i-1][w-weight[i]]和 c[i-1][w]的最大值赋予c[i][w]
for i in range(6):
    for w in range(11):
        c[i].append(0)
        if weight[i] <= w and i>0:
            c[i][w] = max(c[i-1][w-weight[i]]+value[i], c[i-1][w])
        else:
            c[i][w] = c[i-1][w]
    c.append([])
result = pd.DataFrame(c[1:6])
print(result)


# In[2]:


x = {}
w = 10#保存剩余weight
#倒推 若c[i][w]不等于c[i-1][w]则表示放入了第i个元素，将w减去用的weight[i]，在将i从5-1遍历
for i in range(5,0,-1):
    if c[i][w] == c[i-1][w]:
        x[i]=0
    else:
        x[i]=1
        w-=weight[i]
        
print("五个元素的使用量：", x, "最大存放value：", c[5][-1], "最终剩余weight：", w)


# In[3]:


weight = [2,2,6,5,4]
value =  [6,3,5,4,6]
w = 10
v = 0
dict_ = {1:0, 2:0, 3:0, 4:0, 5:0}
index = [ v/w for w, v in zip(weight, value)] #每个元素的单位价值
 
#计算每个元素的单位价值排名
sort_ = [1]*5
for i in range(5):
    for j in range(i+1, 5):
        if index[i]<index[j]:
            sort_[i] += 1
        else:
            sort_[j] += 1
            
#从排名1开始塞东西            
rank = 1
while w>0:
    i = sort_.index(rank)
    if w>weight[i]:
        w -= weight[i]
        v += value[i]
        dict_[i+1] = 1
    else:
        v += value[i]*w/weight[i]
        dict_[i+1] = w/weight[i]
        w = 0
    rank += 1
    
print("五个元素的使用量：", dict_, "最大存放value：", v, "最终剩余weight：", w)

