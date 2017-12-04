# coding: utf-8

# In[4]:

# run SQL commands to create a database: 
import numpy as np
import pandas as pd

import sqlite3

# Exectute SQL commands and store as an sqlite file (newthing.db):
qry = open('updated_jokedb.sql', 'r').read()
conn = sqlite3.connect('jokes.db')
c = conn.cursor()
c.executescript(qry)
conn.commit()
c.close()
conn.close()


# In[5]:

# read in the data:
conn = sqlite3.connect('jokes.db')


# In[6]:

# Get table names:
res = conn.execute("SELECT name FROM sqlite_master WHERE type='table';")
for name in res:
    print name[0]


# In[7]:

user_df = pd.read_sql_query("SELECT * FROM JokeRater", conn)


# In[8]:

rating_df = pd.read_sql_query("SELECT * FROM JokeRating", conn)


# In[10]:

rating_df.head()


# -------

# ## Analyzing the Discrete Distribution of User Ratings

# * **94** users in the database
# * **152** jokes rated at least once
# 

# In[52]:

get_ipython().magic('matplotlib inline')
import matplotlib.pyplot as plt


# 
# We can investigate the `JokeRater` Table directly to calculate the rating distribution for each user.

# In[11]:

# groupby() to split data per user:
ratings_per_user = rating_df.groupby(by='joke_rater_id')

# Calculate summary statistics (of ratings) on each split:
user_rating_desc = ratings_per_user.describe()['rating']


# In[64]:

user_rating_desc['var'] = np.square(user_rating_desc['std'])


# In[65]:

# What does the summary option return (for each user)?
user_rating_desc.head()


# ### _How many people had low variance in joke ratings?_

# **The extreme case of low variance: How many people had zero variance in rating?**

# In[47]:

zero_var_users = user_rating_desc.index[user_rating_desc['std'] == 0]

print "{} users had zero variance in ratings.".format(len(zero_var_users))

print "The number of jokes they rated: {}".format(list(user_rating_desc['count'][zero_var_users]))
print "Their ratings: {}".format(list(user_rating_desc['mean'][zero_var_users]))


# **The general case of low variance: How do we define "Low"? **
# 
# While it is an obvious choice to remove users with zero-variance in ratings, there should be more responses that could be "dishonest". To select some threshold for low variance users (which could possibly be elimited from downstream analysis), we consider the distribution of rating variance: 

# In[94]:

user_rating_desc_no0 = user_rating_desc.drop(zero_var_users)


# In[96]:

ratings_dist = user_rating_desc_no0['var'].describe()
ratings_dist


# In[79]:

# What is the range of variances?
( ratings_dist['max'] - ratings_dist['min'] )


# In[172]:

pd.DataFrame.hist(user_rating_desc_no0,column='var',bins = 100)
plt.title('Distribution of User Rating Variances \n (Excluding Zero-Variance Cases)')
plt.ylabel('Count')
plt.xlabel('Variance of 1-5 Ratings per User')


# By setting a high number of bins in the histogram, it becomes more clear where the potential cutoffs can be found. For instance, there seems to be a gap around the `0.5` variance region, so we will check users who exist below this threshold:

# In[101]:

low_var_users = user_rating_desc_no0.index[user_rating_desc_no0['var'] <= 0.5]


# In[124]:

low_var_df = user_rating_desc_no0.loc[low_var_users]
low_var_df


# In[173]:

len(low_var_df)


# Although the variances are indeed low for all these users, it requires some thinking to determine which ones are suspicious. To make the assessment more clear, we add columns indicating the counts for each rating (1-5) to the above dataframe:

# In[117]:

# re-create the original table of ratings without the zero-variance users:
rating_df_no0 = rating_df[~rating_df.joke_rater_id.isin(zero_var_users)]


# In[118]:

# We should now have 94-2 = 92 users present:
len(pd.unique(rating_df_no0['joke_rater_id']))


# In[ ]:

from collections import Counter


# In[165]:

for i in range(1,6):
    low_var_df[str(i)] = np.nan


# In[166]:

for user in low_var_df.index:
    # count the ratings for each user:
    ratings_counter = Counter(rating_df.groupby(by='joke_rater_id').get_group(user)['rating'])
    # add these counts to the summary output:
    for i in ratings_counter.keys():
        low_var_df.loc[user][str(i)] = ratings_counter[i]


# In[167]:

low_var_df


# The counts reveal the manner in which each user attained a variance below `0.5`. 
# 
# Though the variances are low, most of these users seem to have answered with some sense of "honesty".
# 

# It also becomes clear that a "low variance" criteria may not be sufficient, as users who exclusively select either 1 or 5 with equal frequency would not be included. 

# ---------

# Next, we try the same analysis for "high variance", though I personally don't expect anything crazy on this end. 

# In[176]:

hi_var_users = user_rating_desc_no0.index[user_rating_desc_no0['var'] >= 2.0]
hi_var_df = user_rating_desc_no0.loc[hi_var_users]

for i in range(1,6):
    hi_var_df[str(i)] = np.nan
    
for user in hi_var_df.index:
    # count the ratings for each user:
    ratings_counter = Counter(rating_df.groupby(by='joke_rater_id').get_group(user)['rating'])
    # add these counts to the summary output:
    for i in ratings_counter.keys():
        hi_var_df.loc[user][str(i)] = ratings_counter[i]
        
hi_var_df


# ---------

# ## Bias and other Patterns
# 

# 
# First, we will finish our analysis of the User Ratings by determining where the majority of ratings lie (between 1-5):

# In[183]:

pd.DataFrame.hist(rating_df_no0, column= 'rating')


# In[177]:

profile_df = pd.read_sql_query("SELECT * FROM JokeRater", conn)


# In[179]:

profile_df.head()


# In[230]:

def getlen(col): 
    return len(np.unique(col))


# In[233]:

profile_df.apply(getlen, axis=0)


# In[ ]:




# ---------

# ## Selection: Users

# In[200]:

# Normalized (User,Rating) matrix:
UR_mat = rating_df_no0.pivot(index='joke_rater_id',columns='joke_id',values='rating')
UR_matN = (UR_mat - UR_mat.mean())/UR_mat.std()


# In[246]:

all_user_features = profile_df.columns[2:]


# In[247]:

all_user_features


# In[276]:

# though this is called y_all, they are actually our predictors.
y_all = profile_df[profile_df['id'].isin(UR_matN.index)][all_user_features]


# In[253]:

# our actual y:
var_to_predict = user_rating_desc_no0['var']


# In[361]:

from sklearn.model_selection import train_test_split
X = pd.get_dummies(y_all).as_matrix()
y = var_to_predict.as_matrix()
Xtr,Xte,ytr,yte = train_test_split(X, y, test_size=0.33, random_state=42)


# Now we will try to predict rating variance per user:

# In[362]:

from sklearn.linear_model import LinearRegression
model = LinearRegression(fit_intercept=False)
model.fit(Xtr, ytr)


# In[341]:

from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
clf_ridge = Ridge(alpha=10)
clf_ridge.fit(Xtr,ytr)
clf_lasso = Lasso(alpha=0.0100)
clf_lasso.fit(Xtr,ytr)


# In[389]:

from sklearn.linear_model import RidgeCV
from sklearn.linear_model import LassoCV

clf_ridge = RidgeCV(alphas=(1,0.1,0.01,0.01))
clf_ridge.fit(Xtr,ytr)

clf_lasso = LassoCV(alphas=(0.1,0.01,0.01))
clf_lasso.fit(Xtr,ytr)

print 'MSE of 5-fold CV Ridge Regression with alpha {0} : {1}'.format(clf_ridge.alpha_,mean_squared_error(yte,clf_ridge.predict(Xte)))
print 'MSE of 5-fold CV LASSO Regression with alpha {0} : {1}'.format(clf_lasso.alpha_,mean_squared_error(yte,clf_lasso.predict(Xte)))


# In[390]:

from sklearn.metrics import mean_squared_error
print 'MSE of Ridge Regression: {}'.format(mean_squared_error(yte,clf_ridge.predict(Xte)))
print 'MSE of LASSO Regression: {}'.format(mean_squared_error(yte,clf_lasso.predict(Xte)))


# In[391]:

# check coefficients to see which predictors were most informative:
coefs_ridge_list = list(zip(clf_ridge.coef_, pd.get_dummies(y_all).columns))
coefs_lasso_list = list(zip(clf_lasso.coef_, pd.get_dummies(y_all).columns))
coefs_ridge_df = pd.DataFrame(coefs_ridge_list)
coefs_lasso_df = pd.DataFrame(coefs_lasso_list)

coefs_ridge_df.columns = ['coef','feature']
coefs_lasso_df.columns = ['coef','feature']

ridge_top10 = coefs_ridge_df.reindex(coefs_ridge_df.coef.abs().sort_values(ascending=False).index)[:10]
lasso_top10 = coefs_lasso_df.reindex(coefs_lasso_df.coef.abs().sort_values(ascending=False).index)[:10]


# In[392]:

lasso_top10


# As mentioned before, the ratings for each user depend on their own criteria. To counteract this phenomenon, we will create a (User, Joke) matrix and normalize each row:

# --------

# ## Variance in Rating per Joke

# Now, instead of looking at ratings per user, we will shift attention to ratings per joke. Unlike with users, where we wanted to identify their rating patterns, the goal with jokes is to determine some consensus measure of humor based on the 1-5 rating responses.
# 
# Following this analysis, we want to identify which features of a joke or user contribute to high/low ratings.

# In[188]:

rating_df_no0.head()


# In[189]:

ratings_per_joke = rating_df_no0.groupby(by='joke_id')


# In[192]:

joke_rating_desc = ratings_per_joke.describe()['rating']
joke_rating_desc['var'] = np.square(joke_rating_desc['std'])


# In[193]:

joke_rating_desc.head()


# In[197]:

# What is the range of variances?
joke_ratings_dist = joke_rating_desc['var'].describe()
( joke_ratings_dist['max'] - joke_ratings_dist['min'] )
# Does this matter?
pd.DataFrame.hist(joke_rating_desc,column='var',bins = 122)


# The joke-rating variances actually seem to be distributed much more normally than the user-rating measurements.

# ------
