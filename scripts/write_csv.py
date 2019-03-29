import pandas as pd
import os

path = "/home/c/workspace/tf_models/research/SteelDetection/train_data/img/"

dirs = os.listdir(path)
# print(dirs)
#for filename in dirs:
dataframe = pd.DataFrame({'a_name':dirs})

#将DataFrame存储为csv,index表示是否显示行名，default=True
dataframe.to_csv("test.csv",index=False,sep=',')
