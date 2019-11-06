
import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def check_speed(time_gap, speed_gap, total_time, min_speed, max_speed):

  times = (int)(total_time / time_gap)   #获取读取仪表盘的次数

  data_array = np.empty(times)
  weights_array = np.empty(times)
  weights_array.fill(1 / times)

  for i in range(0, times):
    if (speed_gap < 1):
      data_array[i] = random.random() * max_speed  #随机生成一个最高速和最低速之间的速度
    else:
      data_array[i] = random.randint(0, max_speed / speed_gap) * speed_gap  #随机生成一个最高速和最低速之间的速度，先除以speed_gap然后乘以speed_gap进行离散化

  data_frame = pd.DataFrame(data_array)
  bin_range = np.arange(0, 200, speed_gap)
  data_frame.plot(kind = 'hist', bins = bin_range, legend = False)  #获取时速统计次数的直方图
  data_frame.plot(kind = 'hist', bins = bin_range, legend = False, weights = weights_array, ).set_ylabel("Probability")  #获取时速统计概率的直方图
  plt.show()

check_speed(0.01, 0.1, 60, 0, 200)