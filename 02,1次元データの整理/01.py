import numpy as np
import pandas as  pd

# Jupyter Notebookの出力を小数点以下３桁に抑える。
#%precision 3
# Dataframeの出力を小数点以下３桁に抑える。
pd.set_option('precision', 3)


df = pd.read_csv('C:/Users/Lazurle/Desktop/git/python_stat_sample/data/ch2_scores_em.csv', index_col = '生徒番号')
print("\n")
print("In[2]")
# dfの先頭5行表示
print(df.head())
# dfの末尾5行表示
print(df.tail())

print("\n")
print("In[3]")
# NumPyのarrayというデータ構造にしてscoresという名前で保存。
scores = np.array(df['英語'])[:10]
print(scores)

#scores_df.set_option('precision', 3)

a = 16.600123
print(a)
print("\n")
print("In[4]")
scores_df = pd.DataFrame({'点数':scores}, index = pd.Index(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'], name = '生徒'))
print(scores_df)

print("\n")
print("In[5]")
print(sum(scores)/len(scores))

print("\n")
print("In[6]")
print( np.mean(scores) )
print(type(np.mean(scores)))

print(type(scores))
print(type(sum(scores)/len(scores)))
print("\n")

print("\n")
print("In[8]")
sorted_scores = np.sort(scores)
n = len(sorted_scores)
m0 = sorted_scores[n//2 - 1]
print(type(m0))

print("\n")
print("In[12]")
print( pd.Series([1, 1, 1, 2, 2, 3]).mode() )
a = pd.Series([1, 1, 1, 2, 2, 3]).mode()
print("\n")
print( a )
print( type(a) )
b =  pd.Series([5, 4, 2, 2, 1, 1]).mode()
print( pd.Series([5, 4, 2, 2, 1, 1]).mode() )
print( b[1] )
print( type(b[1]) )
