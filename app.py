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
    recommendations = model.sentimentBasedProductRecommendations(username)
    # Converting recommendations list to a dataFrame
    recommendations = pd.DataFrame(recommendations, columns=['Product Recommendations'])

    # Creating a HTML table using DataFrame
    recommendations_table = [recommendations.to_html(classes='recommendations')]
    # Defining Table title
    table_title = ['NAN', 'Top 5 Product Recommendations for : {}'.format(username)]

    # Rendering Template while passing the results
    return  render_template('index.html', productsTable = recommendations_table, titles=table_title)



# Starting Flask Application
if __name__ == '__main__' :
    app.run(debug=True )






