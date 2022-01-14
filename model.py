# Importing required libraries
import pandas as pd
import numpy as np
import pickle

# Importing constants for loading required variables
import constants



# Loading Recommendation System
ProductRecommendationSystem = pickle.load(file=open(constants.RECOMMENDATION_SYSTEM_PATH, 'rb'))

# Loading ProductReviewMapping (TRAIN)
processedProductReviewMapping = pd.read_csv(constants.PRODUCT_REVIEWS_MAPPING_PATH)

# Loading Vectorizer
vectorizer = pickle.load(file=open(constants.VECTORIZER_PATH, 'rb'))
# Loading Sentiment Classifier
SentimentClassifier = pickle.load(file=open(constants.SENTIMENT_CLASSIFIER_PATH, 'rb'))
# Loading the Probability Threshold
probThreshold = constants.PROBABILITY_THRESHOLD




# Defining function for Sentiment based Product Recommendations
def sentimentBasedProductRecommendations(username):
    '''
    This function takes username as input and
    generates top 5 product recommendations based on their preferences
    ::Uses Item-based Recommendation System::
    '''
    
    # Fetching top 20 recommendations for user
    try:
        top20_recommendations = (ProductRecommendationSystem
                                 .loc[username]
                                 .sort_values(ascending=False)[:20])
    except KeyError:
        # If user doesn't exist print the error message
        errorMessage = "ERROR: Unable to recommend products to username '{}', as it doesn't not exist in the system!\n\
            Please try again with another user that already exists in the system.".format(username)
        
        return errorMessage
    
    # Creating a Dictionary to store the percentage of positive sentiments
    recommendationsPositivePercentage = {}
    
    # Iterating over all the recommendations
    for recommendedProduct in top20_recommendations.index:
        
        # Filtering out the reviews_text from the Training Dataset
        filteredReviews = (processedProductReviewMapping
                           [processedProductReviewMapping['name'] == recommendedProduct]
                           ['reviews_text'])
        
        # Using Vectorizer to transform the filtered reviews
        vectorizedReviews = vectorizer.transform(filteredReviews)
        
        # Getting the sentiment probability using vectorized reviews
        sentimentProba = SentimentClassifier.predict_proba(vectorizedReviews).T[1]
        # Using probability threshold to label predictions
        reviewsSentiment = [1 if val>probThreshold else 0 for val in sentimentProba]
        
        # Calculating the percentatge of positive reviews
        positivePercentage = sum(reviewsSentiment) / len(reviewsSentiment)
        
        # Logging in the dictionary
        recommendationsPositivePercentage[recommendedProduct] = positivePercentage
        
    # Sorting the dictionary based on values in descending
    sortedByPositivePercentage = dict(sorted(recommendationsPositivePercentage.items(),
                                             key=lambda x : x[1],
                                             reverse=True))
    
    # Storing the recommendations in the required order and returning the top 5 recommendations
    recommendations = list(sortedByPositivePercentage.keys())[:5]
    
    # Returning the recommendations
    return recommendations