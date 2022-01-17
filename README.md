# Sentiment Based Product Recommendation System

The e-commerce business is quite popular today. Here, we do not need to take orders by going to each customer. A company launches its website to sell the items to the end consumer, and customers can order the products that they require from the same website. Famous examples of such e-commerce companies are Amazon, Flipkart, Myntra, Paytm and Snapdeal.

Here , we used a data for an fictional company  named "Ebuss" that sells products in various categories such as household essentials, books, personal care products, medicines, cosmetic items, beauty products, electrical appliances, kitchen and dining products and health care products.

With the advancement in technology, it is imperative for Ebuss to grow quickly in the e-commerce market to become a major leader in the market because it has to compete with the likes of Amazon, Flipkart, etc., which are already market leaders.
 
Here, our task is to build a model that will improve the recommendations given to the users given their past reviews and ratings. 

In order to do this, I planned to build a sentiment-based product recommendation system, which includes the following tasks.

- Data sourcing and Sentiment Analysis
- Building a Recommendation System
- Improving the recommendations using the Sentiment Analysis model

So, this project has the following workflow:
1. User enters the username (From the system database)
2. Recommender System runs in the background to recommend products based on their past data. 
3. Reviews of these products are passed to __Sentiment Classifier__ to fine-tune the recommendations based on their review sentiments from other users. 
4. This will eventually improve the recommedations and help the user choose the product effectively.

 __Recommender System__ : Collaborative Filter (Item-based) i.e. Similarity b/w items is used for recommendations
 __Sentiment Classifier__ : Logistic Regression based Sentiment Classifier is used