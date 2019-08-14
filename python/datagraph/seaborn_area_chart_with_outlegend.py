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


def get_df_graph(product_name, adf):
    return adf[adf['商品名'] == product_name]


def main(csv_inputdir):
    adf = get_df_from_csv(csv_inputdir)

    # 日本語フォント指定
    sns.set(font='IPAGothic')

    plt.figure()
    # グラフ描画
    product_names = ['三井住友・ＤＣ外国リートインデックスファンド',
                     '三菱ＵＦＪＤＣ新興国債券インデックスファンド',
                     'iFree 8資産ﾊﾞﾗﾝｽ',
                     'ＤＣニッセイ日経２２５インデックスファンドＡ']
    product_dt = None # 基準日
    product_prices_df = pd.DataFrame()
    for product_name in product_names:
        # 各columnの商品名毎のデータを取り出す
        product_df = get_df_graph(product_name, adf)
        # 基準日を設定する
        if not '基準日' in product_prices_df.columns:
            product_prices_df['基準日'] = product_df['基準日'].values
        product_prices_df[product_name] = product_df['基準価額'].values

    # print(product_prices_df.head())
    # 以下データ
    #   三井住友・ＤＣ外国リートインデックスファンド  三菱ＵＦＪＤＣ新興国債券インデックスファンド  iFree 8資産ﾊﾞﾗﾝｽ  ＤＣニッセイ日経２２５インデックスファンドＡ        基準日
    #   0                 11393.0                 13578.0         12001.0                 14076.0 2018-01-10
    #   1                 10130.0                 13111.0         11372.0                 12591.0 2018-03-30
    #   2                 11096.0                 12114.0         11453.0                 13269.0 2018-06-29
    #   3                 11063.0                 13149.0         11312.0                 11661.0 2017-09-18
    #   4                 10680.0                 12159.0         11252.0                 12243.0 2019-01-13
    # 基準日をx軸にして、stackしない設定。
    # stackとは、積み上げグラフを指す
    product_prices_df.plot.area(x='基準日', stacked=False)

    # グラフ設定
    ax = plt.gca()
    ax.set(xlabel='基準日[年-月]', ylabel='基準価額[円]')

    # 余白設定
    plt.subplots_adjust(top=0.95, right=0.95, bottom=0.50)
    # 凡例を外側に設定
    lg = plt.legend(bbox_to_anchor=(0, -0.38), loc='upper left',
               borderaxespad=0, fontsize=11)
    for lg_text in lg.get_texts():
        text = lg_text.get_text()
        mean = product_prices_df[text].mean()
        min = product_prices_df[text].min()
        max = product_prices_df[text].max()
        lg_text.set_text(text + "\nmean:{} min:{} max:{}".format(mean, min, max))
    plt.savefig("seaborn_area_chart_add_legend.png")
    plt.close('all')


if __name__ == '__main__':
    ARGV = sys.argv
    main(ARGV[1])
