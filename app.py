# AUTHOR: Sumit Sahay
# Importing required libraries
from flask import Flask, render_template, request, redirect, url_for
import warnings
import pandas as pd
warnings.filterwarnings("ignore")

# Importing model library
import model


# Initializing Flask App
app = Flask(__name__)


# Defining method for root path
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/recommend-products', methods=['POST'])
def recommendProducts():
    # Fetching the user entered username 
    username =  str(request.form.get('username'))

    # Getting recommendations for user using the model
    modelOutput = model.sentimentBasedProductRecommendations(username)

    # Checking type of variable if it's not a list then it will be an error
    if type(modelOutput) != list : 
        # Returning the error to be displayed
        return render_template('index.html', error=modelOutput)

    # If output is a list then:
    # Converting recommendations list to a dataFrame
    recommendations = pd.DataFrame(modelOutput, columns=['Product Recommendations'])

    # Creating a HTML table using DataFrame
    recommendations_table = [recommendations.to_html(classes='recommendations')]
    # Defining Table title
    table_title = ['NAN', 'Top 5 Product Recommendations for : {}'.format(username)]

    # Rendering Template while passing the results
    return  render_template('index.html', productsTable = recommendations_table, titles=table_title)

@app.route('/allusernames', methods=['GET'])
def allUsernames():
    # Reading usernames from source i.e. recommendation system
    usernamesList = list(model.ProductRecommendationSystem.index)

    # Converting List to a dataframe
    usernamesDF = pd.DataFrame(usernamesList, columns=['Available Usernames'])

    # Creating a HTML table using DataFrame
    usernameTable = [usernamesDF.to_html(classes='usernames')]
    # Defining Table title
    table_title = ['NAN', 'List of all usernames available in SBPRS Database']

    # Rendering the page
    return render_template('allusernames.html', usernameTable = usernameTable, titles = table_title )


# Starting Flask Application
if __name__ == '__main__' :
    app.run()