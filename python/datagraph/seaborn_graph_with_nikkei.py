#!/usr/bin/env python

import json
import os
import sys
import pandas as pd
import glob
import re
import matplotlib.pyplot as plt
import seaborn as sns

# 主に警告対応
# matplotlibのライブラリでpandasを上書きする用途?
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()


def read_nikkei_json():
    """ nikkei-225-index-historical-chart-data.json """
    """ nikkei-225-index-historical-chart-data.csv to JSON """
    with open("nikkei-225-index-historical-chart-data.json", 'r') as f:
        json_data = json.load(f)
    return json_data


def get_df_from_csv(csv_inputdir):
    # 一時的な保管リスト
    list_ = []

    for csv in glob.glob(os.path.join(ARGV[1], "*.csv")):
        df = pd.read_csv(csv, encoding='cp932', )

        csv_filename = os.path.basename(csv)
        now = re.match(r'241000101_SHOHIN-LINEUP_(.*).csv', csv_filename)
        now_dt = now.group(1)

        df[u"基準日"] = [pd.to_datetime(now_dt)] * len(df)
        list_.append(df)

    adf = pd.concat(list_, axis=0)

    return adf


def get_nikkei_df():
    """ 日経平均 """
    nikkei_data = read_nikkei_json()
    nikkei_df = pd.DataFrame({'x': nikkei_data[0], 'y': nikkei_data[1]})
    nikkei_df['x'] = pd.to_datetime(nikkei_df['x'])
    nikkei_df['y'] = nikkei_df['y'].astype(float)

    return nikkei_df


def set_df_graph(product_name, adf):
    graph_df = adf[adf['商品名'] == product_name]
    sns.lineplot(x=graph_df['基準日'], y=graph_df['基準価額'], label=product_name)


def main(csv_inputdir):
    adf = get_df_from_csv(csv_inputdir)

    # 日本語フォント指定
    sns.set(font='IPAGothic')

    plt.figure()
    # グラフ描画
    for product_name in ['三井住友・ＤＣ外国リートインデックスファンド',
                         '三菱ＵＦＪＤＣ新興国債券インデックスファンド',
                         'iFree 8資産ﾊﾞﾗﾝｽ',
                         'ＤＣニッセイ日経２２５インデックスファンドＡ']:
        set_df_graph(product_name, adf)
    nikkei_df = get_nikkei_df()
    sns.lineplot(x=nikkei_df['x'], y=nikkei_df['y'], label='日経平均')

    # グラフ設定
    ax = plt.gca()
    ax.set(xlabel='基準日[年-月]', ylabel='基準価額[円]')

    # 余白設定
    plt.subplots_adjust(top=0.95, right=0.95, bottom=0.37)
    # 凡例を外側に設定
    plt.legend(bbox_to_anchor=(0, -0.18), loc='upper left',
               borderaxespad=0, fontsize=11)

    plt.savefig("seaborn_graph_with_nikkei.png")
    plt.close('all')


if __name__ == '__main__':
    ARGV = sys.argv
    main(ARGV[1])
