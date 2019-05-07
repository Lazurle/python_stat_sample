import numpy as np
import pandas as  pd

# Jupyter Notebookの出力を小数点以下３桁に抑える。
#%precision 3
# Dataframeの出力を小数点以下３桁に抑える。
pd.set_option('precision', 3)


df = pd.read_csv('C:/Users/Lazurle/Desktop/git/python_stat_sample/data/ch2_scores_em.csv', index_col = '生徒番号')

# dfの先頭5行表示
print(df.head())
# dfの末尾5行表示
print(df.tail())

# NumPyのarrayというデータ構造にしてscoresという名前で保存。
scores = np.array(df['英語'])[:10]
print(scores)

scores_df = pd.DataFrame({'点数':scores}, index = pd.Index(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'], name = '生徒'))
print(scores_df)
