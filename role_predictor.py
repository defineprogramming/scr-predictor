from prediction_model import train_model
from role_data import role_data
from role_hierarchy import role_hierarchy

def predict_role(user_data):
    # Train the model with the role data and hierarchy
    model = train_model(role_data, role_hierarchy)

    # Prepare the user data for prediction
    prediction_data = [user_data['current_role'], user_data['time_in_role'], user_data['factor1'], user_data['factor2'], user_data['factor3']]

    # Predict the role
    predicted_role = model.predict([prediction_data])

    return predicted_role[0]