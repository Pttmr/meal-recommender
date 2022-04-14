# meal-recommender

This app is the first attempt to predict a meal with a recommender.

Used libraries: **numpy, pandas, matplotlib, streamlit, tensorflow** 

-----------------------------

###The 'Groceries' page:
This page asks the visitor to upload a photo, which then uses an ImageClassification Model to identify the fruits in that picture. 

The recognized ingredients are added to the ingredient list in the fridge.
The recommender button then recommends a cooking recipe.

###The 'Cooking recipes' page:
This page collects and displays the cooking recipes.

###The 'Fridge' page:
The available ingredients are listed on the page.


----

###Lessons learned:
- version-control with github
- easy setup of web application with streamlit
- developing an image classification model with tensorflow

###Challenges:
- limited formatting of streamlit application
- not able to implement model into streamlit app
- not able to use uploaded image in developed model

###Next steps:
- find out how to load trained model in streamlit app
- connect databases