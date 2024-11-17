# import psutil
# import time
# import datetime
# import win32gui
# import win32process
# import csv

# # 獲取當前活動視窗的名稱
# def get_active_window_title():
#     window = win32gui.GetForegroundWindow()
#     title = win32gui.GetWindowText(window)
#     return title

# # 獲取當前活動視窗對應的進程名稱
# def get_process_name_from_window():
#     window = win32gui.GetForegroundWindow()
#     # 使用 win32process 來取得視窗對應的進程 ID
#     thread_id, pid = win32process.GetWindowThreadProcessId(window)
#     # 使用 psutil 來獲取進程名稱
#     process = psutil.Process(pid)
#     return process.name()

# # 紀錄應用程式使用時間
# def log_app_usage(log_file):
#     active_app = None
#     start_time = None

#     with open(log_file, mode='a', newline='', encoding='utf-8') as file:
#         writer = csv.writer(file)
#         writer.writerow(["App Name", "Window Title", "Start Time", "End Time", "Duration (seconds)"])
        
#         try:
#             while True:
#                 current_app = get_process_name_from_window()
#                 current_window_title = get_active_window_title()
#                 print(current_app)

#                 if active_app != current_app:
#                     if active_app:
#                         # 紀錄舊的應用程式的使用時間
#                         end_time = datetime.datetime.now()
#                         duration = (end_time - start_time).total_seconds()
#                         writer.writerow([active_app, active_window_title, start_time.strftime("%Y-%m-%d %H:%M:%S"), end_time.strftime("%Y-%m-%d %H:%M:%S"), duration])
#                         file.flush()  # 即時寫入文件

#                     # 更新新的應用程式
#                     active_app = current_app
#                     active_window_title = current_window_title
#                     start_time = datetime.datetime.now()
                
#                 time.sleep(1)  # 每秒檢查一次
#         except KeyboardInterrupt:
#             print("程式已終止")

# # 執行紀錄程式
# if __name__ == "__main__":
#     log_file = "app_usage_log.csv"
#     log_app_usage(log_file)
import time

def main():
    i = 0
    while True:
        print(i)
        i += 1
        time.sleep(1)
        
if __name__ == "__main__":
    main()
