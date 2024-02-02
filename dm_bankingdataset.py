# -*- coding: utf-8 -*-
"""DM_BankingDataset.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VWXNPaZAEGxE1IjC8-2NjW_1NDG_Xye8

# Đọc dữ liệu và tải các thư viện
"""

from google.colab import drive
drive.mount('/content/drive')

"""Tải các thư viện"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import silhouette_score, confusion_matrix, classification_report
from sklearn.naive_bayes import GaussianNB

"""Import data and tranform from `*.csv` type to `dataframe` type"""

file_train = '/content/drive/MyDrive/BTL_KPDL_Banking/train.csv'
file_test = '/content/drive/MyDrive/BTL_KPDL_Banking/test.csv'

df_train = pd.read_csv(file_train, delimiter = ';', header = 0)
df_test = pd.read_csv(file_test, delimiter = ';', header = 0)

df_train.info()

df_test.info()

print(df_train)

print(df_test)

df_train.describe().round(2)

df_test.describe().round(2)

"""**Trực quan hóa một vài thuộc tính của bộ dữ liệu `df_train`**"""

y_barCol = {}
for x in df_train['job'].unique():
  y_barCol[x] = df_train[df_train['job'] == x].count()['job']

my_cmap = plt.get_cmap('Set2')
plt.barh(df_train['job'].unique(), y_barCol.values(), color = my_cmap.colors)
plt.show()

y_barCol = {}
for x in df_test['job'].unique():
  y_barCol[x] = df_test[df_test['job'] == x].count()['job']

my_cmap = plt.get_cmap('Set2')
plt.barh(df_test['job'].unique(), y_barCol.values(), color = my_cmap.colors)
plt.show()

y_barCol = {}
for x in df_train['marital'].unique():
  y_barCol[x] = df_train[df_train['marital'] == x].count()['marital']

my_cmap = plt.get_cmap('Set2')
plt.barh(df_train['marital'].unique(), y_barCol.values(), color = my_cmap.colors)
plt.show()

y_barCol = {}
for x in df_test['marital'].unique():
  y_barCol[x] = df_test[df_test['marital'] == x].count()['marital']

my_cmap = plt.get_cmap('Set2')
plt.barh(df_test['marital'].unique(), y_barCol.values(), color = my_cmap.colors)
plt.show()

y_barCol = {}
for x in df_train['education'].unique():
  y_barCol[x] = df_train[df_train['education'] == x].count()['education']

my_cmap = plt.get_cmap('Set2')
plt.barh(df_train['education'].unique(), y_barCol.values(), color = my_cmap.colors)
plt.show()

y_barCol = {}
for x in df_test['education'].unique():
  y_barCol[x] = df_test[df_test['education'] == x].count()['education']

my_cmap = plt.get_cmap('Set2')
plt.barh(df_test['education'].unique(), y_barCol.values(), color = my_cmap.colors)
plt.show()

fig = plt.figure(figsize=(20, 5))
#dict(sorted(df_train['age'].value_counts().items())).plot(kind='bar', rot='horizontal')
type(df_train['age'].value_counts())

sns.displot(data=df_train, x='age', height=5, aspect=2, color='green')

sns.displot(data=df_test, x='age', height=5, aspect=2, color='green')

sns.boxplot(df_train['balance'])

sns.boxplot(df_test['balance'])

y_barCol = {}
for x in df_train['contact'].unique():
  y_barCol[x] = df_train[df_train['contact'] == x].count()['contact']

my_cmap = plt.get_cmap('Set2')
plt.barh(df_train['contact'].unique(), y_barCol.values(), color = my_cmap.colors)
plt.show()

y_barCol = {}
for x in df_train['contact'].unique():
  y_barCol[x] = df_train[df_train['contact'] == x].count()['contact']

plt.pie(y_barCol.values(), labels = df_train['contact'].unique(), autopct='%1.1f%%')
plt.show()

y_barCol = {}
for x in df_test['contact'].unique():
  y_barCol[x] = df_test[df_test['contact'] == x].count()['contact']

my_cmap = plt.get_cmap('Set2')
plt.barh(df_test['contact'].unique(), y_barCol.values(), color = my_cmap.colors)
plt.show()

y_barCol = {}
for x in df_test['contact'].unique():
  y_barCol[x] = df_test[df_test['contact'] == x].count()['contact']

plt.pie(y_barCol.values(), labels = df_test['contact'].unique(), autopct='%1.1f%%')
plt.show()

my_cmap = plt.get_cmap('Set2')
plt.barh(label.value_counts().index, label.value_counts().values, color = my_cmap.colors)
plt.show()

my_cmap = plt.get_cmap('Set2')
plt.barh(label_test.value_counts().index, label_test.value_counts().values, color = my_cmap.colors)
plt.show()

"""# Tiền xử lý dữ liệu

Xóa các cột không cần thiết
"""

df_train = df_train.drop(columns='contact')
label = df_train['y']
df_train = df_train.drop(columns='y')

label

df_train.info()

print(df_train)

df_test = df_test.drop(columns='contact')
label_test = df_test['y']
df_test = df_test.drop(columns='y')

label_test

df_test.info()

print(df_test)

"""Đổi giá trị của các cột `default`, `housing`, `loan` từ yes/no thành true/false"""

df_train['default'] = df_train['default'].replace('yes', True)
df_train['default'] = df_train['default'].replace('no', False)

df_train['housing'] = df_train['housing'].replace('no', False)
df_train['housing'] = df_train['housing'].replace('yes', True)

df_train['loan'] = df_train['loan'].replace('no', False)
df_train['loan'] = df_train['loan'].replace('yes', True)

df_test['default'] = df_test['default'].replace('yes', True)
df_test['default'] = df_test['default'].replace('no', False)

df_test['housing'] = df_test['housing'].replace('no', False)
df_test['housing'] = df_test['housing'].replace('yes', True)

df_test['loan'] = df_test['loan'].replace('no', False)
df_test['loan'] = df_test['loan'].replace('yes', True)

"""Đếm số dòng dữ liệu trùng lặp"""

duplicated_rows = df_train[df_train.duplicated()]
print(len(duplicated_rows))

duplicated_rows = df_test[df_test.duplicated()]
print(len(duplicated_rows))

"""# Thực hiện gom cụm bằng thuật toán K-means"""

from sklearn.cluster import KMeans
from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import silhouette_score, confusion_matrix, classification_report

"""Tìm các cột có dữ liệu kiểu *category*"""

categorical_cols = [col for col in df_train.columns if df_train[col].dtype=='O']
print(categorical_cols) 	##in các cột dữ liệu dạng category

"""Mã hóa dữ liệu không phải số bằng `LabelEncoder`

"""

df_kmeans = df_train.copy(deep = True)
le = LabelEncoder()
for col in categorical_cols:
  df_kmeans[col] = le.fit_transform(df_kmeans[col])

"""Bảng dữ liệu sau khi mã hóa:"""

df_kmeans

for col in categorical_cols:
  print(col, ': ', df_train[col].unique())

for col in categorical_cols:
  print(col, ': ', df_kmeans[col].unique())

max_clusters = 10  # Số cụm tối đa muốn xem
sse = []
for k in range(1, max_clusters + 1):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(df_kmeans)
    sse.append(kmeans.inertia_)

plt.plot(range(1, max_clusters + 1), sse, marker='o')
plt.xlabel('Số lượng cụm')
plt.ylabel('SSE')
plt.title('Phương pháp Elbow')
plt.show()

# Số cụm tối ưu dựa trên biểu đồ Elbow
num_clusters = 4

# Áp dụng thuật toán K-means
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
kmeans.fit(df_kmeans)

# Gán nhãn cụm cho dữ liệu
df_kmeans['Cluster'] = kmeans.labels_

# Vẽ biểu đồ phân cụm
plt.scatter(df_kmeans['Cluster'], df_kmeans['balance'], c=df_kmeans['Cluster'], cmap='viridis')
plt.xlabel('Cluster')
plt.ylabel('Balance')
plt.title('Phân cụm K-means')
plt.show()

# Vẽ biểu đồ phân cụm theo số dư tài khoản và kết quả của chiến dịch trước
plt.scatter(df_kmeans['poutcome'], df_kmeans['balance'], c=df_kmeans['Cluster'], cmap='viridis')
plt.xlabel('Previous Outcome')
plt.ylabel('Balance')
plt.title('Phân cụm K-means theo số dư tài khoản và kết quả của chiến dịch trước')
plt.show()

"""# Luật kết hợp"""

df_ap = df_train.copy(deep=True)
df_ap = df_ap.drop(columns=['age', 'duration', 'day', 'month', 'campaign', 'pdays', 'previous', 'housing', 'loan'])
df_ap.head()

df_ap.info()

transactions = []
for i in range(0, len(df_train)):
    transactions.append([str(df_ap.values[i, j]) for j in range(0, 6)])

print(transactions[:2])

!pip install apyori

from apyori import apriori
rules = apriori(transactions, min_support = 0.01, min_confidence = 0.6, min_lift = 3, min_length = 2)
results = list(rules)

results = pd.DataFrame(results)
results

"""# Gaussian Naive Bayes"""

X = df_train.copy(deep=True)
Y = label

categorical_cols = [col for col in df_train.columns if df_train[col].dtype=='O']
print(categorical_cols) 	##in các cột dữ liệu dạng category

le = LabelEncoder()
for col in categorical_cols:
  X[col] = le.fit_transform(X[col])

X

Y

print(df_train['job'].unique())
print(X['job'].unique())

nb_test = df_test.copy(deep=True)
enc_list = []
for col in categorical_cols:
  enc = {}
  for x in range(0, len(df_train[col].unique())):
    enc[df_train[col].unique()[x]] = X[col].unique()[x]
  enc_list.append(enc)

print(enc_list[0])

nb_test = df_test.copy(deep=True)
for col in range(0, len(categorical_cols)):
  for r in range(0, len(nb_test[categorical_cols[col]])):
    nb_test.at[r, categorical_cols[col]] = enc_list[col][nb_test.at[r, categorical_cols[col]]]

nb_test

print(df_test['job'].unique())
print(nb_test['job'].unique())

from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()
clf.fit(X, Y)
GaussianNB()

result_nb = clf.predict(nb_test)
print(result_nb)

nb_test = df_test.copy(deep = True)
nb_test.insert(15, 'new_y', result_nb, True)
nb_test

"""Gom cụm thể hiện mối tương quan giữa các thuộc tính trong nb_test"""

nb_kmeans = nb_test.copy(deep = True)
le = LabelEncoder()
for col in categorical_cols:
  nb_kmeans[col] = le.fit_transform(nb_kmeans[col])
nb_kmeans['new_y'] = le.fit_transform(nb_kmeans['new_y'])

nb_kmeans

max_clusters = 10  # Số cụm tối đa muốn xem
sse = []
for k in range(1, max_clusters + 1):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(nb_kmeans)
    sse.append(kmeans.inertia_)

plt.plot(range(1, max_clusters + 1), sse, marker='o')
plt.xlabel('Số lượng cụm')
plt.ylabel('SSE')
plt.title('Phương pháp Elbow')
plt.show()

# Số cụm tối ưu dựa trên biểu đồ Elbow
num_clusters = 4

# Áp dụng thuật toán K-means
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
kmeans.fit(nb_kmeans)

# Gán nhãn cụm cho dữ liệu
nb_kmeans['Cluster'] = kmeans.labels_

plt.scatter(nb_kmeans['Cluster'], nb_kmeans['balance'], c=nb_kmeans['Cluster'], cmap='viridis')
plt.xlabel('Cluster')
plt.ylabel('Balance')
plt.title('Phân cụm K-means')
plt.show()

plt.scatter(nb_kmeans['new_y'], nb_kmeans['balance'], c=nb_kmeans['Cluster'], cmap='viridis')
plt.xlabel('Predict Result')
plt.ylabel('Balance')
plt.title('Phân cụm K-means theo số dư tài khoản và kết quả dự đoán khả năng đồng ý')
plt.show()

plt.scatter(nb_kmeans['Cluster'], nb_kmeans['age'], c=nb_kmeans['Cluster'], cmap='viridis')
plt.xlabel('Cluster')
plt.ylabel('Age')
plt.title('Phân cụm K-means')
plt.show()

plt.scatter(nb_kmeans['new_y'], nb_kmeans['age'], c=nb_kmeans['Cluster'], cmap='viridis')
plt.xlabel('Predict Result')
plt.ylabel('Age')
plt.title('Phân cụm K-means theo số tuổi khách hàng và kết quả dự đoán khả năng đồng ý')
plt.show()

"""# Support Vector Machine (SVM)

kernel = 'rbf'
"""

X = df_train.copy(deep=True)
Y = label

X

Y

categorical_cols = [col for col in df_train.columns if df_train[col].dtype=='O']
print(categorical_cols)

le = LabelEncoder()
for col in categorical_cols:
  X[col] = le.fit_transform(X[col])

X

svm_test = df_test.copy(deep=True)
enc_list = []
for col in categorical_cols:
  enc = {}
  for x in range(0, len(df_train[col].unique())):
    enc[df_train[col].unique()[x]] = X[col].unique()[x]
  enc_list.append(enc)

print(enc_list[0])

svm_test = df_test.copy(deep=True)
for col in range(0, len(categorical_cols)):
  for r in range(0, len(svm_test[categorical_cols[col]])):
    svm_test.at[r, categorical_cols[col]] = enc_list[col][svm_test.at[r, categorical_cols[col]]]

svm_test

from sklearn import svm
clf = svm.SVC()
clf.fit(X, Y)
svm.SVC()

svm_result = clf.predict(svm_test)

svm_result

svm_test = df_test.copy(deep = True)
svm_test.insert(15, 'new_y', svm_result, True)
svm_test

svm_kmeans = svm_test.copy(deep = True)
le = LabelEncoder()
for col in categorical_cols:
  svm_kmeans[col] = le.fit_transform(svm_kmeans[col])
svm_kmeans['new_y'] = le.fit_transform(svm_kmeans['new_y'])

svm_kmeans

max_clusters = 10  # Số cụm tối đa muốn xem
sse = []
for k in range(1, max_clusters + 1):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(svm_kmeans)
    sse.append(kmeans.inertia_)

plt.plot(range(1, max_clusters + 1), sse, marker='o')
plt.xlabel('Số lượng cụm')
plt.ylabel('SSE')
plt.title('Phương pháp Elbow')
plt.show()

# Số cụm tối ưu dựa trên biểu đồ Elbow
num_clusters = 4

# Áp dụng thuật toán K-means
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
kmeans.fit(svm_kmeans)

# Gán nhãn cụm cho dữ liệu
svm_kmeans['Cluster'] = kmeans.labels_

plt.scatter(svm_kmeans['Cluster'], svm_kmeans['balance'], c=svm_kmeans['Cluster'], cmap='viridis')
plt.xlabel('Cluster')
plt.ylabel('Balance')
plt.title('Phân cụm K-means')
plt.show()

plt.scatter(svm_kmeans['new_y'], svm_kmeans['balance'], c=svm_kmeans['Cluster'], cmap='viridis')
plt.xlabel('Predict Result')
plt.ylabel('Balance')
plt.title('Phân cụm K-means theo số dư tài khoản và kết quả dự đoán khả năng đồng ý')
plt.show()

plt.scatter(svm_kmeans['new_y'], svm_kmeans['age'], c=svm_kmeans['Cluster'], cmap='viridis')
plt.xlabel('Predict Result')
plt.ylabel('Age')
plt.title('Phân cụm K-means theo số tuổi khách hàng và kết quả dự đoán khả năng đồng ý')
plt.show()

"""# Kiểm tra độ chính xác của các thuật toán phân lớp bằng ma trận sai lầm"""

from sklearn.metrics import ConfusionMatrixDisplay
ConfusionMatrixDisplay.from_predictions(label_test, svm_result)
plt.show()

from sklearn.metrics import ConfusionMatrixDisplay
ConfusionMatrixDisplay.from_predictions(label_test, result_nb)
plt.show()