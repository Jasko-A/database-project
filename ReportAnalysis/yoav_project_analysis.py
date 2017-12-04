import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st

user_features = {'id': 0, 'joke_submitter_id': 1, 'gender': 2, 'birth_country': 3, 'major': 4, 'preferred_joke_genre': 5,
'preferred_joke_genre2': 6, 'preferred_joke_type': 7, 'favorite_music_genre': 8, 'favorite_movie_genre': 9, 'age': 10}

conn = sqlite3.connect('jokedb.db')
c = conn.cursor()
c.execute('SELECT * FROM JokeRater')
users = {}
user_genres = []
user_cats = []
row = c.fetchone()

gender = {}
birth_country = {}
major = {}
ages = {}
preferred_joke_genre = {}
preferred_category = {}
favorite_music = {}
favorite_movie = {}
count = 0
j_count = 0
while row:
    count += 1
    users[row[0]] = row
    if not row[5] in user_genres:
        user_genres.append(row[5])
    if not row[7] in user_cats:
        user_cats.append(row[7])

    if not row[2] in gender:
        gender[row[2]] = 0
    gender[row[2]] += 1

    if not row[3] in birth_country:
        birth_country[row[3]] = 0
    birth_country[row[3]] += 1

    if not row[4] in major:
        major[row[4]] = 0
    major[row[4]] += 1
    
    if row[5] == '':
        if not 'Other' in preferred_joke_genre:
            preferred_joke_genre['Other'] = 0
        preferred_joke_genre['Other'] += 1
    else:
        if not row[5] in preferred_joke_genre:
            preferred_joke_genre[row[5]] = 0
        preferred_joke_genre[row[5]] += 1
    j_count += 1
    if row[6] == '':
        pass
    else:
        j_count += 1
        if not row[6] in preferred_joke_genre:
            preferred_joke_genre[row[6]] = 0
        preferred_joke_genre[row[6]] += 1

    if row[7] == '':
        if not 'Other' in preferred_category:
            preferred_category['Other'] = 0
        preferred_category['Other'] += 1
    else:
        if not row[7] in preferred_category:
            preferred_category[row[7]] = 0
        preferred_category[row[7]] += 1

    if not row[8] in favorite_music:
        favorite_music[row[8]] = 0
    favorite_music[row[8]] += 1

    if not row[9] in favorite_movie:
         favorite_movie[row[9]] = 0
    favorite_movie[row[9]] += 1

    if not row[10] in ages:
        ages[row[10]] = 0
    ages[row[10]] += 1

    row = c.fetchone()
    
#                   GENRE    STRUCTURE
c.execute('SELECT id,category, joke_type FROM Joke')
jokes = {}
row = c.fetchone()
genres = []
types = []
gs = {}
cs = {}
count = 0
while row:
    jokes[row[0]] = row
    if not row[1] in genres:
        genres.append(row[1])
    if not row[2] in types:
        types.append(row[2])

    if not row[1] in gs:
        gs[row[1]] = 0
    gs[row[1]] += 1

    if not row[2] in cs:
        cs[row[2]] = 0
    cs[row[2]] += 1
    count+=1
    row = c.fetchone()


# Let's see if users actually preferred jokes of their preferred joke genre
joke_ratings = {}
for genre in user_genres:
    joke_ratings[genre] = {}
    joke_ratings[genre]['Preferred'] = []
    joke_ratings[genre]['Not Preferred'] = []
    joke_ratings[genre]['Other Jokes'] = []
    for joke_id in jokes:
        # We want to see if users who preferred a genre rated that genre higher than other people who didn't prefer it
        if jokes[joke_id][1] == genre:
            c.execute('SELECT rating, joke_rater_id, joke_id FROM JokeRating WHERE joke_id = {}'.format(joke_id))
            ratings = c.fetchall()
            for rating in ratings:
                # If the current user prefers the current genre, add them to the "preferred" list.
                if users[rating[1]][5] == genre or users[rating[1]][6] == genre:
                    joke_ratings[genre]['Preferred'].append(rating[0])
                else:
                    joke_ratings[genre]['Not Preferred'].append(rating[0])
        # We also want to see if the users who preferred a genre rated those jokes higher than other jokes
        else:
            c.execute('SELECT rating, joke_rater_id, joke_id FROM JokeRating WHERE joke_id = {}'.format(joke_id))
            ratings = c.fetchall()
            for rating in ratings:
                # If the current user prefers the current genre, add them to the "preferred" list.
                if users[rating[1]][5] == genre or users[rating[1]][6] == genre:
                    joke_ratings[genre]['Other Jokes'].append(rating[0])

ind = np.arange(len(joke_ratings))
bar_width = .4

pref_means = []
pref_stds = []
not_pref_means = []
not_pref_stds = []
other_jokes = []
other_stds = []

all_pref = []
all_not = []
all_other = []

p_scores = {}

for genre in joke_ratings:
    pref_means.append(np.mean(joke_ratings[genre]['Preferred']))
    pref_stds.append(np.std(joke_ratings[genre]['Preferred']))

    not_pref_means.append(np.mean(joke_ratings[genre]['Not Preferred']))
    not_pref_stds.append(np.std(joke_ratings[genre]['Not Preferred']))

    other_jokes.append(np.mean(joke_ratings[genre]['Other Jokes']))
    other_stds.append(np.std(joke_ratings[genre]['Other Jokes']))

    p_scores[genre] = {}

    # Get p-score for ratings of genres for preferred vs. not preferred
    diff = np.mean(joke_ratings[genre]['Preferred']) - np.mean(joke_ratings[genre]['Not Preferred'])
    sigma = np.sqrt(np.var(joke_ratings[genre]['Preferred']) / len(joke_ratings[genre]['Preferred']) + np.var(joke_ratings[genre]['Not Preferred']) / len(joke_ratings[genre]['Not Preferred']))
    p_scores[genre]['Pref vs. Not Pref'] = .5 - diff/sigma

    diff = np.mean(joke_ratings[genre]['Preferred']) - np.mean(joke_ratings[genre]['Other Jokes'])
    sigma = np.sqrt(np.var(joke_ratings[genre]['Preferred']) / len(joke_ratings[genre]['Preferred']) + np.var(joke_ratings[genre]['Other Jokes']) / len(joke_ratings[genre]['Other Jokes']))
    p_scores[genre]['Pref vs. Other'] = .5 - diff/sigma

    for i in joke_ratings[genre]['Preferred']:
        all_pref.append(i)
    for i in joke_ratings[genre]['Not Preferred']:
        all_not.append(i)
    for i in joke_ratings[genre]['Other Jokes']:
        all_other.append(i)

p_scores['Overall'] = {}
p_scores['Overall']['Pref vs. Not Pref'] = (np.mean(all_pref) - np.mean(all_not)) / np.sqrt(np.var(all_pref)/len(all_pref) + np.var(all_not) / len(all_not))
p_scores['Overall']['Pref vs. Other'] = (np.mean(all_pref) - np.mean(all_other)) / np.sqrt(np.var(all_pref)/len(all_other) + np.var(all_not) / len(all_other))



fig, axes = plt.subplots(nrows = 2, sharex = False)
ax = axes[0]
rects1 = ax.bar(ind, pref_means, bar_width, color='b', yerr=pref_stds)
rects2 = ax.bar(ind+bar_width, not_pref_means, bar_width, color='r', yerr=not_pref_stds)

ax.set_ylabel('Mean Ratings')
ax.set_title('Mean Ratings of Jokes of Genres, Preferred vs. Not Preferred')
ax.set_xticks(ind + bar_width / 2)
ax.set_xticklabels([genre for genre in joke_ratings])
ax.set_yticks([1,2,3,4,5])

ax.legend((rects1[0], rects2[0]), ('Preferred Genre', 'Not Preferred Genre'), loc='center left', bbox_to_anchor=(.95, .99))

ax = axes[1]
rects1 = ax.bar(ind, pref_means, bar_width, color='b', yerr=pref_stds)
rects2 = ax.bar(ind+bar_width, other_jokes, bar_width, color='g', yerr=other_stds)

ax.set_ylabel('Mean Ratings')
ax.set_title('Mean Ratings of Preferred Genre vs. Other Genres')
ax.set_xticks(ind + bar_width / 2)
ax.set_xticklabels([genre for genre in joke_ratings])
ax.set_yticks([1,2,3,4,5])

ax.legend((rects1[0], rects2[0]), ('Preferred Genre', 'Other Genres'), loc='center left', bbox_to_anchor=(.95, .99))


plt.show()

fig, axs = plt.subplots()
columns = ('Pref vs. Not Pref', 'Jokes of Pref vs. Other Jokes')
rows = [genre for genre in p_scores]
table_vals = []
for genre in rows:
    table_vals.append([str(st.norm(0,1).cdf(-1 * ((p_scores[genre]['Pref vs. Not Pref'])**2)**5)), str(st.norm(0,1).cdf(-1 * ((p_scores[genre]['Pref vs. Other'])**2)**5))])

axs.axis('tight')
axs.axis('off')
the_table = axs.table(cellText=table_vals, rowLabels=rows, colLabels = columns, loc='center')

plt.show()


# Now, do same thing but for joke type -----------------
joke_ratings = {}
for category in user_cats:
    joke_ratings[category] = {}
    joke_ratings[category]['Preferred'] = []
    joke_ratings[category]['Not Preferred'] = []
    joke_ratings[category]['Other Jokes'] = []

    joke_cat = category
    if category == 'Puns':
        joke_cat = 'Pun'
    elif category == 'Pick-up Line':
        joke_cat = 'Pick Up Line'
    elif category == 'One-Liner':
        joke_cat = 'One-liner'
    elif category == 'Fun fact':
        joke_cat = 'Fun Fact'

    
    for joke_id in jokes:
        # We want to see if users who preferred a category rated that category higher than other people who didn't prefer it
        if jokes[joke_id][2] == joke_cat:
            c.execute('SELECT rating, joke_rater_id, joke_id FROM JokeRating WHERE joke_id = {}'.format(joke_id))
            ratings = c.fetchall()
            for rating in ratings:
                # If the current user prefers the current category, add them to the "preferred" list.
                if users[rating[1]][7] == category:
                    joke_ratings[category]['Preferred'].append(rating[0])
                else:
                    joke_ratings[category]['Not Preferred'].append(rating[0])
        # We also want to see if the users who preferred a category rated those jokes higher than other jokes
        else:
            c.execute('SELECT rating, joke_rater_id, joke_id FROM JokeRating WHERE joke_id = {}'.format(joke_id))
            ratings = c.fetchall()
            for rating in ratings:
                # If the current user prefers the current category, add them to the "preferred" list.
                if users[rating[1]][7] == category:
                    joke_ratings[category]['Other Jokes'].append(rating[0])

ind = np.arange(len(joke_ratings))
bar_width = .4



pref_means = []
pref_stds = []
not_pref_means = []
not_pref_stds = []
other_jokes = []
other_stds = []
p_scores = {}

all_pref = []
all_not = []
all_other = []

for category in joke_ratings:
    pref_means.append(np.mean(joke_ratings[category]['Preferred']))
    pref_stds.append(np.std(joke_ratings[category]['Preferred']))

    not_pref_means.append(np.mean(joke_ratings[category]['Not Preferred']))
    not_pref_stds.append(np.std(joke_ratings[category]['Not Preferred']))

    other_jokes.append(np.mean(joke_ratings[category]['Other Jokes']))
    other_stds.append(np.std(joke_ratings[category]['Other Jokes']))

    p_scores[category] = {}

    # Get p-score for ratings of categorys for preferred vs. not preferred
    diff = np.mean(joke_ratings[category]['Preferred']) - np.mean(joke_ratings[category]['Not Preferred'])
    sigma = np.sqrt(np.var(joke_ratings[category]['Preferred']) / len(joke_ratings[category]['Preferred']) + np.var(joke_ratings[category]['Not Preferred']) / len(joke_ratings[category]['Not Preferred']))
    p_scores[category]['Pref vs. Not Pref'] = diff/sigma

    diff = np.mean(joke_ratings[category]['Preferred']) - np.mean(joke_ratings[category]['Other Jokes'])
    sigma = np.sqrt(np.var(joke_ratings[category]['Preferred']) / len(joke_ratings[category]['Preferred']) + np.var(joke_ratings[category]['Other Jokes']) / len(joke_ratings[category]['Other Jokes']))
    p_scores[category]['Pref vs. Other'] = diff/sigma

    for i in joke_ratings[category]['Preferred']:
        all_pref.append(i)
    for i in joke_ratings[category]['Not Preferred']:
        all_not.append(i)
    for i in joke_ratings[category]['Other Jokes']:
        all_other.append(i)

p_scores['Overall'] = {}
p_scores['Overall']['Pref vs. Not Pref'] = (np.mean(all_pref) - np.mean(all_not)) / np.sqrt(np.var(all_pref)/len(all_pref) + np.var(all_not) / len(all_not))
p_scores['Overall']['Pref vs. Other'] = (np.mean(all_pref) - np.mean(all_other)) / np.sqrt(np.var(all_pref)/len(all_other) + np.var(all_not) / len(all_other))

fig, axes = plt.subplots(nrows = 2, sharex = False)
ax = axes[0]
rects1 = ax.bar(ind, pref_means, bar_width, color='b', yerr=pref_stds)
rects2 = ax.bar(ind+bar_width, not_pref_means, bar_width, color='r', yerr=not_pref_stds)

ax.set_ylabel('Mean Ratings')
ax.set_title('Mean Ratings of Jokes by Category, Preferred vs. Not Preferred')
ax.set_xticks(ind + bar_width / 2)
ax.set_xticklabels([category for category in joke_ratings])
ax.set_yticks([1,2,3,4,5])

ax.legend((rects1[0], rects2[0]), ('Preferred Category', 'Not Preferred Category'), loc='center left', bbox_to_anchor=(.9, .99))

ax = axes[1]
rects1 = ax.bar(ind, pref_means, bar_width, color='b', yerr=pref_stds)
rects2 = ax.bar(ind+bar_width, other_jokes, bar_width, color='g', yerr=other_stds)

ax.set_ylabel('Mean Ratings')
ax.set_title('Mean Ratings of Preferred Category vs. Other Categories')
ax.set_xticks(ind + bar_width / 2)
ax.set_xticklabels([category for category in joke_ratings])
ax.set_yticks([1,2,3,4,5])

ax.legend((rects1[0], rects2[0]), ('Preferred Category', 'Other Categories'), loc='center left', bbox_to_anchor=(.95, .99))


plt.show()


fig, axs = plt.subplots()
columns = ('Pref vs. Not Pref', 'Jokes of Pref vs. Other Jokes')
rows = [genre for genre in p_scores]
table_vals = []
for genre in rows:
    table_vals.append([str(st.norm(0,1).cdf(-1 * ((p_scores[genre]['Pref vs. Not Pref'])**2)**5)), str(st.norm
                                                                                                       (0,1).cdf(-1 * ((p_scores[genre]['Pref vs. Other'])**2)**5))])

axs.axis('tight')
axs.axis('off')
the_table = axs.table(cellText=table_vals, rowLabels=rows, colLabels = columns, loc='center')


plt.show()
