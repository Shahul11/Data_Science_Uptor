from Machine_learning_supervised_linear_regression import model_training
from utilities.file_reading import data_to_data_frame
from sklearn.linear_model import  LinearRegression

#Below we are giving the new value to predict the output , However till model.fit we are training the data
my_input = {"year":[2009,2010]}
input_df = data_to_data_frame(my_input)


def final_predication():
    model = model_training(LinearRegression())
    my_prediction = model.predict(input_df)
    print("My final output")
    print(my_prediction)
    print("******* End of the Program ******")


if __name__ == "__main__":
    final_predication()
    