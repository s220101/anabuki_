import datetime as dt
import tkinter as tk
from tkinter import ttk, messagebox
from RPi import GPIO

import View
import Model

PIN_START = 4
PIN_FINISH = 6
PIN_RESET = 5
PIN_LAP_A = 22
PIN_LAP_B = 11
PIN_LAP_C = 26

# メインウインドウ制御
class MainWindowController:
    def __init__(self):
        self.sendVal = Model.SendValue()
        self.flag = {'Total':False, 'A':False, 'B':False, 'C':False}

        # ウィンドウの立ち上げ
        self.mainWindow = View.MainWindow()
        self.mainWindow.idBtn.config(command=self.idBtnClicked)
        self.mainWindow.targetBtn.config(command=self.targetBtnClicked)
        
        # ボタン設定
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(PIN_START, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(PIN_FINISH, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(PIN_RESET, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(PIN_LAP_A, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(PIN_LAP_B, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(PIN_LAP_C, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        
        GPIO.add_event_detect(PIN_START, GPIO.BOTH, callback=self.callback_switch, bouncetime=200)
        GPIO.add_event_detect(PIN_FINISH, GPIO.BOTH, callback=self.callback_switch, bouncetime=200)
        GPIO.add_event_detect(PIN_RESET, GPIO.BOTH, callback=self.callback_switch, bouncetime=200)
        GPIO.add_event_detect(PIN_LAP_A, GPIO.BOTH, callback=self.callback_switch, bouncetime=200)
        GPIO.add_event_detect(PIN_LAP_B, GPIO.BOTH, callback=self.callback_switch, bouncetime=200)
        GPIO.add_event_detect(PIN_LAP_C, GPIO.BOTH, callback=self.callback_switch, bouncetime=200)
        
        # Start window
        self.mainWindow.master.after(10,self.update)
        self.mainWindow.mainloop()

    # --- 状態更新 ---
    def update(self):
        if(self.flag['Total']):
            delta_time = dt.datetime.now() - self.start_time
            lap, gap, hms = Model.disp_time(delta_time, self.sendVal.target['Total'])
            self.mainWindow.dispVal.lap['Total'].set(lap)
            self.mainWindow.dispVal.gap['Total'].set(gap)
            self.mainWindow.dispVal.total_hms.set(hms)
        
        self.mainWindow.master.after(10,self.update)

    # --- 物理ボタン関連 ---
    # push switch detect
    def callback_switch(self, pin):
        if(pin==PIN_START):
            self.countStart()
        elif(pin==PIN_FINISH):
            self.countStop()
        elif(pin==PIN_RESET):
            self.countReset()
        elif(pin==PIN_LAP_A):
            self.lapPush('A')
        elif(pin==PIN_LAP_B):
            self.lapPush('B')
        elif(pin==PIN_LAP_C):
            self.lapPush('C')
    
    # スタートボタン動作
    def countStart(self):
        if(not self.flag['Total']):
            #self.countReset()
            self.start_time = dt.datetime.now()
            self.flag['Total'] = True

    # ストップボタン動作
    def countStop(self):
        if(self.flag['Total']):
            self.flag['Total'] = False

            # 合計時間計算
            delta_time = dt.datetime.now() - self.start_time
            lap, gap, hms = Model.disp_time(delta_time, self.sendVal.target['Total'])
            self.mainWindow.dispVal.lap['Total'].set(lap)
            self.mainWindow.dispVal.gap['Total'].set(gap)
            self.mainWindow.dispVal.total_hms.set(hms)
            self.sendVal.lap['Total'] = float(lap)
            self.sendVal.gap['Total'] = float(gap)
            self.sendVal.total_hms[0] = hms

            Model.send(self.sendVal)
    
    # リセットボタン動作
    def countReset(self):
        self.flag = {'Total':False, 'A':False, 'B':False, 'C':False}
        self.mainWindow.dispVal.total_hms.set("00:00.00")
        self.mainWindow.dispVal.lap['Total'].set("0.00")
        self.mainWindow.dispVal.lap['A'].set("0.00")
        self.mainWindow.dispVal.lap['B'].set("0.00")
        self.mainWindow.dispVal.lap['C'].set("0.00")
        self.mainWindow.dispVal.gap['Total'].set("0.00")
        self.mainWindow.dispVal.gap['A'].set("0.00")
        self.mainWindow.dispVal.gap['B'].set("0.00")
        self.mainWindow.dispVal.gap['C'].set("0.00")
        self.sendVal.total_hms = ["00:00.00"]
        self.sendVal.lap = {'Total':0.0, 'A':0.0, 'B':0.0, 'C':0.0}
        self.sendVal.gap = {'Total':0.0, 'A':0.0, 'B':0.0, 'C':0.0}
    
    def lapPush(self, key:str):
        if(self.flag['Total'] and not self.flag[key]):
            delta_time = dt.datetime.now() - self.start_time
            sum_time = sum(self.sendVal.lap.values())*60
            lap_time = delta_time - dt.timedelta(seconds=sum_time)

            lap, gap, hms = Model.disp_time(lap_time, self.sendVal.target[key])
            self.mainWindow.dispVal.lap[key].set(lap)
            self.mainWindow.dispVal.gap[key].set(gap)
            self.sendVal.lap[key] = float(lap)
            self.sendVal.gap[key] = float(gap)
            self.flag[key] = True
            
            if (self.flag['A'] and self.flag['B'] and self.flag['C']):
                self.countStop()
    
    # --- 画面遷移関連 ---
    def idBtnClicked(self):
        IDWindowController(tk.Toplevel(self.mainWindow.master), self.mainWindow.dispVal.user_id, self.sendVal.user_id)

    def targetBtnClicked(self):
        TargetWindowController(tk.Toplevel(self.mainWindow.master), self.mainWindow.dispVal.target, self.sendVal.target)

# ID入力ウインドウ制御
class IDWindowController:
    def __init__(self, master, disp_id, send_id):
        self.disp_id = disp_id
        self.send_id = send_id
        self.idWindow = View.IDWindow(master)
        self.idWindow.enterBtn.config(command=self.enterBtnClicked)
        self.idWindow.cancelBtn.config(command=self.cancelBtnClicked)

    # 確定ボタン押下時の処理
    def enterBtnClicked(self):
        uid = self.idWindow.id.get()
        if(uid==''):
            messagebox.showwarning("Warning", "値を入力してください")
        else:
            self.disp_id.set(uid)
            self.send_id[0] = uid
            self.idWindow.master.destroy()

    # キャンセルボタン押下時の処理
    def cancelBtnClicked(self):
        self.idWindow.master.destroy()

# 目標値入力ウインドウ制御
class TargetWindowController:
    def __init__(self, master, disp_target, send_target):
        self.disp_target = disp_target
        self.send_target = send_target
        self.targetWindow = View.TargetWindow(master)
        self.targetWindow.enterBtn.config(command=self.enterBtnClicked)
        self.targetWindow.cancelBtn.config(command=self.cancelBtnClicked)

    # 確定ボタン押下時の処理
    def enterBtnClicked(self):
        entry = {'A':self.targetWindow.lapA_target.get(), 
                 'B':self.targetWindow.lapB_target.get(),
                 'C':self.targetWindow.lapC_target.get()}
        
        # エラーチェック
        try:
            for key in entry:
                entry[key] = round(float(entry[key]),2)
        except:
            # 少数型に変換できなければ警告を表示
            messagebox.showwarning("Warning", "値は少数を入力してください")
        else:
            total_target = 0
            for key in entry:
                val = round(entry[key], 2)
                total_target += val
                self.disp_target[key].set('{:.2f}'.format(val))
                self.send_target[key] = val
            self.disp_target['Total'].set('{:.2f}'.format(total_target))
            self.send_target['Total'] = total_target
            self.targetWindow.master.destroy()

    # キャンセルボタン押下時の処理
    def cancelBtnClicked(self):
        self.targetWindow.master.destroy()

class MainProcess():
    def __init__(self) -> None:
        MainWindowController()
