# streamlit

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from app.preprocess import load_and_preprocess
from app.model import train_and_predict

st.title("💸 Tips Prediction with MLOps")

X_train, X_test, y_train, y_test = load_and_preprocess()
model, y_true, y_pred, mse = train_and_predict(X_train, X_test, y_train, y_test)

st.subheader("예측 결과 비교")
df_result = pd.DataFrame({'Actual': y_true.values, 'Predicted': y_pred})
st.write(df_result.head())

fig, ax = plt.subplots()
ax.scatter(y_true, y_pred, alpha=0.6)
ax.plot([y_true.min(), y_true.max()], [y_true.min(), y_true.max()], 'r--')
ax.set_xlabel("Actual Tip")
ax.set_ylabel("Predicted Tip")
ax.set_title("Actual vs. Predicted")
st.pyplot(fig)

st.metric("MSE", f"{mse:.4f}")
