import tkinter as tk
from tkinter import ttk

font_color = "#FFFFFF"

AAA = 50 #"職能訓練者ID: "
BBB = 30 #"作業時間"
CCC = 25 #"TARGET"
DDD = 20 #"作業時間[m:s.ms]"
EEE = 15 #"Work Time"

class DisplayValue:
    def __init__(self,
                 user_id = "default",
                 total_hms = "00:00.00",
                 target = {'Total':"0.00", 'A':"0.00", 'B':"0.00", 'C':"0.00"},
                 lap = {'Total':"0.00", 'A':"0.00", 'B':"0.00", 'C':"0.00"},
                 gap = {'Total':"0.00", 'A':"0.00", 'B':"0.00", 'C':"0.00"}):
        
        self.user_id = tk.StringVar(value=user_id)
        self.total_hms = tk.StringVar(value=total_hms)
        self.target = {'Total':tk.StringVar(value=target['Total']), 'A':tk.StringVar(value=target['A']), 'B':tk.StringVar(value=target['B']), 'C':tk.StringVar(value=target['C'])}
        self.lap = {'Total':tk.StringVar(value=lap['Total']), 'A':tk.StringVar(value=lap['A']), 'B':tk.StringVar(value=lap['B']), 'C':tk.StringVar(value=lap['C'])}
        self.gap = {'Total':tk.StringVar(value=gap['Total']), 'A':tk.StringVar(value=gap['A']), 'B':tk.StringVar(value=gap['B']), 'C':tk.StringVar(value=gap['C'])}

# メインウインドウ
class MainWindow(tk.Frame):

    def __init__(self):
        self.master = tk.Tk()
        super().__init__(self.master)
        self.dispVal = DisplayValue()

        # ウィンドウの設定
        self.master.geometry("1920x620")
        self.master.title('NISSAN-職業訓練システム')
        self.configure(bg='black')

        # ウィジェットの配置
        self.create_widgets()
        self.pack()
            
    # 配置設定
    def create_widgets(self):
        # --- ID ---
        # IDの設定[日本語表記]
        self.numberd_set_JP=tk.Label(self, bg="black", font=("ToppanBunkyuMidashiMinchoStdN-ExtraBold",AAA,"bold"), text="職能訓練者ID: " ,fg=font_color)
        self.numberd_set_JP.grid(row=0, column=0,sticky="news")
        # IDの設定[英語表記]
        self.numberd_set_EN=tk.Label(self, bg="black", font=("NissanOpti",CCC), text="Player ID" ,fg=font_color)
        self.numberd_set_EN.grid(row=1, column=0, sticky="news")
        # IDの設定[出力値]
        self.numberd_id=tk.Label(self, bg="black", font=("NissanOpti",AAA), textvariable=self.dispVal.user_id, fg=font_color, width=7)
        self.numberd_id.grid(row=0, column=1, columnspan=2, sticky="news")
        
        # --- カラムの表示 ---
        self.column_target_JP=tk.Label(self, bg="black",font=("NissanOpti",CCC), text="TARGET" ,fg=font_color)
        self.column_target_JP.grid(row=2, column=1,sticky="news")
        self.column_actual_JP=tk.Label(self, bg="black",font=("NissanOpti",CCC), text="ACTUAL" ,fg=font_color)
        self.column_actual_JP.grid(row=2, column=3,sticky="news")
        self.column_gap_JP=tk.Label(self, bg="black",font=("NissanOpti",CCC), text="GAP" ,fg=font_color)
        self.column_gap_JP.grid(row=2, column=5,sticky="news")
        
        #---- 総作業時間 [h:m:s]　-----
        self.worktime_set_JP=tk.Label(self, bg="black", font=("NissanOpti",DDD,"bold"), text="作業時間[m:s.ms]" ,fg=font_color)
        self.worktime_set_JP.grid(row=0, column=3, sticky="news")
        self.worktime_all_actual = tk.Label(self, bg="black", font=("NissanOpti", AAA), textvariable=self.dispVal.total_hms, fg=font_color, width=5)
        self.worktime_all_actual.grid(row=0, column=4, columnspan=3, sticky="news", padx=(10,0))
        self.worktime_set_EN=tk.Label(self, bg="black", font=("NissanOpti",EEE), text="Work Time" ,fg=font_color)
        self.worktime_set_EN.grid(row=1, column=3, sticky="news")
        
        # --- 総作業時間 ---
        # 総作業時間の設定[日本語表記]
        self.worktime_set_JP=tk.Label(self, bg="black", font=("NissanOpti",BBB,"bold"), text="作業時間" ,fg=font_color)
        self.worktime_set_JP.grid(row=3, column=0, sticky="news")
        # 総作業時間の設定[英語表記]
        self.worktime_set_EN=tk.Label(self, bg="black", font=("NissanOpti",CCC), text="Work Time" ,fg=font_color)
        self.worktime_set_EN.grid(row=4, column=0, sticky="news")
        # 総作業時間の設定[目標値]
        self.worktime_target=tk.Label(self, bg="black", font=("NissanOpti", BBB, "bold"), textvariable=self.dispVal.target['Total'], fg=font_color)
        self.worktime_target.grid(row=3 , column=1)
        # 総作業時間の設定[(min)表示]
        self.column_min_JP=tk.Label(self, bg="black",font=("NissanOpti", BBB, "bold"), text="[min]   " ,fg=font_color)
        self.column_min_JP.grid(row=3, column=2,sticky="news")
        # 総作業時間の設定[実測値]
        self.worktime_actual=tk.Label(self, bg="black", font=("NissanOpti", BBB, "bold"), textvariable=self.dispVal.lap['Total'], fg=font_color)
        self.worktime_actual.grid(row=3 , column=3)
        # 総作業時間の設定[(min)表示]
        self.column_min_JP=tk.Label(self, bg="black",font=("NissanOpti", BBB, "bold"), text="[min]   " ,fg=font_color)
        self.column_min_JP.grid(row=3, column=4,sticky="news")
        # 総作業時間の設定[ギャップ]
        self.worktime_gap=tk.Label(self, bg="black", font=("NissanOpti", BBB, "bold"), textvariable=self.dispVal.gap['Total'], fg=font_color)
        self.worktime_gap.grid(row=3 , column=5)
        # 総作業時間の設定[(min)表示]
        self.column_min_JP=tk.Label(self, bg="black",font=("NissanOpti", BBB, "bold"), text="[min]   " ,fg=font_color)
        self.column_min_JP.grid(row=3, column=6,sticky="news")
        
        # --- ラップタイム ---
        # === LapTimeA ===
        # 作業工程Aの設定[日本語表記]
        self.lapA_set_JP=tk.Label(self, bg="black", font=("NissanOpti",BBB,"bold"), text="工程 A" ,fg=font_color)
        self.lapA_set_JP.grid(row=5, column=0, sticky="news")
        # 作業工程Aの設定[英語表記]
        self.lapA_set_EN=tk.Label(self, bg="black",font=("NissanOpti",CCC), text="Process A" ,fg=font_color)
        self.lapA_set_EN.grid(row=6, column=0, sticky="news")
        # 作業工程Aの設定[目標値]
        self.lapA_time_target=tk.Label(self, bg="black", font=("NissanOpti", BBB, "bold"), textvariable=self.dispVal.target['A'], fg=font_color)
        self.lapA_time_target.grid(row=5 , column=1)
        # 作業工程Aの設定[(min)表示]
        self.column_min_JP=tk.Label(self, bg="black",font=("NissanOpti", BBB, "bold"), text="[min]   ", fg=font_color)
        self.column_min_JP.grid(row=5, column=2,sticky="news")
        # 作業工程Aの設定[実測値]
        self.lapA_time_actual=tk.Label(self, bg="black", font=("NissanOpti", BBB, "bold"), textvariable=self.dispVal.lap['A'], fg=font_color)
        self.lapA_time_actual.grid(row=5 , column=3)
        # 作業工程Aの設定[(min)表示]
        self.column_min_JP=tk.Label(self, bg="black",font=("NissanOpti", BBB, "bold"), text="[min]   " ,fg=font_color)
        self.column_min_JP.grid(row=5, column=4,sticky="news")
        # 作業工程Aの設定[ギャップ]
        self.lapA_time_gap=tk.Label(self, bg="black", font=("NissanOpti", BBB, "bold"), textvariable=self.dispVal.gap['A'], fg=font_color)
        self.lapA_time_gap.grid(row=5 , column=5)
        # 作業工程Aの設定[(min)表示]
        self.column_min_JP=tk.Label(self, bg="black",font=("NissanOpti", BBB, "bold"), text="[min]   " ,fg=font_color)
        self.column_min_JP.grid(row=5, column=6,sticky="news")

        # === LapTimeB ===
        # 作業工程Bの設定[日本語表記]
        self.lapB_set_JP=tk.Label(self, bg="black",font=("NissanOpti",BBB,"bold"), text="工程 B" ,fg=font_color)
        self.lapB_set_JP.grid(row=7, column=0, sticky="news")
        # 作業工程Bの設定[英語表記]
        self.lapB_set_EN=tk.Label(self, bg="black",font=("NissanOpti",CCC), text="Process B" ,fg=font_color)
        self.lapB_set_EN.grid(row=8, column=0, sticky="news")
        # 作業工程Bの設定[目標値]
        self.lapB_time_target=tk.Label(self, bg="black", font=("NissanOpti", BBB, "bold"), textvariable=self.dispVal.target['B'], fg=font_color)
        self.lapB_time_target.grid(row=7 , column=1)
        # 作業工程Bの設定[(min)表示]
        self.column_min_JP=tk.Label(self, bg="black",font=("NissanOpti", BBB, "bold"), text="[min]   " ,fg=font_color)
        self.column_min_JP.grid(row=7, column=2,sticky="news")
        # 作業工程Bの設定[実測値]
        self.lapB_time_actual=tk.Label(self, bg="black", font=("NissanOpti", BBB, "bold"), textvariable=self.dispVal.lap['B'], fg=font_color)
        self.lapB_time_actual.grid(row=7 , column=3)
        # 作業工程Bの設定[(min)表示]
        self.column_min_JP=tk.Label(self, bg="black",font=("NissanOpti", BBB, "bold"), text="[min]   " ,fg=font_color)
        self.column_min_JP.grid(row=7, column=4,sticky="news")
        # 作業工程Bの設定[ギャップ]
        self.lapB_time_gap=tk.Label(self, bg="black", font=("NissanOpti", BBB, "bold"), textvariable=self.dispVal.gap['B'], fg=font_color)
        self.lapB_time_gap.grid(row=7 , column=5)
        # 作業工程Bの設定[(min)表示]
        self.column_min_JP=tk.Label(self, bg="black",font=("NissanOpti", BBB, "bold"), text="[min]   " ,fg=font_color)
        self.column_min_JP.grid(row=7, column=6,sticky="news")

        # === LapTimeC ===
        # 作業工程Cの設定[日本語表記]
        self.lapC_set_JP=tk.Label(self, bg="black",font=("NissanOpti",BBB,"bold"), text="工程 C" ,fg=font_color)
        self.lapC_set_JP.grid(row=9, column=0, sticky="news")
        # 作業工程Cの設定[英語表記]
        self.lapC_set_EN=tk.Label(self, bg="black",font=("NissanOpti",CCC), text="Process C" ,fg=font_color)
        self.lapC_set_EN.grid(row=10, column=0, sticky="news")
        # 作業工程Cの設定[目標値]
        self.lapC_time_target=tk.Label(self, bg="black", font=("NissanOpti", BBB, "bold"), textvariable=self.dispVal.target['C'], fg=font_color)
        self.lapC_time_target.grid(row=9 , column=1)
        # 作業工程Cの設定[(min)表示]
        self.column_min_JP=tk.Label(self, bg="black",font=("NissanOpti", BBB, "bold"), text="[min]   " ,fg=font_color)
        self.column_min_JP.grid(row=9, column=2,sticky="news")
        # 作業工程Cの設定[実測値]
        self.lapC_time_actual=tk.Label(self, bg="black", font=("NissanOpti", BBB, "bold"), textvariable=self.dispVal.lap['C'], fg=font_color)
        self.lapC_time_actual.grid(row=9 , column=3)
        # 作業工程Cの設定[(min)表示]
        self.column_min_JP=tk.Label(self, bg="black",font=("NissanOpti", BBB, "bold"), text="[min]   " ,fg=font_color)
        self.column_min_JP.grid(row=9, column=4,sticky="news")
        # 作業工程Cの設定[ギャップ]
        self.lapC_time_gap=tk.Label(self, bg="black", font=("NissanOpti", BBB, "bold"), textvariable=self.dispVal.gap['C'], fg=font_color)
        self.lapC_time_gap.grid(row=9 , column=5)
        # 作業工程Cの設定[(min)表示]
        self.column_min_JP=tk.Label(self, bg="black",font=("NissanOpti", BBB, "bold"), text="[min]   " ,fg=font_color)
        self.column_min_JP.grid(row=9, column=6,sticky="news")
        
        # --- ボタン ---
        # ログインボタン(テンキー)の生成
        self.idBtn = tk.Button(self, text='ID')
        self.idBtn.grid(row=15,column=1, columnspan=2, sticky = 'nsew')
        # 目標値設定ボタンの生成
        self.targetBtn = tk.Button(self, text='Target time')
        self.targetBtn.grid(row=15,column=3, columnspan=2, sticky = 'nsew')

# ID入力ウィンドウ
class IDWindow(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # ウィンドウの設定
        master.title("ID認証")
        master.geometry("500x200")
        master.attributes("-topmost", True)
        self.grab_set()
        self.focus_set()

        # ウィジェットの配置
        self.create_widgets()
        self.pack()
    
    # 配置設定
    def create_widgets(self):
        self.id_text = tk.Label(self, text="ID NUMBERを入力", width=50)
        self.id_text.grid(row=0, columnspan=2, sticky="news")
        self.id = ttk.Entry(self, width=50)
        self.id.grid(row=1, columnspan=2, sticky="news")
        self.enterBtn = ttk.Button(self, text='確定', width=1)
        self.enterBtn.grid(row=2, column=0, sticky="news", padx=(10, 10), pady=(20, 10))
        self.cancelBtn = ttk.Button(self, text='キャンセル', width=1)
        self.cancelBtn.grid(row=2, column=1, sticky="news", padx=(10, 10), pady=(20, 10))

# 目標時間入力ウィンドウ
class TargetWindow(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # ウィンドウの設定
        self.master.title("目標値設定")
        self.master.geometry("300x200")
        master.attributes("-topmost", True)
        self.grab_set()
        self.focus_set()

        # ウィジェットの配置
        self.create_widgets()
        self.pack()
    
    # 配置設定
    def create_widgets(self):
        # 作業工程A目標時間の設定
        self.lapA_text = tk.Label(self, text="ラップA")
        self.lapA_text.grid(row=0, column=0, sticky="news", padx=(10, 10))
        self.lapA_target = ttk.Entry(self)
        self.lapA_target.grid(row=0, column=1, columnspan=2, sticky="news", pady=(10, 10))
        # 作業工程B目標時間の設定
        self.lapB_text = tk.Label(self, text="ラップB")
        self.lapB_text.grid(row=1, column=0, sticky="news", padx=(10, 10))
        self.lapB_target = ttk.Entry(self)
        self.lapB_target.grid(row=1, column=1, columnspan=2, sticky="news", pady=(10, 10))
        # 作業工程C目標時間の設定
        self.lapC_text = tk.Label(self, text="ラップC")
        self.lapC_text.grid(row=2, column=0, sticky="news", pady=(10, 10))
        self.lapC_target = ttk.Entry(self)
        self.lapC_target.grid(row=2, column=1, columnspan=2, sticky="news", pady=(10, 10))

        # ボタン
        self.enterBtn = ttk.Button(self, text='確定', width=1)
        self.enterBtn.grid(row=3, columnspan=2, sticky="news", padx=(10, 10), pady=(10, 10))
        self.cancelBtn = ttk.Button(self, text='キャンセル', width=1)
        self.cancelBtn.grid(row=3, column=2, sticky="news", padx=(10, 10), pady=(10, 10))