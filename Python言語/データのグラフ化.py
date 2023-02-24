import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as md
import datetime as dt

df = pd.read_csv('実験2.1いろんな角度.csv')
#display(df)
df = df.rename(columns={'task time(ms)':'作業時間(ms)','waist angle':'腰の角度','side angle':'脇の角度','elbow angle':'肘の角度','wrist angle':'手首の角度',})
df['作業時間(ms)'] = df['作業時間(ms)']/1000
display(df['作業時間(ms)'])

cal = ['腰の角度','脇の角度','肘の角度','手首の角度']
color_ = ["#0000FF","#00FF00","#FF0000","#F0F0F0"]
time_range_lowest = ['0','0','60','140']
time_range_highest = ['100','90','140','180']
loop_var = len(cal) 

i = 0
time = df['作業時間(ms)']
while(i < loop_var):
    plt.rcParams["font.size"] = 14
    plt.rcParams['font.family'] = 'MS Gothic'
    plt.rcParams["figure.figsize"] = (10, 6)
    plt.rcParams['figure.subplot.bottom'] = 0.15
    plt.grid()
    plt.xticks(rotation=0)
    name = df[cal[i]]
    plt.ylim(int(time_range_lowest[i]),int(time_range_highest[i]))#30,110
    if(i == 3):
        plt.xlim(-0.5,13)
    plt.xlabel("作業時間(s)")
    plt.ylabel(cal[i] + '[deg]')
    plt.plot(time,name,lw = 6,color=color_[0],label=cal[i])
    plt.legend(ncol=1)
    plt.savefig(cal[i]+'.png')
    plt.show()
    i = i + 1
