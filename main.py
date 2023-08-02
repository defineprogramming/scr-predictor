from role_predictor import predict_role
from user_input import get_user_input
from prediction_model import train_model

def main():
    user_data = get_user_input()
    train_model(user_data)
    predicted_role = predict_role(user_data)
    print(f"Your predicted role in 3 months is: {predicted_role}")

if __name__ == "__main__":
    main()