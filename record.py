import psutil
import time
import datetime
import win32gui
import win32process
import win32api
import win32con
import csv

# 獲取當前所有視窗
def enum_windows(callback):
    win32gui.EnumWindows(callback, None)

# 獲取視窗的名稱
def get_window_title(hwnd):
    if win32gui.IsWindowVisible(hwnd):
        return win32gui.GetWindowText(hwnd)
    return None

# 獲取視窗所屬的進程名稱
def get_process_name(hwnd):
    try:
        _, pid = win32process.GetWindowThreadProcessId(hwnd)
        process = psutil.Process(pid)
        return process.name()
    except Exception:
        return None

# 檢查視窗是否位於多顯示器上
def get_monitor_from_window(hwnd):
    try:
        monitor = win32api.MonitorFromWindow(hwnd, win32con.MONITOR_DEFAULTTONULL)
        return monitor
    except Exception:
        return None

# 紀錄應用程式使用時間
def log_app_usage(log_file):
    active_windows = {}
    start_time = {}

    with open(log_file, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # TODO: Add categories
        writer.writerow(["App Name", "Window Title", "Monitor", "Start Time", "End Time", "Duration (seconds)"])
        
        try:
            while True:
                current_windows = {}

                # 列舉所有視窗
                def callback(hwnd, extra):
                    window_title = get_window_title(hwnd)
                    if window_title:
                        process_name = get_process_name(hwnd)
                        monitor = get_monitor_from_window(hwnd)

                        if monitor and process_name:
                            current_windows[hwnd] = (process_name, window_title, monitor)
                
                enum_windows(callback)

                # 檢查新視窗
                for hwnd, (process_name, window_title, monitor) in current_windows.items():
                    if hwnd not in active_windows:
                        # 紀錄新的應用程式和螢幕
                        active_windows[hwnd] = (process_name, window_title, monitor)
                        start_time[hwnd] = datetime.datetime.now()
                    elif active_windows[hwnd] != (process_name, window_title, monitor):
                        # 如果視窗資料改變，紀錄舊資料
                        end_time = datetime.datetime.now()
                        duration = (end_time - start_time[hwnd]).total_seconds()
                        old_process_name, old_window_title, old_monitor = active_windows[hwnd]
                        writer.writerow([old_process_name, old_window_title, old_monitor, start_time[hwnd].strftime("%Y-%m-%d %H:%M:%S"), end_time.strftime("%Y-%m-%d %H:%M:%S"), duration])
                        file.flush()

                        # 更新新的資料
                        active_windows[hwnd] = (process_name, window_title, monitor)
                        start_time[hwnd] = datetime.datetime.now()

                # 檢查已關閉的視窗
                for hwnd in list(active_windows.keys()):
                    if hwnd not in current_windows:
                        # 紀錄結束的應用程式
                        end_time = datetime.datetime.now()
                        duration = (end_time - start_time[hwnd]).total_seconds()
                        process_name, window_title, monitor = active_windows[hwnd]
                        writer.writerow([process_name, window_title, monitor, start_time[hwnd].strftime("%Y-%m-%d %H:%M:%S"), end_time.strftime("%Y-%m-%d %H:%M:%S"), duration])
                        file.flush()
                        del active_windows[hwnd]
                        del start_time[hwnd]

                time.sleep(1)  # 每秒檢查一次

        except KeyboardInterrupt:
            print("程式已終止")

# 執行紀錄程式
if __name__ == "__main__":
    log_file = "app_usage_log.csv"
    log_app_usage(log_file)