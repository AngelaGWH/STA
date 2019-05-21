# -*- coding: <encoding name> -*-
import tushare as ts
import pandas as pd
from datetime import datetime, time, date, timedelta
import matplotlib.pyplot as plt
#pd.options.mode.chained_assignment = None

EXCEL_FILE = r'C:\PythonProj\ML_Study\600690_one_year.xlsx'


def fetch_data():
    pro = ts.pro_api("6bc09ebf58a5a5685c5283c3a9e106dd0bd057bcf5d1c07acaa4f7a8")
    begin_time = '2014-05-10'
    end_time = '2019-05-10'
    code = "600690"
    df = ts.get_hist_data(code, start=begin_time, end=end_time)
    df.to_excel('600690_one_year.xlsx')


def display_trend(data, min, max):
    # plt.figure(1)
    # plt.plot(data.index, data['close'])
    # print(type(data.index))
    # plt.xlabel('Date')
    # plt.ylabel('Price')
    # plt.ylim(min - 1, max + 1)
    # plt.title('History of 600690')

    plt.figure(1)
    data.loc[:, 'dayNo'] = [t.dayofyear for t in data.index]
    df_2016 = data[[t.year == 2016 for t in data.index]]
    plt.plot(df_2016.dayNo, df_2016.close, label='2016')

    df_2017 = data[[t.year == 2017 for t in data.index]]
    plt.plot(df_2017.dayNo, df_2017.close, label='2017')

    df_2018 = data[[t.year == 2018 for t in data.index]]
    plt.plot(df_2018.dayNo, df_2018.close, label='2018')

    df_2019 = data[[t.year == 2019 for t in data.index]]
    plt.plot(df_2019.dayNo, df_2019.close, label='2019')

    plt.xlabel('Day of Year')
    plt.ylabel('Price')
    plt.ylim(min - 1, max + 1)
    plt.title('History of 600690')
    plt.legend(loc='upper right', fontsize='x-small')
    plt.show()


def display(data, min, max):
    plt.figure(1)
    plt.plot(data['date'], data['close'])
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.ylim(min - 1, max + 1)
    plt.title('History of 600690')

    plt.figure(2)
    ax1 = plt.subplot(4,1,1)
    ax2 = plt.subplot(4,1,2)
    ax3 = plt.subplot(4,1,3)
    ax4 = plt.subplot(4,1,4)

    plt.sca(ax1)
    df_2016 = data[[t.startswith('2016') for t in data.date]]
    print(df_2016.shape)
    plt.plot(df_2016.date, df_2016.close)

    plt.sca(ax2)
    df_2017 = data[[t.startswith('2017') for t in data.date]]
    print(df_2017.shape)
    plt.plot(df_2017.date, df_2017.close)

    plt.sca(ax3)
    df_2018 = data[[t.startswith('2018') for t in data.date]]
    print(df_2018.shape)
    plt.plot(df_2018.date, df_2018.close)

    plt.sca(ax4)
    df_2019 = data[[t.startswith('2019') for t in data.date]]
    print(df_2019.shape)
    plt.plot(df_2019.date, df_2019.close)

    plt.show()


def basic_analysis(file_name):
    xls = pd.ExcelFile(file_name)
    data = xls.parse('Sheet1')
    data['date'] = data['date'].astype('datetime64')
    data.set_index("date", inplace=True)

    min_value = data['close'].min()
    max_value = data['close'].max()
    min_index = data['close'] == min_value
    max_index = data['close'] == max_value

    print("历史最低价: " + data[min_index].index.strftime('%Y-%m-%d').values[0] + ", 在 " + str(min_value))
    print("历史最高价: " + data[max_index].index.strftime('%Y-%m-%d').values[0] + ", 在 " + str(max_value))

    display_trend(data, min_value, max_value)

if __name__ == '__main__':
    basic_analysis(EXCEL_FILE)

