import re

def search_file(file, pattern):
    content = open(file).read()
    if re.search(pattern, content, re.MULTILINE | re.DOTALL):
        return True
    return False


### Find unusual patterns in hourly Google search traffic (25 points)
def test_traffic():
    assert search_file("forecasting_net_prophet.ipynb", rf"abc123") == True, "Read the search data into a DataFrame. (5 points)"






### Split the Data into Training and Testing Sets (30 points)
def test_split():
    assert search_file("forecasting_net_prophet.ipynb", rf"abc123") == True, "There is a prediction about which model you expect to do better. (5 points)"

    assert search_file("forecasting_net_prophet.ipynb", rf"abc123") == True, "The labels set (y) is created from the “spam” column. (5 points)"

    assert search_file("forecasting_net_prophet.ipynb", rf"abc123") == True, "The features DataFrame (X) is created from the remaining columns. (5 points)"

    assert search_file("forecasting_net_prophet.ipynb", rf"abc123") == True, "The value_counts function is used to check the balance of the labels variable (y). (5 points)"

    assert search_file("forecasting_net_prophet.ipynb", rf"abc123") == True, "The data is correctly split into training and testing datasets by using train_test_split. (10 points)"

### Scale the Features (20 points)
def test_scale():
    assert search_file("forecasting_net_prophet.ipynb", rf"abc123") == True, "An instance of StandardScaler is created. (5 points)"

    assert search_file("forecasting_net_prophet.ipynb", rf"abc123") == True, "The Standard Scaler instance is fit with the training data. (5 points)"

    assert search_file("forecasting_net_prophet.ipynb", rf"abc123") == True, "The training features DataFrame is scaled using the transform function. (5 points)"

    assert search_file("forecasting_net_prophet.ipynb", rf"abc123") == True, "The testing features DataFrame is scaled using the transform function. (5 points)"

### Create a Logistic Regression Model (20 points)
def test_lr_model():
    assert search_file("forecasting_net_prophet.ipynb", rf"abc123") == True, "A logistic regression model is created with a random_state of 1. (5 points)"

    assert search_file("forecasting_net_prophet.ipynb", rf"abc123") == True, "The logistic regression model is fitted to the scaled training data (X_train_scaled and y_train). (5 points)"

    assert search_file("forecasting_net_prophet.ipynb", rf"abc123") == True, "Predictions are made for the testing data labels by using the testing feature data (X_test_scaled) and the fitted model, and saved to a variable. (5 points)"

    assert search_file("forecasting_net_prophet.ipynb", rf"abc123") == True, "The model’s performance is evaluated by calculating the accuracy score of the model with the accuracy_score function. (5 points)"

### Create a Random Forest Model (20 points)
def test_rf_model():
    assert search_file("forecasting_net_prophet.ipynb", rf"abc123") == True, "A random forest model is created with a random_state of 1. (5 points)"

    assert search_file("forecasting_net_prophet.ipynb", rf"abc123") == True, "The random forest model is fitted to the scaled training data (X_train_scaled and y_train). (5 points)"

    assert search_file("forecasting_net_prophet.ipynb", rf"abc123") == True, "Predictions are made for the testing data labels by using the testing feature data (X_test_scaled) and the fitted model, and saved to a variable. (5 points)"

    assert search_file("forecasting_net_prophet.ipynb", rf"abc123") == True, "The model’s performance is evaluated by calculating the accuracy score of the model with the accuracy_score function. (5 points)"

### Evaluate the Models (10 points)
def test_eval():
    assert search_file("forecasting_net_prophet.ipynb", rf"abc123") == True, "Which model performed better? (5 points)"

    assert search_file("forecasting_net_prophet.ipynb", rf"abc123") == True, "How does that compare to your prediction? (5 points)"
