import os
import csv
import datetime as dt

class SendValue:
    def __init__(self,
                 user_id = ["default"], total_hms = ["00:00.00"],
                 target = {'Total':0.0, 'A':0.0, 'B':0.0, 'C':0.0},
                 lap = {'Total':0.0, 'A':0.0, 'B':0.0, 'C':0.0},
                 gap = {'Total':0.0, 'A':0.0, 'B':0.0, 'C':0.0}) -> None:
        
        self.user_id = user_id          # ID
        self.total_hms = total_hms     # 作業開始時刻
        self.target = target            # 目標時間
        self.lap = lap                  # 作業時間
        self.gap = gap                  # 差分時間

def val2array(values:SendValue):
    write_time = dt.datetime.now()
    user_id = values.user_id[0]
    total_hms = values.total_hms[0]
    target = values.target
    lap = values.lap
    gap = values.gap

    return [write_time, user_id, total_hms,
            target['Total'], lap['Total'], gap['Total'],
            target['A'], lap['A'], gap['A'],
            target['B'], lap['B'], gap['B'],
            target['C'], lap['C'], gap['C']]


def send(send_val:SendValue):
    save_data = val2array(send_val)
    #csvファイル作成
    folder_path = 'NISSAN_JOB_TRAIN/csv/'#/home/pi/Desktop/
    file_name = folder_path + str(save_data[1]) + '.csv'

    # file detect
    if not os.path.exists(file_name):
        # フォルダがなければ作成
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        
        header = ["save_log","user_id", "total_time[m:s.ms]",
                  "total_target[min]", "total_time[min]","total_gap[min]",
                  "lapA_target[min]", "lapA_time[min]", "lapA_gap[min]",
                  "lapB_target[min]", "lapB_time[min]", "lapB_gap[min]",
                  "lapC_target[min]", "lapC_time[min]", "lapC_gap[min]"]
        file = open(file_name, 'a')
        writer = csv.writer(file)
        writer.writerow(header)
        file.close()

    file = open(file_name, 'a')
    writer = csv.writer(file)
    writer.writerow(save_data)
    file.close()

def disp_time(time:dt.timedelta, target:float):
    total_sec = time.total_seconds()

    lap = cut_round(total_sec/60, 2)
    gap = lap-target
    min = int(total_sec/60)
    sec = cut_round(total_sec%60, 2)

    str_lap = "%.2f" %lap
    str_gap = "%.2f" %gap
    str_hms = "%02d:%02d:%02d" %(min/60, min%60, int(sec))
    str_ms = "%02d:%05.2f" %(min, sec%60)

    return str_lap, str_gap, str_ms

def cut_round(val:float, digit:int):
    dst = int(val * 10**digit)
    return dst / 10**digit
