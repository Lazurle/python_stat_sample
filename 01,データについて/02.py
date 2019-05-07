# Pandasをpdという名前でインポートする

# Pandasは表データを処理することに特化した、統計解析において重要なライブラリの一つ。

# In [1]
import pandas as pd
# read_csv()でcsvファイルを読み込んで、DataFrameというデータ構造で返す

# In [2]
df = pd.read_csv('C:/Users/Lazurle/Desktop/git/python_stat_sample/data/ch1_sport_test.csv', index_col = '生徒番号')
print(df)

# In [3]
# 下記の場合、Seriesというデータ構造で返ってくる。
df2 = df['握力']
print(df2)
# DataFrameは２次元の表データのデータ構造だったが、
# Seriesは１次元版のデータ構造となっている。

# 1.1 データの大きさ

# shapeで確かめられる。
# In [4]
print(df.shape)
# Out[4]
# (10, 5)
#　データの数が10個、変数の数が5個とわかった
# 5変数なので５次元ともいえる。
# 生徒番号はインデックスに使われているためカウントされていないが、立派な変数の１つ
