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
    username =  str(request.form.get('username'))
    recommendations = model.sentimentBasedProductRecommendations(username)
    recommendations = pd.DataFrame(recommendations, columns=['Product Recommendations'])
    # tables=[recommendations.to_html(classes='Product Recommendations')], titles = ['NAN', 'Product Recommendations']
    return  render_template('index.html', result=recommendations)







# Starting Flask Application
if __name__ == '__main__' :
    app.run(debug=True )






