# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# # 讀取資料
# data = pd.read_csv('./app_usage_log.csv')

# # 確保時間格式正確
# data['Start Time'] = pd.to_datetime(data['Start Time'])
# data['End Time'] = pd.to_datetime(data['End Time'])

# # 1. 應用程式使用頻率分析
# # 計算每個應用程式的使用次數
# app_usage_count = data['App Name'].value_counts()

# # 計算每個應用程式的總使用時間
# app_usage_duration = data.groupby('App Name')['Duration (seconds)'].sum().sort_values(ascending=False)

# # 顯示應用程式使用頻率
# plt.figure(figsize=(10, 6))
# app_usage_count.plot(kind='bar', title='App Usage Frequency')
# plt.xlabel('App Name')
# plt.ylabel('Usage Count')
# plt.xticks(rotation=45)
# plt.show()

# # 顯示應用程式使用總時間
# plt.figure(figsize=(10, 6))
# app_usage_duration.plot(kind='bar', title='App Usage Duration')
# plt.xlabel('App Name')
# plt.ylabel('Total Usage Time (seconds)')
# plt.xticks(rotation=45)
# plt.show()

# # 2. 使用時間分佈分析
# # 提取開始時間的小時部分
# data['Hour'] = data['Start Time'].dt.hour

# # 計算每小時的總使用時間
# hourly_usage = data.groupby('Hour')['Duration (seconds)'].sum()

# # 顯示每小時的使用時間
# plt.figure(figsize=(10, 6))
# hourly_usage.plot(kind='line', marker='o', title='Hourly App Usage')
# plt.xlabel('Hour of Day')
# plt.ylabel('Total Usage Time (seconds)')
# plt.xticks(range(24))
# plt.grid(True)
# plt.show()

# # 3. 窗口標題分析
# # 計算每個窗口標題的使用時間
# window_usage_duration = data.groupby('Window Title')['Duration (seconds)'].sum().sort_values(ascending=False)

# # 顯示前 10 個使用時間最多的窗口
# plt.figure(figsize=(10, 6))
# window_usage_duration.head(10).plot(kind='bar', title='Top 10 Window Titles by Usage Time')
# plt.xlabel('Window Title')
# plt.ylabel('Total Usage Time (seconds)')
# plt.xticks(rotation=45)
# plt.show()

# # 4. 應用程式與工作時間的關聯分析
# # 定義工作時間（9:00 AM - 6:00 PM）
# data['Is Work Time'] = data['Start Time'].dt.hour.between(9, 18)

# # 計算在工作時間和非工作時間的應用程式使用情況
# work_time_usage = data[data['Is Work Time']].groupby('App Name')['Duration (seconds)'].sum()
# non_work_time_usage = data[~data['Is Work Time']].groupby('App Name')['Duration (seconds)'].sum()

# # 顯示工作時間與非工作時間的使用情況
# plt.figure(figsize=(10, 6))
# work_time_usage.plot(kind='bar', color='blue', alpha=0.6, label='Work Time Usage')
# non_work_time_usage.plot(kind='bar', color='orange', alpha=0.6, label='Non-Work Time Usage')
# plt.title('App Usage During Work and Non-Work Hours')
# plt.xlabel('App Name')
# plt.ylabel('Total Usage Time (seconds)')
# plt.legend()
# plt.xticks(rotation=45)
# plt.show()

# # 5. 應用程式使用的持續時間分佈
# # 畫出每次使用的持續時間分佈（直方圖）
# plt.figure(figsize=(10, 6))
# plt.hist(data['Duration (seconds)'], bins=50, color='skyblue', edgecolor='black')
# plt.title('Distribution of App Usage Duration')
# plt.xlabel('Duration (seconds)')
# plt.ylabel('Frequency')
# plt.grid(True)
# plt.show()

# # 6. 應用程式使用時間序列分析
# # 使用時間序列分析應用程式的總使用時間
# data['Date'] = data['Start Time'].dt.date
# daily_usage = data.groupby('Date')['Duration (seconds)'].sum()

# # 顯示每日的使用時間
# plt.figure(figsize=(10, 6))
# daily_usage.plot(kind='line', marker='o', title='Daily App Usage')
# plt.xlabel('Date')
# plt.ylabel('Total Usage Time (seconds)')
# plt.xticks(rotation=45)
# plt.grid(True)
# plt.show()

import time

def main():
    print("Not implement yet.")
        
if __name__ == "__main__":
    main()