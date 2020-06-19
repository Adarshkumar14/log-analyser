#!/usr/bin/env python
# coding: utf-8

# In[67]:


import pandas as pd


# In[68]:


dataset = pd.read_csv('/root/access_log.csv',header=None,delim_whitespace=True)


# In[69]:


dataset.head(10)


# In[70]:


dataset=dataset.rename(columns = {0:'ip'})
dataset=dataset.rename(columns = {5:'webaddress'})
dataset=dataset.rename(columns = {6:'status'})


# In[71]:


dataset.head(30)


# In[72]:


ip_times=dataset.pivot_table(index=['ip'],aggfunc='size')


# In[73]:


dataset['ip'].unique().tolist()


# In[74]:


ip_times


# In[75]:


status_times=dataset.pivot_table(index=['ip','status',],aggfunc='size')


# In[76]:


status_times


# In[77]:





df = status_times.to_frame().reset_index()


# In[78]:


df


# In[79]:


df=df.rename(columns = {0:'count'})


# In[80]:


df


# In[81]:


import ipaddress


# In[82]:


x=0
for i in df['ip']:
     df['ip'][x]=int(ipaddress.IPv4Address(i))
     x=x+1


# In[83]:


df['ip'].max()


# In[84]:


import matplotlib.pyplot as plt


# In[85]:


ip=df['ip']


# In[86]:


status=df['status']


# In[87]:


count=df['count']


# In[88]:


dataset.columns


# In[89]:


plt.scatter(ip, status)
plt.xlabel('ip')
plt.ylabel('rq')


# In[90]:


from sklearn.preprocessing import StandardScaler


# In[91]:


sc = StandardScaler()


# In[92]:


data_scaled = sc.fit_transform(df)


# In[93]:


data_scaled


# In[94]:


from sklearn.cluster import KMeans


# In[95]:


model = KMeans(n_clusters=2)


# In[96]:


model.fit(data_scaled)


# In[97]:


pred  = model.fit_predict(data_scaled)


# In[98]:


df.columns


# In[99]:


pred


# In[100]:


dataset_scaled = pd.DataFrame(data_scaled, columns=['ip', 'status','count'])


# In[101]:


dataset_scaled


# In[102]:


data_scaled


# In[103]:


dataset_scaled['cluster name'] = pred


# In[104]:


dataset_scaled


# In[105]:


df['cluster name'] = pred


# In[106]:


x=0
for i in df['ip']:
  df['ip'][x]=str(ipaddress.IPv4Address(i))
  x=x+1


# In[107]:


df.head(60)


# In[108]:


plt.scatter(df['ip'],df['count'], c=df['cluster name'])


# In[109]:


plt.scatter(dataset_scaled['ip'], dataset_scaled['count'], c=dataset_scaled['cluster name'])


# In[205]:


df[df['cluster name']==1]


# In[324]:



 

mal_ip=[]
mal_ip[:]=df[df['cluster name']==0].iloc[:]['ip']


# In[325]:


type(mal_ip)
#mal_ip=mal_ip.to_frame()


# In[332]:


file1=open("/root/malicious_ip.txt","w")
for i in mal_ip:
 #file1.write(str(i))
 L=i+"\n"
 file1.writelines(L)
 
file1.close()


# In[333]:


print('completed!!')
# In[339]:





# In[ ]:




