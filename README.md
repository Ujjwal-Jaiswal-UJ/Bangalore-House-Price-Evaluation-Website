
# Bangalore House Prediction using Machine Learning Algorithm

## Introduction
* The project aim to predict rental house prices in Bangalore city, Karnataka. By combining Data Science techniques with web development skills, we’ve created a valuable resource for potential home buyers and real estate enthusiasts. 
* Linear Regression is the choosen Algorithm for the fundamental technique in predictive model. The project demonstrates a comprehensive approach to predicting housing prices.
* The project paper are published on International Journal for Reseach in Applied Science & Engineering Technology(IJRASET) under the authors - Ujjwal Jaiswal, Ayush Kumar, Deeptanil Das, Aryan Chakraborty, Aditya Vikram Sahana, Debmitra Ghosh and Nirbhay Mishra
* The purpose of deploying this project is to gain practical knowledge in the field of Data Science and to make the fundamental strongs. The project provide many new information about the Data Analysis, Outlier Detection and Removal and many more. 




## Implementation
  ### Data Collection
  * The dataset for model building is taken from the kaggle website. Kaggle is a data science competition platform and online community of data scientists and machine learning practitioners. Kaggle enables users to find and publish datasets, explore and build models in a web-based data science environment
  * The Bangalore Housing Dataset is a comprehensive collection of real estate listings within the bustling city of Bangalore, India. This dataset provides a very basic set of information about residential properties, facilitating in-depth analysis and insights into the city's housing market.
  Link: https://www.kaggle.com/datasets/sarthakniwate13/bangalore-house-price-dataset
  ### Data Cleaning
  * After collecting the dataset from the kaggle website, the data cleaning process set up. Identified and removed any missing null values from the dataset. Ensuring that the subsequent analysis are based on complete data.
  * Removed Unnecessary columns such as availability, society, balcony etc from the dataset and trim it down to dataset with columns such as location, bhk, total_sqft, bath and price.Trimming reduces noise and simplifies the dataset.
  * Converted some dataset columns values for easier access such as total_sqft columns values are converted into float values. A new column bhk is created for keeping the values of size column and the data type is int. 
  ### Feature Extraction
  * After completing the data cleaning process, we have begin with feature extraction process. Feature Engineering is the process of using domain knowledge to extract feature from raw data via machine learning techniques. These features can be used to improve the performance of machine learning algorithm.
  * Created a new column named price_per_sqft by calculating it. The price column is divided by total_sqft column. This column help in camparing the average price of 1bhk, 2bhk, 3bhk, 4bhk, 5bhk. This further help in later processes.
  * Extracted unique location values from the location columns which is helpful in making a drop-down list of our website. Explore statistical summaries for each location to identify trends and outliers. Eliminate locations where the houses available for rent is less than 10.
  ### Outlie Detection and Removal
  * Outlier is an observation that diverges from an overall pattern on a sample. There are many outlier detection techniques such as Extreme Value Analysis, Probabilistic and Statistical Modeling.Here we have used simple domain knowledge of real state market to detect the outliers of the dataset.
  * Firstly I remove houses which have less than 300 sqare feet area for 1 room, which is the average area of 1 bhk flat in Bangalore city. This step ensures that the dataset contains reasonable data points for analysis.
  * For outlier detection, I created a scatter plot for 2 bhk and 3 bhk houses which are in the same location. The discrepancy between 2 BHK and 3 BHK prices served as an indicator of outliers.
  * For outlier removal, group the houses for each location first. Then detected 2 BHK houses with unusually high prices compared to 3 BHK houses. Removing these outliers ensures a cleaner dataset for model training
  ### model Building
  * Categorical features (like location) were encoded into binary form (True/False) using one-hot encoding. For each house, compared its location with a dataset containing only location labels. If the location column matched a value, it turned True for that cell; otherwise, it was False.This process created a binary representation of location information.
  * The binary location representation was merged back into the original dataset. Now the dataset includes both numerical and binary features. We used train_test_split from sklearn.model_selection to split the dataset into training and testing sets. Importing LinearRegression from sklearn.linear_model,we trained a linear regression model.
  * Linear regression is a suitable choice for predicting continuous target variables like house prices. After fitting the model with the training and test datasets, we evaluated its performance. Achieving a model accuracy of 84.52% indicates that our linear regression model captures a significant portion of the variance in house prices.

## Web Development 
  ### prediction_model Directory
  * Under this directory, we have saved column.json file containing all the distinct location name in it. We are able to generate a dynamically populate location dropdowns on our website. 
  * Using the pickle library, we serialized our trained linear regression model. The model is saved as banglore_home_prices_model.pickle. Serialization ensures that we can easily load the model in our server code for predictions.
  ### backend_server Directory
  * Under this directory we have created a sub-directory name guide. It contain the copy of the column.json file and banglore_home_prices_model.pickle. These both were used in building our flask server. 
  * In the server.py we call the fetch_loc_name function from the util.py file using the GET request of the API. It get the location name and return the response in frontend UI. 
  * This file also call forecast_home_price function using GET and POST request of the API. This function takes input from user end and call get_evaluated_price which return the response to frontend UI.
  * The util.py file simply load the data from the column.json file when fetch_loc_name function request is generated from the server.py file. It load the banglore_home_prices_model.pickle for evalution of price when forecast_home_price function request is called from server.py file.
  ### frontend_ui Directory
  * This directory contain three file namely website.html, website.css and website.js. These three file uses three different language for developing the website UI, namely HTML, CSS and JavaScript.
  * The html file, website.html contain the basic structure of the website such as Website name, Carpet Area and it enter space, BHK configuration and enter value. Same goes for the Bath configuration, then the locality where the user get drop down menu for location selection and finally the button.
  * The css file, website.css is basically use to inhance the UI of the website. This file help in selecting the background of the website. Font sizes for Website title, Different Labels. It is also useful for creating scale selection containg values from 1 to 5 which is use in the BHK configuration and Bath configuration.
  * The javascript file, website.js is used from proper functioning of the website. On clicking the button, it takes total_sqft area, location, no_bhk and no_bath as input and all prediction model from the server.py file and finally return the evatuated prince in Lakhs.


## Documentation
The paper is published in the Internation Journel for Research in Applied Science & Engineering Technology which is a peer-reviewed, open-access journal that publishes original research and development articles in the fields of applied science and engineering. This journal aims to provide a platform for scholarly work and international publication opportunities.
The paper name is Predicting the Rental Values of Houses in Bangalore City Using the Linear Regression Approach under Ujjwal Jaiswal, Ayush Kumar, Deeptanil Das, Aryan Chakraborty, Aditya Vikram Sahana, our mentors Debmitra Ghosh and Nirbhay Mishra from JIS University.

[Predicting the Rental Values of Houses in Bangalore
City Using the Linear Regression Approach Paper](https://www.ijraset.com/research-paper/predicting-the-rental-values-of-houses-in-bangalore-city)

[Predicting the Rental Values of Houses in Bangalore
City Using the Linear Regression Approach Certificate](https://drive.google.com/file/d/1Q1aZl8Em31bQbn0pZX_x3apXZqSrd8uB/view?usp=sharing)

[Predicting the Rental Values of Houses in Bangalore
City Using the Linear Regression Approach Presentation](https://www.canva.com/design/DAFvJqww5_U/GRDwDI-UNCh64r-w7FBXLQ/view?utm_content=DAFvJqww5_U&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=h5c84d7b312)
