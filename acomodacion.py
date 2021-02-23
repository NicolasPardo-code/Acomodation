from sklearn import metrics
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
import pandas as pd 

def normalization(df):
    le = preprocessing.LabelEncoder()
    df = df.drop([df.columns[0],df.columns[1],df.columns[5],df.columns[6]],axis=1)
    df = df.rename(columns={df.columns[0]:'Genero',df.columns[1]:'Edad',df.columns[2]:'Niños'})      
    df['Edad'].fillna(value=df['Edad'].median(),inplace=True)
    df['Niños'].fillna(method='ffill',inplace=True)
    df['Genero']=le.fit_transform(df['Genero'])
    return df




data = pd.read_csv('train.csv')
acomodacion = data.Acomodacion
data = normalization(data)

X_train,X_test,Y_train,Y_test = train_test_split(data,acomodacion,test_size=0.2,random_state = 0)
dt = tree.DecisionTreeClassifier()
dt = dt.fit(X_train,Y_train)

implementation = pd.read_csv('DataAcomodacion.csv')
prob = normalization(implementation)
aco = dt.predict(prob)
implementation.iloc[:,6] = aco

implementation.to_csv('resultado.csv')



