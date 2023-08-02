from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from role_data import role_data
from role_hierarchy import role_hierarchy

def train_model(user_data):
    # Prepare data for training
    X = []
    y = []
    for data in role_data:
        X.append([data['current_role'], data['time_in_role'], data['factor1'], data['factor2'], data['factor3']])
        y.append(data['future_role'])

    # Encode categorical data
    le = LabelEncoder()
    X = le.fit_transform(X)
    y = le.fit_transform(y)

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the model
    model = RandomForestClassifier(n_estimators=100)
    model.fit(X_train, y_train)

    # Predict the user's future role
    user_data_encoded = le.transform([user_data['current_role'], user_data['time_in_role'], user_data['factor1'], user_data['factor2'], user_data['factor3']])
    prediction = model.predict([user_data_encoded])

    # Decode the prediction
    predicted_role = le.inverse_transform(prediction)

    return predicted_role[0]