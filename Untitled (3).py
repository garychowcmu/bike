
# coding: utf-8

# ### this part below combines all months data for one city in 2020

# In[3]:


import os
import glob
import pandas as pd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

bikeAllMonth2019 = None
aa = 'csv'  #后缀为csv格式的文件
a = [i for i in glob.glob('*.{}'.format(aa))]  #加载所有后缀为csv的文件。
frames = []
city = 'Boston' # specify the city name, then the output combined csv will be for boston only
for i in a:
    print(i)
    if '2020' in i:#specify the years you want it to read
        frames.append(pd.read_csv(i))
        print('True')
bikeAllMonth = pd.concat(frames)  #合并
        
bikeAllMonth.to_csv("%s2020.csv"%city, index=False, encoding='utf-8-sig') #输出


bikeAllMonth = pd.read_csv("%s2020.csv"%city, parse_dates=['starttime']) #将starttime处理为标准时间格式

bikeAllMonth['day'] = bikeAllMonth['starttime'].dt.day #提取starttime日期，之后做weekday&weekend分组
bikeAllMonth['hour'] = bikeAllMonth['starttime'].dt.hour #提取starttime小时，之后做hour分组
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None) #这两行是为了让pycharm完整显示处理结果


# In[4]:


bikeAllMonth[:10]


# ### this part below combines all months data for one city in 2020

# In[5]:


import os
import glob
import pandas as pd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

bikeAllMonth2019 = None
aa = 'csv'  #后缀为csv格式的文件
a = [i for i in glob.glob('*.{}'.format(aa))]  #加载所有后缀为csv的文件。
frames = []
city = 'Boston'# specify the city name, then the output combined csv will be for boston only
for i in a:
    print(i)
    if '2018' in i: #specify the years you want it to read
        frames.append(pd.read_csv(i))
        print('True')
bikeAllMonth2019 = pd.concat(frames)  #合并
        
bikeAllMonth2019.to_csv("%s2019.csv"%city, index=False, encoding='utf-8-sig') #输出


bikeAllMonth2019 = pd.read_csv("%s2019.csv"%city, parse_dates=['starttime']) #将starttime处理为标准时间格式

bikeAllMonth2019['day'] = bikeAllMonth2019['starttime'].dt.day #提取starttime日期，之后做weekday&weekend分组
bikeAllMonth2019['hour'] = bikeAllMonth2019['starttime'].dt.hour #提取starttime小时，之后做hour分组
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None) #这两行是为了让pycharm完整显示处理结果


# In[6]:


bikeAllMonth2019[:10]


# In[11]:


# count number of trips by day
import datetime
bikeAllMonth['Month/Day'] = bikeAllMonth['starttime'].apply(lambda x: "%s-%f" % (x.month, x.day/10)) # this part creates a new column, specifying the month and day
everydayCount = bikeAllMonth['Month/Day'].value_counts() # count unique values of 'Month/Day' column
everydayCount = everydayCount.to_frame()
everydayCount = everydayCount.sort_index()
# plot the trip numbers as y axix, date as x axis
everydayCount.plot(figsize = (20,10))

# manually set the x axis
minDate = bikeAllMonth['starttime'].min()
date_list = [minDate + datetime.timedelta(days=x) for x in range(len(everydayCount))]
date_list_7days = [str(date_list[i].month) + "-"+str(date_list[i].day) for i in range(0,len(date_list),14)]
plt.xticks(np.arange(0,len(everydayCount),14),date_list_7days,fontsize = 20)


# In[12]:


# do the same for 2019
bikeAllMonth2019['Month/Day'] = bikeAllMonth2019['starttime'].apply(lambda x: "%d-%f" % (x.month, x.day/10))
everydayCount2019 = bikeAllMonth2019['Month/Day'].value_counts()
everydayCount2019 = everydayCount2019.to_frame()
everydayCount2019 = everydayCount2019.sort_index()


# In[13]:


everydayCount


# In[14]:


# plot 2020 and 2019 altogether

everydayCount.plot(figsize = (20,10))
plt.plot(everydayCount2019)
labels = ['2020','2019']
plt.legend(labels)
# manually set the x axis
minDate = bikeAllMonth['starttime'].min()
date_list = [minDate + datetime.timedelta(days=x) for x in range(len(everydayCount))]
date_list_7days = [str(date_list[i].month) + "-"+str(date_list[i].day) for i in range(0,len(date_list),14)]
plt.xticks(np.arange(0,len(everydayCount),14),date_list_7days,fontsize = 20)


# ### Now let's fo comparison, first, comparison within the SAME YEAR

# In[15]:


plt.figure(figsize = (20,10))

# select a subset from all data for subscriber
bikeAllMonthSelected = bikeAllMonth[bikeAllMonth.usertype == 'Subscriber'] 
everydayCountSelected = bikeAllMonthSelected['Month/Day'].value_counts()
everydayCountSelected
everydayCountSelected = everydayCountSelected.to_frame()
everydayCountSelected = everydayCountSelected.sort_index()

# select a subset from all data for customer
bikeAllMonthSelectedOther = bikeAllMonth[bikeAllMonth.usertype == 'Customer'] 
everydayCountSelectedOther = bikeAllMonthSelectedOther['Month/Day'].value_counts()
everydayCountSelected
everydayCountSelectedOther = everydayCountSelectedOther.to_frame()
everydayCountSelectedOther = everydayCountSelectedOther.sort_index()

everydayCountSelected.plot(figsize = (20,10))
plt.plot(everydayCountSelectedOther)

# plt.xticks([])
plt.xticks(rotation = 20,fontsize = 20) # here you can sepcify fontsize
labels = ['Subscriber','Customer']
plt.legend(labels,fontsize = 20) # here you can sepcify fontsize
# manually set the x axis
minDate = bikeAllMonth['starttime'].min()
date_list = [minDate + datetime.timedelta(days=x) for x in range(len(everydayCountSelected))]
date_list_7days = [str(date_list[i].month) + "-"+str(date_list[i].day) for i in range(0,len(date_list),14)]
plt.xticks(np.arange(0,len(everydayCountSelected),14),date_list_7days,fontsize = 20)


# In[16]:


plt.figure(figsize = (20,10))

# another example for birthyear


# select a subset from all data for Adult, older
bikeAllMonthSelected = bikeAllMonth[(bikeAllMonth['birth year'] >= 1975) & (bikeAllMonth['birth year'] <= 1996)]
everydayCountSelected = bikeAllMonthSelected['Month/Day'].value_counts()
everydayCountSelected
everydayCountSelected = everydayCountSelected.to_frame()
everydayCountSelected = everydayCountSelected.sort_index()

# select a subset from all data for TEENS, younger
bikeAllMonthSelectedOther = bikeAllMonth[(bikeAllMonth['birth year'] >= 1997) & (bikeAllMonth['birth year'] <= 2020)] 
everydayCountSelectedOther = bikeAllMonthSelectedOther['Month/Day'].value_counts()
everydayCountSelected
everydayCountSelectedOther = everydayCountSelectedOther.to_frame()
everydayCountSelectedOther = everydayCountSelectedOther.sort_index()

everydayCountSelected.plot(figsize = (20,10))
plt.plot(everydayCountSelectedOther)

# plt.xticks([])
plt.xticks(rotation = 20,fontsize = 20) # here you can sepcify fontsize
labels = ['Adult','Teens']
plt.legend(labels,fontsize = 20) # here you can sepcify fontsize
# manually set the x axis
minDate = bikeAllMonth['starttime'].min()
date_list = [minDate + datetime.timedelta(days=x) for x in range(len(everydayCountSelected))]
date_list_7days = [str(date_list[i].month) + "-"+str(date_list[i].day) for i in range(0,len(date_list),14)]
plt.xticks(np.arange(0,len(everydayCountSelected),14),date_list_7days,fontsize = 20)



# In[17]:


plt.figure(figsize = (20,10))

# another example for GENDER


# select a subset from all data for gender
bikeAllMonthSelected = bikeAllMonth[(bikeAllMonth['gender'] == 1)]
everydayCountSelected = bikeAllMonthSelected['Month/Day'].value_counts()
everydayCountSelected
everydayCountSelected = everydayCountSelected.to_frame()
everydayCountSelected = everydayCountSelected.sort_index()

# select a subset from all data for gender
bikeAllMonthSelectedOther = bikeAllMonth[(bikeAllMonth['gender'] == 2)] 
everydayCountSelectedOther = bikeAllMonthSelectedOther['Month/Day'].value_counts()
everydayCountSelected
everydayCountSelectedOther = everydayCountSelectedOther.to_frame()
everydayCountSelectedOther = everydayCountSelectedOther.sort_index()

everydayCountSelected.plot(figsize = (20,10))
plt.plot(everydayCountSelectedOther)

# plt.xticks([])
plt.xticks(rotation = 20,fontsize = 20) # here you can sepcify fontsize
labels = ['Male','Female']
plt.legend(labels,fontsize = 20) # here you can sepcify fontsize

# manually set the x axis
minDate = bikeAllMonth['starttime'].min()
date_list = [minDate + datetime.timedelta(days=x) for x in range(len(everydayCountSelected))]
date_list_7days = [str(date_list[i].month) + "-"+str(date_list[i].day) for i in range(0,len(date_list),14)]
plt.xticks(np.arange(0,len(everydayCountSelected),14),date_list_7days,fontsize = 20)


# ### Now let's DO TRIP COUNTS comparison, comparison across DIFFERENT YEARS
# 

# In[18]:


# NOW, lets look at FEMALE IN 2020 AND 2019. TRIP COUNTS

#this is 2020

plt.figure(figsize = (20,10))
bikeAllMonthSelected = bikeAllMonth[bikeAllMonth.gender == 2] # select female only for 2020
everydayCountSelected = bikeAllMonthSelected['Month/Day'].value_counts()
everydayCountSelected
everydayCountSelected = everydayCountSelected.to_frame()
everydayCountSelected = everydayCountSelected.sort_index()

#this is 2019

bikeAllMonthSelectedOther = bikeAllMonth2019[bikeAllMonth2019.gender == 2] # select female only for 2019
everydayCountSelectedOther = bikeAllMonthSelectedOther['Month/Day'].value_counts()
everydayCountSelected
everydayCountSelectedOther = everydayCountSelectedOther.to_frame()
everydayCountSelectedOther = everydayCountSelectedOther.sort_index()


# now lets start plotting 2020 and then 2019
everydayCountSelected.plot(figsize = (20,10))
plt.plot(everydayCountSelectedOther)

# plt.xticks([])
plt.xticks(rotation = 20)
labels = ['2020','2019']
plt.legend(labels,fontsize = 20)
plt.title('Female TRIP COUNTS in 2019 and 2020, trip counts',fontsize = 20)
# manually set the x axis
minDate = bikeAllMonth['starttime'].min()
date_list = [minDate + datetime.timedelta(days=x) for x in range(len(everydayCountSelected))]
date_list_7days = [str(date_list[i].month) + "-"+str(date_list[i].day) for i in range(0,len(date_list),14)]
plt.xticks(np.arange(0,len(everydayCountSelected),14),date_list_7days,fontsize = 20)


# In[19]:



# NOW, lets look at MALE IN 2020 AND 2019. TRIP COUNTS

#this is 2020

plt.figure(figsize = (20,10))
bikeAllMonthSelected = bikeAllMonth[bikeAllMonth.gender == 1] # select male only for 2020
everydayCountSelected = bikeAllMonthSelected['Month/Day'].value_counts()
everydayCountSelected
everydayCountSelected = everydayCountSelected.to_frame()
everydayCountSelected = everydayCountSelected.sort_index()

#this is 2019

bikeAllMonthSelectedOther = bikeAllMonth2019[bikeAllMonth2019.gender == 1] # select male only for 2019
everydayCountSelectedOther = bikeAllMonthSelectedOther['Month/Day'].value_counts()
everydayCountSelected
everydayCountSelectedOther = everydayCountSelectedOther.to_frame()
everydayCountSelectedOther = everydayCountSelectedOther.sort_index()

# now lets start plotting 2020 and then 2019

everydayCountSelected.plot(figsize = (20,10))
plt.plot(everydayCountSelectedOther)

# plt.xticks([])
plt.xticks(rotation = 20)
labels = ['2020','2019']
plt.legend(labels,fontsize = 20)
plt.title('Male TRIP COUNTS in 2019 and 2020, trip counts',fontsize = 20)
# manually set the x axis
minDate = bikeAllMonth['starttime'].min()
date_list = [minDate + datetime.timedelta(days=x) for x in range(len(everydayCountSelected))]
date_list_7days = [str(date_list[i].month) + "-"+str(date_list[i].day) for i in range(0,len(date_list),14)]
plt.xticks(np.arange(0,len(everydayCountSelected),14),date_list_7days,fontsize = 20)


# In[20]:


# NOW, lets look at ELDERs IN 2020 AND 2019.TRIP COUNTS

#this is 2020

plt.figure(figsize = (20,10))
bikeAllMonthSelected = bikeAllMonth[(bikeAllMonth['birth year'] >= 1945) & (bikeAllMonth['birth year'] <= 1975)] # elders only
everydayCountSelected = bikeAllMonthSelected['Month/Day'].value_counts()
everydayCountSelected
everydayCountSelected = everydayCountSelected.to_frame()
everydayCountSelected = everydayCountSelected.sort_index()

#this is 2019

bikeAllMonthSelectedOther = bikeAllMonth2019[(bikeAllMonth2019['birth year'] >= 1945) & (bikeAllMonth2019['birth year'] <= 1975)] # elders
everydayCountSelectedOther = bikeAllMonthSelectedOther['Month/Day'].value_counts()
everydayCountSelected
everydayCountSelectedOther = everydayCountSelectedOther.to_frame()
everydayCountSelectedOther = everydayCountSelectedOther.sort_index()

# now lets start plotting 2020 and then 2019

everydayCountSelected.plot(figsize = (20,10))
plt.plot(everydayCountSelectedOther)

# plt.xticks([])
plt.xticks(rotation = 20)
labels = ['2020','2019']
plt.legend(labels,fontsize = 20)
plt.title('Elders TRIP COUNTS in 2019 and 2020, trip counts',fontsize = 20)
# manually set the x axis
minDate = bikeAllMonth['starttime'].min()
date_list = [minDate + datetime.timedelta(days=x) for x in range(len(everydayCountSelected))]
date_list_7days = [str(date_list[i].month) + "-"+str(date_list[i].day) for i in range(0,len(date_list),14)]
plt.xticks(np.arange(0,len(everydayCountSelected),14),date_list_7days,fontsize = 20)


# In[21]:


# NOW, more importantly, we can compare trip counts of longer trips (trip duration > 1800 seconds (0.5 hr), and < 3600 seconds (1 hr))

#TRIP COUNTS
#this is 2020
plt.figure(figsize = (20,10))
bikeAllMonthSelected = bikeAllMonth[(bikeAllMonth['tripduration'] >= 1800) & (bikeAllMonth['tripduration'] <= 3600)] # selecting trip duration > 1800 seconds (0.5 hr), and < 3600 seconds (1 hr)
everydayCountSelected = bikeAllMonthSelected['Month/Day'].value_counts()
everydayCountSelected
everydayCountSelected = everydayCountSelected.to_frame()
everydayCountSelected = everydayCountSelected.sort_index()

#this is 2019

bikeAllMonthSelectedOther = bikeAllMonth2019[(bikeAllMonth2019['tripduration'] >= 1800) & (bikeAllMonth2019['tripduration'] <= 3600)]
everydayCountSelectedOther = bikeAllMonthSelectedOther['Month/Day'].value_counts()
everydayCountSelected
everydayCountSelectedOther = everydayCountSelectedOther.to_frame()
everydayCountSelectedOther = everydayCountSelectedOther.sort_index()

# now lets start plotting 2020 and then 2019

everydayCountSelected.plot(figsize = (20,10))
plt.plot(everydayCountSelectedOther)

# plt.xticks([])
plt.xticks(rotation = 20)
labels = ['2020','2019']
plt.legend(labels,fontsize = 20)
plt.title('Longer trips TRIP COUNTS (0.5 to 1 hr) in 2019 and 2020, trip counts',fontsize = 20)

# manually set the x axis
minDate = bikeAllMonth['starttime'].min()
date_list = [minDate + datetime.timedelta(days=x) for x in range(len(everydayCountSelected))]
date_list_7days = [str(date_list[i].month) + "-"+str(date_list[i].day) for i in range(0,len(date_list),14)]
plt.xticks(np.arange(0,len(everydayCountSelected),14),date_list_7days,fontsize = 20)


# In[22]:


# NOW, lets look at AM PEAK IN 2020 AND 2019.TRIP COUNTS, 

#this is 2020


plt.figure(figsize = (20,10))
# select 7 to 12 am
bikeAllMonthSelected = bikeAllMonth[(bikeAllMonth.starttime.dt.hour >= 7) & (bikeAllMonth.starttime.dt.hour <= 12)] # AM PEAK 
everydayCountSelected = bikeAllMonthSelected['Month/Day'].value_counts()
everydayCountSelected
everydayCountSelected = everydayCountSelected.to_frame()
everydayCountSelected = everydayCountSelected.sort_index()

#this is 2019

bikeAllMonthSelectedOther = bikeAllMonth2019[(bikeAllMonth2019.starttime.dt.hour >= 7) & (bikeAllMonth2019.starttime.dt.hour <= 12)] # AM PEAK 
everydayCountSelectedOther = bikeAllMonthSelectedOther['Month/Day'].value_counts()
everydayCountSelected
everydayCountSelectedOther = everydayCountSelectedOther.to_frame()
everydayCountSelectedOther = everydayCountSelectedOther.sort_index()

# now lets start plotting 2020 and then 2019

everydayCountSelected.plot(figsize = (20,10))
plt.plot(everydayCountSelectedOther)

# plt.xticks([])
plt.xticks(rotation = 20)
labels = ['2020','2019']
plt.legend(labels,fontsize = 20)
plt.title('AM TRIP COUNTS in 2019 and 2020, trip counts',fontsize = 20)

# manually set the x axis
minDate = bikeAllMonth['starttime'].min()
date_list = [minDate + datetime.timedelta(days=x) for x in range(len(everydayCountSelected))]
date_list_7days = [str(date_list[i].month) + "-"+str(date_list[i].day) for i in range(0,len(date_list),14)]
plt.xticks(np.arange(0,len(everydayCountSelected),14),date_list_7days,fontsize = 20)


# ### Now let's DO TRIP DURATION comparison, comparison across DIFFERENT YEARS, also we consider median, mean, percentile etc.

# In[23]:



# we aggregate results based on time of day in 2020, and we choose the median of tripduration using the code below
bikeDuration = bikeAllMonth.groupby(['Month/Day'])['tripduration'].agg(lambda x: np.median(x.unique()))
bikeDuration = bikeDuration.to_frame()
bikeDuration = bikeDuration.sort_index()
# bikeDuration.plot()

# we aggregate results based on time of day in 2019, and we choose the median of tripduration using the code below
bikeDuration2019 = bikeAllMonth2019.groupby(['Month/Day'])['tripduration'].agg(lambda x: np.median(x.unique()))
bikeDuration2019 = bikeDuration2019.to_frame()
bikeDuration2019 = bikeDuration2019.sort_index()


bikeDuration.plot(figsize = (20,10))
plt.plot(bikeDuration2019)

# plt.xticks([])
plt.xticks(rotation = 20)
labels = ['2020','2019']

plt.legend(labels,fontsize = 20)
plt.title('MEDIAN trip duration in 2019 and 2020',fontsize = 20)
plt.legend(labels)

# manually set the x axis
minDate = bikeAllMonth['starttime'].min()
date_list = [minDate + datetime.timedelta(days=x) for x in range(len(everydayCountSelected))]
date_list_7days = [str(date_list[i].month) + "-"+str(date_list[i].day) for i in range(0,len(date_list),14)]
plt.xticks(np.arange(0,len(everydayCountSelected),14),date_list_7days,fontsize = 20)


# In[24]:


#NOW, AVERAGE DURATION

# we aggregate results based on time of day in 2020, and we choose the MEAN of tripduration using the code below
bikeDuration = bikeAllMonth.groupby(['Month/Day'])['tripduration'].agg(lambda x: np.mean(x.unique()))
bikeDuration = bikeDuration.to_frame()
bikeDuration = bikeDuration.sort_index()
# bikeDuration.plot()

# we aggregate results based on time of day in 2019, and we choose the MEAN of tripduration using the code below
bikeDuration2019 = bikeAllMonth2019.groupby(['Month/Day'])['tripduration'].agg(lambda x: np.mean(x.unique()))
bikeDuration2019 = bikeDuration2019.to_frame()
bikeDuration2019 = bikeDuration2019.sort_index()


bikeDuration.plot(figsize = (20,10))
plt.plot(bikeDuration2019)

# plt.xticks([])
plt.xticks(rotation = 20)
labels = ['2020','2019']

plt.legend(labels,fontsize = 20)
plt.title('Mean trip duration in 2019 and 2020',fontsize = 20)
plt.legend(labels)
# manually set the x axis
minDate = bikeAllMonth['starttime'].min()
date_list = [minDate + datetime.timedelta(days=x) for x in range(len(everydayCountSelected))]
date_list_7days = [str(date_list[i].month) + "-"+str(date_list[i].day) for i in range(0,len(date_list),14)]
plt.xticks(np.arange(0,len(everydayCountSelected),14),date_list_7days,fontsize = 20)


# ### Okay, let's take a deeper look at trip duration in different groups, the example below is a good template for you to do trip duration comparison among different groups, like subscriber, customer and gender etc. 

# In[30]:


# first we select subset of customer, 2020
bikeAllMonthSelected = bikeAllMonth[(bikeAllMonth['usertype'] == 'Customer')]

# then we select subset of Subscriber, 2020
bikeAllMonthSelectedOther = bikeAllMonth[(bikeAllMonth['usertype'] == 'Subscriber')]


# Noe we do the aggregation for customer, aggregate the results based on date, and use the 50th percentile (MEDIAN) as a aggregate results
bikeDurationSelected = bikeAllMonthSelected.groupby(['Month/Day'])['tripduration'].agg(lambda x: np.percentile(x.unique(),50))
bikeDurationSelected = bikeDurationSelected.to_frame()
bikeDurationSelected = bikeDurationSelected.sort_index()



# Noe we do the aggregation for customer, aggregate the results based on date, and use the 25th percentile as a aggregate results
bikeDurationSelected_25 = bikeAllMonthSelected.groupby(['Month/Day'])['tripduration'].agg(lambda x: np.percentile(x.unique(),25))
bikeDurationSelected_25 = bikeDurationSelected_25.to_frame()
bikeDurationSelected_25 = bikeDurationSelected_25.sort_index()

# Noe we do the aggregation for customer, aggregate the results based on date, and use the 75th percentile as a aggregate results
bikeDurationSelected_75 = bikeAllMonthSelected.groupby(['Month/Day'])['tripduration'].agg(lambda x: np.percentile(x.unique(),75))
bikeDurationSelected_75 = bikeDurationSelected_75.to_frame()
bikeDurationSelected_75 = bikeDurationSelected_75.sort_index()

# Noe we do the aggregation for Subscriber, aggregate the results based on date, and use the 50th percentile (MEDIAN) as a aggregate results
bikeDurationSelected2019 = bikeAllMonthSelectedOther.groupby(['Month/Day'])['tripduration'].agg(lambda x: np.percentile(x.unique(),50))
bikeDurationSelected2019 = bikeDurationSelected2019.to_frame()
bikeDurationSelected2019 = bikeDurationSelected2019.sort_index()

# Noe we do the aggregation for Subscriber, aggregate the results based on date, and use the 25th percentile as a aggregate results
bikeDurationSelected2019_25 = bikeAllMonthSelectedOther.groupby(['Month/Day'])['tripduration'].agg(lambda x: np.percentile(x.unique(),25))
bikeDurationSelected2019_25 = bikeDurationSelected2019_25.to_frame()
bikeDurationSelected2019_25 = bikeDurationSelected2019_25.sort_index()

# Noe we do the aggregation for Subscriber, aggregate the results based on date, and use the 75th percentile as a aggregate results
bikeDurationSelected2019_75 = bikeAllMonthSelectedOther.groupby(['Month/Day'])['tripduration'].agg(lambda x: np.percentile(x.unique(),75))
bikeDurationSelected2019_75 = bikeDurationSelected2019_75.to_frame()
bikeDurationSelected2019_75 = bikeDurationSelected2019_75.sort_index()

# never mind this part, its for the plot filling colors
bikeDurationSelected2019_25['index1'] = bikeDurationSelected2019_25.index
bikeDurationSelected2019_75['index1'] = bikeDurationSelected2019_25.index


# never mind this part, its for the plot filling colors
bikeDurationSelected_25['index1'] = bikeDurationSelected_25.index
bikeDurationSelected_75['index1'] = bikeDurationSelected_75.index


# now we start plotting the median line
bikeDurationSelected.plot(figsize = (20,10))
# now we start plotting the shaded area between 25th to 75th percentile
plt.fill_between(bikeDurationSelected_25['index1'],bikeDurationSelected_25['tripduration'],bikeDurationSelected_75['tripduration'],alpha = 0.2)

# now we start plotting the median line
plt.plot(bikeDurationSelected2019)
# now we start plotting the shaded area between 25th to 75th percentile
plt.fill_between(bikeDurationSelected2019_25['index1'],bikeDurationSelected2019_25['tripduration'],bikeDurationSelected2019_75['tripduration'],alpha = 0.2)

# plt.xticks([])
plt.xticks(rotation = 20)
labels = ['Customer','Subscriber',]
plt.legend(labels,fontsize = 20)
plt.title('Subscriber and Customer trip duration in 2019, median, 25 and 75th percentile',fontsize = 20)

# manually set the x axis
minDate = bikeAllMonth['starttime'].min()
date_list = [minDate + datetime.timedelta(days=x) for x in range(len(everydayCountSelected))]
date_list_7days = [str(date_list[i].month) + "-"+str(date_list[i].day) for i in range(0,len(date_list),14)]
plt.xticks(np.arange(0,len(everydayCountSelected),14),date_list_7days,fontsize = 20)



# In[32]:


# first we select subset of customer, 2019
bikeAllMonthSelected = bikeAllMonth2019[(bikeAllMonth2019['usertype'] == 'Customer')]

# then we select subset of Subscriber, 2019
bikeAllMonthSelectedOther = bikeAllMonth2019[(bikeAllMonth2019['usertype'] == 'Subscriber')]


# Noe we do the aggregation for customer, aggregate the results based on date, and use the 50th percentile (MEDIAN) as a aggregate results
bikeDurationSelected = bikeAllMonthSelected.groupby(['Month/Day'])['tripduration'].agg(lambda x: np.percentile(x.unique(),50))
bikeDurationSelected = bikeDurationSelected.to_frame()
bikeDurationSelected = bikeDurationSelected.sort_index()



# Noe we do the aggregation for customer, aggregate the results based on date, and use the 25th percentile as a aggregate results
bikeDurationSelected_25 = bikeAllMonthSelected.groupby(['Month/Day'])['tripduration'].agg(lambda x: np.percentile(x.unique(),25))
bikeDurationSelected_25 = bikeDurationSelected_25.to_frame()
bikeDurationSelected_25 = bikeDurationSelected_25.sort_index()

# Noe we do the aggregation for customer, aggregate the results based on date, and use the 75th percentile as a aggregate results
bikeDurationSelected_75 = bikeAllMonthSelected.groupby(['Month/Day'])['tripduration'].agg(lambda x: np.percentile(x.unique(),75))
bikeDurationSelected_75 = bikeDurationSelected_75.to_frame()
bikeDurationSelected_75 = bikeDurationSelected_75.sort_index()

# Noe we do the aggregation for Subscriber, aggregate the results based on date, and use the 50th percentile (MEDIAN) as a aggregate results
bikeDurationSelected2019 = bikeAllMonthSelectedOther.groupby(['Month/Day'])['tripduration'].agg(lambda x: np.percentile(x.unique(),50))
bikeDurationSelected2019 = bikeDurationSelected2019.to_frame()
bikeDurationSelected2019 = bikeDurationSelected2019.sort_index()

# Noe we do the aggregation for Subscriber, aggregate the results based on date, and use the 25th percentile as a aggregate results
bikeDurationSelected2019_25 = bikeAllMonthSelectedOther.groupby(['Month/Day'])['tripduration'].agg(lambda x: np.percentile(x.unique(),25))
bikeDurationSelected2019_25 = bikeDurationSelected2019_25.to_frame()
bikeDurationSelected2019_25 = bikeDurationSelected2019_25.sort_index()

# Noe we do the aggregation for Subscriber, aggregate the results based on date, and use the 75th percentile as a aggregate results
bikeDurationSelected2019_75 = bikeAllMonthSelectedOther.groupby(['Month/Day'])['tripduration'].agg(lambda x: np.percentile(x.unique(),75))
bikeDurationSelected2019_75 = bikeDurationSelected2019_75.to_frame()
bikeDurationSelected2019_75 = bikeDurationSelected2019_75.sort_index()

# never mind this part, its for the plot filling colors
bikeDurationSelected2019_25['index1'] = bikeDurationSelected2019_25.index
bikeDurationSelected2019_75['index1'] = bikeDurationSelected2019_25.index


# never mind this part, its for the plot filling colors
bikeDurationSelected_25['index1'] = bikeDurationSelected_25.index
bikeDurationSelected_75['index1'] = bikeDurationSelected_75.index


# now we start plotting the median line
bikeDurationSelected.plot(figsize = (20,10))
# now we start plotting the shaded area between 25th to 75th percentile
plt.fill_between(bikeDurationSelected_25['index1'],bikeDurationSelected_25['tripduration'],bikeDurationSelected_75['tripduration'],alpha = 0.2)

# now we start plotting the median line
plt.plot(bikeDurationSelected2019)
# now we start plotting the shaded area between 25th to 75th percentile
plt.fill_between(bikeDurationSelected2019_25['index1'],bikeDurationSelected2019_25['tripduration'],bikeDurationSelected2019_75['tripduration'],alpha = 0.2)

# plt.xticks([])
plt.xticks(rotation = 20)
labels = ['Customer','Subscriber','Customer 25th to 75th','Subscriber 25th to 75th']
plt.legend(labels,fontsize = 20)
plt.title('Subscriber and Customer trip duration in 2019, median, 25 and 75th percentile',fontsize = 20)

# manually set the x axis
minDate = bikeAllMonth['starttime'].min()
date_list = [minDate + datetime.timedelta(days=x) for x in range(len(everydayCountSelected))]
date_list_7days = [str(date_list[i].month) + "-"+str(date_list[i].day) for i in range(0,len(date_list),14)]
plt.xticks(np.arange(0,len(everydayCountSelected),14),date_list_7days,fontsize = 20)


# ### Okay, let's take a deeper look at trip duration in different YEARS

# In[39]:


# first we select subset of younger people, 2020
bikeAllMonthSelected = bikeAllMonth[(bikeAllMonth['birth year'] >= 1990) & (bikeAllMonth['birth year'] <= 2020)]

# first we select subset of younger people, 2019
bikeAllMonthSelectedOther = bikeAllMonth2019[(bikeAllMonth2019['birth year'] >= 1990) & (bikeAllMonth2019['birth year'] <= 2020)]

# Noe we do the aggregation for 2020, aggregate the results based on date, and use the 50th percentile (MEDIAN) as a aggregate results

bikeDurationSelected = bikeAllMonthSelected.groupby(['Month/Day'])['tripduration'].agg(lambda x: np.percentile(x.unique(),50))
bikeDurationSelected = bikeDurationSelected.to_frame()
bikeDurationSelected = bikeDurationSelected.sort_index()

# Noe we do the aggregation for 2020, aggregate the results based on date, and use the 25th percentile  as a aggregate results

bikeDurationSelected_25 = bikeAllMonthSelected.groupby(['Month/Day'])['tripduration'].agg(lambda x: np.percentile(x.unique(),25))
bikeDurationSelected_25 = bikeDurationSelected_25.to_frame()
bikeDurationSelected_25 = bikeDurationSelected_25.sort_index()

# Noe we do the aggregation for 2020, aggregate the results based on date, and use the 75th percentile  as a aggregate results

bikeDurationSelected_75 = bikeAllMonthSelected.groupby(['Month/Day'])['tripduration'].agg(lambda x: np.percentile(x.unique(),75))
bikeDurationSelected_75 = bikeDurationSelected_75.to_frame()
bikeDurationSelected_75 = bikeDurationSelected_75.sort_index()

# never mind this part, its for the plot filling colors

bikeDurationSelected_25['index1'] = bikeDurationSelected_25.index
bikeDurationSelected_75['index1'] = bikeDurationSelected_75.index

# Noe we do the aggregation for 2019, aggregate the results based on date, and use the 50th percentile (MEDIAN) as a aggregate results

bikeDurationSelected2019 = bikeAllMonthSelectedOther.groupby(['Month/Day'])['tripduration'].agg(lambda x: np.percentile(x.unique(),50))
bikeDurationSelected2019 = bikeDurationSelected2019.to_frame()
bikeDurationSelected2019 = bikeDurationSelected2019.sort_index()

# Noe we do the aggregation for 2019, aggregate the results based on date, and use the 25th percentile as a aggregate results

bikeDurationSelected2019_25 = bikeAllMonthSelectedOther.groupby(['Month/Day'])['tripduration'].agg(lambda x: np.percentile(x.unique(),25))
bikeDurationSelected2019_25 = bikeDurationSelected2019_25.to_frame()
bikeDurationSelected2019_25 = bikeDurationSelected2019_25.sort_index()

# Noe we do the aggregation for 2019, aggregate the results based on date, and use the 75th percentile as a aggregate results

bikeDurationSelected2019_75 = bikeAllMonthSelectedOther.groupby(['Month/Day'])['tripduration'].agg(lambda x: np.percentile(x.unique(),75))
bikeDurationSelected2019_75 = bikeDurationSelected2019_75.to_frame()
bikeDurationSelected2019_75 = bikeDurationSelected2019_75.sort_index()

# never mind this part, its for the plot filling colors

bikeDurationSelected2019_25['index1'] = bikeDurationSelected2019_25.index
bikeDurationSelected2019_75['index1'] = bikeDurationSelected2019_25.index


# now we start plotting the median line, for 2020
bikeDurationSelected.plot(figsize = (20,10))
# now we start plotting the shaded area between 25th to 75th percentile, 2020

plt.fill_between(bikeDurationSelected_25['index1'],bikeDurationSelected_25['tripduration'],bikeDurationSelected_75['tripduration'],alpha = 0.2)
# now we start plotting the median line, for 2019

plt.plot(bikeDurationSelected2019)
# now we start plotting the shaded area between 25th to 75th percentile, 2019

plt.fill_between(bikeDurationSelected2019_25['index1'],bikeDurationSelected2019_25['tripduration'],bikeDurationSelected2019_75['tripduration'],alpha = 0.2)

# plt.xticks([])
plt.xticks(rotation = 20)

labels = ['2020','2019','2020 25th to 75th','2019 25th to 75th']
plt.legend(labels,fontsize = 20)
plt.title('2020 and 2019 trip duration in 2020, median, 25 and 75th percentile',fontsize = 20)
# plt.xticks(bikeDurationSelected2019_25['index1'])

# manually set the x axis
minDate = bikeAllMonth['starttime'].min()
date_list = [minDate + datetime.timedelta(days=x) for x in range(len(everydayCountSelected))]
date_list_7days = [str(date_list[i].month) + "-"+str(date_list[i].day) for i in range(0,len(date_list),14)]
plt.xticks(np.arange(0,len(everydayCountSelected),14),date_list_7days,fontsize = 20)


# In[40]:


bikeAllMonth[-10:]


# In[41]:


# first we select subset of younger people, 2020
bikeAllMonthSelected = bikeAllMonth[(bikeAllMonth['birth year'] >= 1996) & (bikeAllMonth['birth year'] <= 2020)]

# first we select subset of younger people, 2019
bikeAllMonthSelectedOther = bikeAllMonth2019[(bikeAllMonth2019['birth year'] >= 1996) & (bikeAllMonth2019['birth year'] <= 2020)]

# Noe we do the aggregation for 2020, aggregate the results based on date, and use the 50th percentile (MEDIAN) as a aggregate results

bikeDurationSelected = bikeAllMonthSelected.groupby(['Month/Day'])['tripduration'].agg(lambda x: np.percentile(x.unique(),50))
bikeDurationSelected = bikeDurationSelected.to_frame()
bikeDurationSelected = bikeDurationSelected.sort_index()

# Noe we do the aggregation for 2020, aggregate the results based on date, and use the 25th percentile  as a aggregate results

bikeDurationSelected_25 = bikeAllMonthSelected.groupby(['Month/Day'])['tripduration'].agg(lambda x: np.percentile(x.unique(),25))
bikeDurationSelected_25 = bikeDurationSelected_25.to_frame()
bikeDurationSelected_25 = bikeDurationSelected_25.sort_index()

# Noe we do the aggregation for 2020, aggregate the results based on date, and use the 75th percentile  as a aggregate results

bikeDurationSelected_75 = bikeAllMonthSelected.groupby(['Month/Day'])['tripduration'].agg(lambda x: np.percentile(x.unique(),75))
bikeDurationSelected_75 = bikeDurationSelected_75.to_frame()
bikeDurationSelected_75 = bikeDurationSelected_75.sort_index()

# never mind this part, its for the plot filling colors

bikeDurationSelected_25['index1'] = bikeDurationSelected_25.index
bikeDurationSelected_75['index1'] = bikeDurationSelected_75.index

# Noe we do the aggregation for 2019, aggregate the results based on date, and use the 50th percentile (MEDIAN) as a aggregate results

bikeDurationSelected2019 = bikeAllMonthSelectedOther.groupby(['Month/Day'])['tripduration'].agg(lambda x: np.percentile(x.unique(),50))
bikeDurationSelected2019 = bikeDurationSelected2019.to_frame()
bikeDurationSelected2019 = bikeDurationSelected2019.sort_index()

# Noe we do the aggregation for 2019, aggregate the results based on date, and use the 25th percentile as a aggregate results

bikeDurationSelected2019_25 = bikeAllMonthSelectedOther.groupby(['Month/Day'])['tripduration'].agg(lambda x: np.percentile(x.unique(),25))
bikeDurationSelected2019_25 = bikeDurationSelected2019_25.to_frame()
bikeDurationSelected2019_25 = bikeDurationSelected2019_25.sort_index()

# Noe we do the aggregation for 2019, aggregate the results based on date, and use the 75th percentile as a aggregate results

bikeDurationSelected2019_75 = bikeAllMonthSelectedOther.groupby(['Month/Day'])['tripduration'].agg(lambda x: np.percentile(x.unique(),75))
bikeDurationSelected2019_75 = bikeDurationSelected2019_75.to_frame()
bikeDurationSelected2019_75 = bikeDurationSelected2019_75.sort_index()

# never mind this part, its for the plot filling colors

bikeDurationSelected2019_25['index1'] = bikeDurationSelected2019_25.index
bikeDurationSelected2019_75['index1'] = bikeDurationSelected2019_25.index


# now we start plotting the median line, for 2020
bikeDurationSelected.plot(figsize = (20,10))
# now we start plotting the shaded area between 25th to 75th percentile, 2020

plt.fill_between(bikeDurationSelected_25['index1'],bikeDurationSelected_25['tripduration'],bikeDurationSelected_75['tripduration'],alpha = 0.2)
# now we start plotting the median line, for 2019

plt.plot(bikeDurationSelected2019)
# now we start plotting the shaded area between 25th to 75th percentile, 2019

plt.fill_between(bikeDurationSelected2019_25['index1'],bikeDurationSelected2019_25['tripduration'],bikeDurationSelected2019_75['tripduration'],alpha = 0.2)

# plt.xticks([])
plt.xticks(rotation = 20)

labels = ['2020','2019','2020 25th to 75th','2019 25th to 75th']
plt.legend(labels,fontsize = 20)
plt.title('2020 and 2019 trip duration in 2020, median, 25 and 75th percentile',fontsize = 20)
# plt.xticks(bikeDurationSelected2019_25['index1'])
plt.xticks(np.arange(0,100, 30))

# manually set the x axis
minDate = bikeAllMonth['starttime'].min()
date_list = [minDate + datetime.timedelta(days=x) for x in range(len(everydayCountSelected))]
date_list_7days = [str(date_list[i].month) + "-"+str(date_list[i].day) for i in range(0,len(date_list),14)]
plt.xticks(np.arange(0,len(everydayCountSelected),14),date_list_7days,fontsize = 20)


# In[42]:


type(bikeDurationSelected2019_75['index1'])


# In[43]:


xlist = bikeDurationSelected2019_75['index1'].tolist()


# In[44]:


# first we select subset of younger people, 2020
bikeAllMonthSelected = bikeAllMonth[(bikeAllMonth['birth year'] >= 1996) & (bikeAllMonth['birth year'] <= 2020)]

# first we select subset of younger people, 2019
bikeAllMonthSelectedOther = bikeAllMonth2019[(bikeAllMonth2019['birth year'] >= 1996) & (bikeAllMonth2019['birth year'] <= 2020)]

# Noe we do the aggregation for 2020, aggregate the results based on date, and use the 50th percentile (MEDIAN) as a aggregate results

bikeDurationSelected = bikeAllMonthSelected.groupby(['Month/Day'])['tripduration'].agg(lambda x: np.percentile(x.unique(),50))
bikeDurationSelected = bikeDurationSelected.to_frame()
bikeDurationSelected = bikeDurationSelected.sort_index()

# Noe we do the aggregation for 2020, aggregate the results based on date, and use the 25th percentile  as a aggregate results

bikeDurationSelected_25 = bikeAllMonthSelected.groupby(['Month/Day'])['tripduration'].agg(lambda x: np.percentile(x.unique(),25))
bikeDurationSelected_25 = bikeDurationSelected_25.to_frame()
bikeDurationSelected_25 = bikeDurationSelected_25.sort_index()

# Noe we do the aggregation for 2020, aggregate the results based on date, and use the 75th percentile  as a aggregate results

bikeDurationSelected_75 = bikeAllMonthSelected.groupby(['Month/Day'])['tripduration'].agg(lambda x: np.percentile(x.unique(),75))
bikeDurationSelected_75 = bikeDurationSelected_75.to_frame()
bikeDurationSelected_75 = bikeDurationSelected_75.sort_index()

# never mind this part, its for the plot filling colors

bikeDurationSelected_25['index1'] = bikeDurationSelected_25.index
bikeDurationSelected_75['index1'] = bikeDurationSelected_75.index

# Noe we do the aggregation for 2019, aggregate the results based on date, and use the 50th percentile (MEDIAN) as a aggregate results

bikeDurationSelected2019 = bikeAllMonthSelectedOther.groupby(['Month/Day'])['tripduration'].agg(lambda x: np.percentile(x.unique(),50))
bikeDurationSelected2019 = bikeDurationSelected2019.to_frame()
bikeDurationSelected2019 = bikeDurationSelected2019.sort_index()

# Noe we do the aggregation for 2019, aggregate the results based on date, and use the 25th percentile as a aggregate results

bikeDurationSelected2019_25 = bikeAllMonthSelectedOther.groupby(['Month/Day'])['tripduration'].agg(lambda x: np.percentile(x.unique(),25))
bikeDurationSelected2019_25 = bikeDurationSelected2019_25.to_frame()
bikeDurationSelected2019_25 = bikeDurationSelected2019_25.sort_index()

# Noe we do the aggregation for 2019, aggregate the results based on date, and use the 75th percentile as a aggregate results

bikeDurationSelected2019_75 = bikeAllMonthSelectedOther.groupby(['Month/Day'])['tripduration'].agg(lambda x: np.percentile(x.unique(),75))
bikeDurationSelected2019_75 = bikeDurationSelected2019_75.to_frame()
bikeDurationSelected2019_75 = bikeDurationSelected2019_75.sort_index()

# never mind this part, its for the plot filling colors

bikeDurationSelected2019_25['index1'] = bikeDurationSelected2019_25.index
bikeDurationSelected2019_75['index1'] = bikeDurationSelected2019_25.index


# now we start plotting the median line, for 2020
bikeDurationSelected.plot(figsize = (20,10))
# now we start plotting the shaded area between 25th to 75th percentile, 2020

plt.fill_between(bikeDurationSelected_25['index1'],bikeDurationSelected_25['tripduration'],bikeDurationSelected_75['tripduration'],alpha = 0.2)
# now we start plotting the median line, for 2019

plt.plot(bikeDurationSelected2019)
# now we start plotting the shaded area between 25th to 75th percentile, 2019

plt.fill_between(bikeDurationSelected2019_25['index1'],bikeDurationSelected2019_25['tripduration'],bikeDurationSelected2019_75['tripduration'],alpha = 0.2)

# plt.xticks([])
plt.xticks(rotation = 20)

labels = ['2020','2019','2020 25th to 75th','2019 25th to 75th']
plt.legend(labels,fontsize = 20)
plt.title('2020 and 2019 trip duration in 2020, median, 25 and 75th percentile',fontsize = 20)
# plt.xticks(bikeDurationSelected2019_25['index1'])
# plt.xticks(bikeDurationSelected2019_25['index1'])
listOfDay = [i for i in range(61)]
plt.xticks(np.arange(0,61,1),listOfDay)


# manually set the x axis
minDate = bikeAllMonth['starttime'].min()
base = datetime.datetime.today()
date_list = [minDate + datetime.timedelta(days=x) for x in range(len(bikeDurationSelected))]
date_list_7days = [str(date_list[i].month) + "-"+str(date_list[i].day) for i in range(0,len(date_list),14)]
plt.xticks(np.arange(0,len(bikeDurationSelected),14),date_list_7days,fontsize = 20)

# minDate = bikeAllMonth['starttime'].min()


# In[45]:


# first we select subset of younger people, 2020
bikeAllMonthSelected = bikeAllMonth[(bikeAllMonth['birth year'] >= 1996) & (bikeAllMonth['birth year'] <= 2020)]

# first we select subset of younger people, 2019
bikeAllMonthSelectedOther = bikeAllMonth2019[(bikeAllMonth2019['birth year'] >= 1996) & (bikeAllMonth2019['birth year'] <= 2020)]

# Noe we do the aggregation for 2020, aggregate the results based on date, and use the 50th percentile (MEDIAN) as a aggregate results

bikeDurationSelected = bikeAllMonthSelected.groupby(['Month/Day'])['tripduration'].agg(lambda x: np.percentile(x.unique(),50))
bikeDurationSelected = bikeDurationSelected.to_frame()
bikeDurationSelected = bikeDurationSelected.sort_index()

# Noe we do the aggregation for 2020, aggregate the results based on date, and use the 25th percentile  as a aggregate results

bikeDurationSelected_25 = bikeAllMonthSelected.groupby(['Month/Day'])['tripduration'].agg(lambda x: np.percentile(x.unique(),25))
bikeDurationSelected_25 = bikeDurationSelected_25.to_frame()
bikeDurationSelected_25 = bikeDurationSelected_25.sort_index()

# Noe we do the aggregation for 2020, aggregate the results based on date, and use the 75th percentile  as a aggregate results

bikeDurationSelected_75 = bikeAllMonthSelected.groupby(['Month/Day'])['tripduration'].agg(lambda x: np.percentile(x.unique(),75))
bikeDurationSelected_75 = bikeDurationSelected_75.to_frame()
bikeDurationSelected_75 = bikeDurationSelected_75.sort_index()

# never mind this part, its for the plot filling colors

bikeDurationSelected_25['index1'] = bikeDurationSelected_25.index
bikeDurationSelected_75['index1'] = bikeDurationSelected_75.index

# Noe we do the aggregation for 2019, aggregate the results based on date, and use the 50th percentile (MEDIAN) as a aggregate results

bikeDurationSelected2019 = bikeAllMonthSelectedOther.groupby(['Month/Day'])['tripduration'].agg(lambda x: np.percentile(x.unique(),50))
bikeDurationSelected2019 = bikeDurationSelected2019.to_frame()
bikeDurationSelected2019 = bikeDurationSelected2019.sort_index()

# Noe we do the aggregation for 2019, aggregate the results based on date, and use the 25th percentile as a aggregate results

bikeDurationSelected2019_25 = bikeAllMonthSelectedOther.groupby(['Month/Day'])['tripduration'].agg(lambda x: np.percentile(x.unique(),25))
bikeDurationSelected2019_25 = bikeDurationSelected2019_25.to_frame()
bikeDurationSelected2019_25 = bikeDurationSelected2019_25.sort_index()

# Noe we do the aggregation for 2019, aggregate the results based on date, and use the 75th percentile as a aggregate results

bikeDurationSelected2019_75 = bikeAllMonthSelectedOther.groupby(['Month/Day'])['tripduration'].agg(lambda x: np.percentile(x.unique(),75))
bikeDurationSelected2019_75 = bikeDurationSelected2019_75.to_frame()
bikeDurationSelected2019_75 = bikeDurationSelected2019_75.sort_index()

# never mind this part, its for the plot filling colors

bikeDurationSelected2019_25['index1'] = bikeDurationSelected2019_25.index
bikeDurationSelected2019_75['index1'] = bikeDurationSelected2019_25.index


# now we start plotting the median line, for 2020
bikeDurationSelected.plot(figsize = (20,10))
# now we start plotting the shaded area between 25th to 75th percentile, 2020

plt.fill_between(bikeDurationSelected_25['index1'],bikeDurationSelected_25['tripduration'],bikeDurationSelected_75['tripduration'],alpha = 0.2)
# now we start plotting the median line, for 2019

plt.plot(bikeDurationSelected2019)
# now we start plotting the shaded area between 25th to 75th percentile, 2019

plt.fill_between(bikeDurationSelected2019_25['index1'],bikeDurationSelected2019_25['tripduration'],bikeDurationSelected2019_75['tripduration'],alpha = 0.2)

# plt.xticks([])
plt.xticks(rotation = 20)

labels = ['2020','2019','2020 25th to 75th','2019 25th to 75th']
plt.legend(labels,fontsize = 20)
plt.title('2020 and 2019 trip duration in 2020, median, 25 and 75th percentile',fontsize = 20)
# plt.xticks(bikeDurationSelected2019_25['index1'])
# plt.xticks(bikeDurationSelected2019_25['index1'])

# manually set the x axis
minDate = bikeAllMonth['starttime'].min()
base = datetime.datetime.today()
date_list = [minDate + datetime.timedelta(days=x) for x in range(len(bikeDurationSelected))]
date_list_7days = [str(date_list[i].month) + "-"+str(date_list[i].day) for i in range(0,len(date_list),14)]
plt.xticks(np.arange(0,len(bikeDurationSelected),14),date_list_7days,fontsize = 20)

print(date_list)
# minDate = bikeAllMonth['starttime'].min()

