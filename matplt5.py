import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np
# import xlrd

if __name__ == '__main__':
    data = pd.read_excel('score.xls')
    print(data)
    ls = data.values.tolist()
    print(ls)