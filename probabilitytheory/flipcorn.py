
import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def flip_coin(times):
  data_array = np.empty(times)
  weights_array = np.empty(times)
  weights_array.fill(1 / times)

  for i in range(0, times):                       #抛times次的硬币
    data_array[i] = random.randint(0, 1)        #假设0表示正面，1表示反面

  data_frame = pd.DataFrame(data_array)
  data_frame.plot(kind = 'hist', legend = False)  #获取正反面统计次数的直方图
  data_frame.plot(kind = 'hist', legend = False, weights = weights_array).set_ylabel("Probability")  #获取正反面统计概率的直方图
  plt.show()

flip_coin(1000)