from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_square_error

def train_and_predict(X_train, X_test, y_train, y_test):
    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    mse = mean_square_error(y_test, y_pred)

    return model, y_test, y_pred, mse