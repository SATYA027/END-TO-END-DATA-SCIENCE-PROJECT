# END-TO-END-DATA-SCIENCE-PROJECT

COMPANY: CODTECH IT SOLUTIONS

NAME: M.D.S.D.Satyanarayana Reddy

INTERN ID: CT06DL1428

DOMAIN: DATA SCIENCE

DURATION: 6 WEEKS

MENTOR: NEELA SANTHOSH

## DESCRIPTION

End-to-End Sentiment Analysis Project — Explained Step by Step
🎯 Objective:
To build, train, and deploy a machine learning model that predicts whether a movie review is positive or negative. This project demonstrates the full cycle of a Data Science workflow — from data processing to real-world deployment using a REST API.

✅ Step 1: Data Collection & Preparation
We began by preparing a dataset consisting of movie reviews. Each review was manually labeled as either positive (1) or negative (0), depending on the sentiment expressed.
This data was converted into a structured format (like a table) to make it suitable for analysis and machine learning.

✅ Step 2: Text Preprocessing and Vectorization
Since machine learning models cannot understand plain text, we converted the reviews into numerical format using a technique called Count Vectorization.
This process transforms each sentence into a vector of numbers that represent how frequently each word appears in the review. It helps the model to understand patterns in text.

✅ Step 3: Model Training
We used a Logistic Regression model for binary classification. It’s a lightweight and efficient algorithm that works well for simple classification tasks.
The model was trained on the vectorized reviews and their corresponding sentiment labels, learning how to associate certain word patterns with positive or negative outcomes.

✅ Step 4: Saving the Model
After training, we saved both the trained model and the word vectorizer so they could be reused in real-time prediction — without retraining again and again.
This step is important for deployment because it allows us to load the model quickly in an application or web service.

✅ Step 5: API Creation with Flask
We built a Flask web application, which serves as an interface for the model. This API receives review text from users, processes it, and returns the prediction.
There are two routes:
A root route (/) that displays a welcome message
A prediction route (/predict) that accepts a review and returns whether it is positive or negative, along with a confidence score

✅ Step 6: Deployment Using Replit
Once the API was working locally, we deployed it to the internet using Replit — a cloud platform that allows Python web apps to be run publicly.
We uploaded all project files to Replit, configured it to run on port 8080, and launched the Flask server. Replit provided a public URL through which anyone can access the sentiment analysis model in real-time.

✅ Step 7: Testing the API
We tested the deployed API using tools like ReqBin, where we sent a sample movie review in the form of a POST request.
The API successfully returned whether the review was positive or negative, along with a confidence percentage showing how sure the model was about its prediction.

🔗 Final Deployment URL:
The project was successfully deployed to this live link:

https://4b4cc18a-de5c-456f-ac7d-97cba9eb0d5b-00-3fzld84tf88we.sisko.replit.dev

## OUTPUT:

1. In the replit:
![image](https://github.com/user-attachments/assets/4b30e6ae-cf5b-4a6f-9c3c-bb9eeee4bea1)

2. After the training online one :
![image](https://github.com/user-attachments/assets/baa9764f-25a0-47d4-96d8-9683c12aeb2a)

3.After trying in the online api testing tool:
![image](https://github.com/user-attachments/assets/d321e67f-365e-4123-b100-c9eafc8d41ab)


