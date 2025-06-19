import seaborn as sns
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

def load_and_preprocess():
    tips = sns.load_dataset("tips")

    le_sex = LabelEncoder()
    le_smoker = LabelEncoder()
    le_day = LabelEncoder()
    le_time = LabelEncoder()

    tips['sex'] = le_sex.fit_transform(tips['sex'])
    tips['smoker'] = le_smoker.fit_transform(tips['smoker'])
    tips['day'] = le_day.fit_transform(tips['day'])
    tips['time'] = le_time.fit_transform(tips['time'])

    X = tips.drop('tip', axis=1)
    y = tips['tip']

    return train_test_split(X, y, test_size=0.2, random_state=42)