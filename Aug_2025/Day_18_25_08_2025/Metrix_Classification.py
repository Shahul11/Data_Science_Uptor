import pandas as pd

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report


my_input ={
    "house_price": [8000,900,1000,11000,1200,1300,14000,15000,1600],
    "house_purchase":[0,1,1,0,1,1,0,0,1]
}#created dictionary
#values given indicates higher value-0(not purchasing),lower value-1(purchasing)

df=pd.DataFrame(my_input)

x=df[["house_price"]]
y=df["house_purchase"]
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)
model=LogisticRegression()
model.fit(x_train,y_train)


y_predict=model.predict(x_test)
print(y_predict)#gives binary values

final_accuracy = accuracy_score(y_test,y_predict)
print(final_accuracy)
print("------")
confusion_matrix_check = confusion_matrix(y_test,y_predict)
print(confusion_matrix_check)
print("------")
classification_check =classification_report(y_test,y_predict)
print(classification_check)



""" 
Git Hub Co pilot-- pasted the prgram
 
🏠 Imagine you're a real estate advisor
You’ve built a smart assistant (your logistic regression model) to help decide whether a customer will buy a house based on its price.
🎯 Accuracy Score in your program
This is like saying:
“Out of the 2 customers I tested, my assistant got both decisions right.”

It’s a summary: 100% accuracy. Sounds great—but it doesn’t tell you how those decisions were made.

🧮 Confusion Matrix in your program
This is like your assistant keeping a detailed log of its predictions:
|  |  |  | 
|  |  |  | 
|  |  |  | 


So:
- True Positive (TP) = 1 → Predicted purchase, and they did buy.
- True Negative (TN) = 1 → Predicted no purchase, and they didn’t buy.
- False Positives / Negatives = 0 → No mistakes.
This matrix shows your assistant didn’t just guess—it made correct decisions for the right reasons.

🧠 Analogy Summary
- Accuracy Score: “My assistant got 2 out of 2 right.”
- Confusion Matrix: “One person didn’t buy and was predicted correctly. One person did buy and was predicted correctly. No mix-ups.”

If you had more test data, say 100 cases, the confusion matrix would help you spot patterns like:
- Is it over-predicting purchases?
- Is it missing out on actual buyers?


"""