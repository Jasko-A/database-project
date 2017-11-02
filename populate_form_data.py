# populate_form_data.py
# Populates the data into the db from the google form stuff.
# exec(open('populate_form_data.py').read()); populate_user_data()

def populate_user_data(filename='users.csv'):
    '''
    Create JokeRater records for all people who filled out 
    the UserProfile form.
    '''
    import csv
    from api.models import JokeRater

    GENDER = 1
    AGE = 2
    COUNTRY = 3
    MAJOR = 4
    PREF_JOKE_GENRE = 5
    PREF_JOKE_GENRE2 = 6
    PREF_JOKE_TYPE = 7
    FAV_MUSIC_GENRE = 8
    FAV_MOVIE_GENRE = 9
    JOKE_SUBM_ID = 10

    csvfile = open(filename, 'r')
    reader = csv.reader(csvfile, delimiter=',')
    firstline = True
    for row in reader:
        if firstline == True:
            firstline = False
            continue
        elif not row:
            continue

        gender = row[GENDER]
        age = int(row[AGE])
        country = row[COUNTRY]
        major = row[MAJOR]
        pref_joke_genre = row[PREF_JOKE_GENRE]
        pref_joke_genre2 = row[PREF_JOKE_GENRE2]
        pref_joke_type = row[PREF_JOKE_TYPE]
        favorite_music_genre = row[FAV_MUSIC_GENRE]
        favorite_movie_genre = row[FAV_MOVIE_GENRE]
        joke_submitter_id = row[JOKE_SUBM_ID]

        try:
            JokeRater.objects.create(
                joke_submitter_id=joke_submitter_id,
                gender=gender,
                age=age,
                birth_country=country,
                major=major,
                preferred_joke_genre=pref_joke_genre,
                preferred_joke_genre2=pref_joke_genre2,
                preferred_joke_type=pref_joke_type,
                favorite_music_genre=favorite_music_genre,
                favorite_movie_genre=favorite_movie_genre
            )
        except Exception as e:
            print("Error at row {0}. {1}".format(row, e))
            continue
    csvfile.close()


def populate_jokes(filename='jokes.tsv'):
    '''
    Create a JokeRecord and corresponding JokeRater record for all
    people who filled out the JokeForm.
    '''
    import csv
    from api.models import Joke, JokeRater

    csvfile = open(filename, 'r')
    reader = csv.reader(csvfile, delimiter='\t')

    for row in reader:
        if not row:
            continue

        # parse the row
        try:
            joke_source = row[0]
            if joke_source[0] == 'C':
                joke_category     = row[1]
                joke_type         = row[2]
                joke_text         = row[3]
                joke_subject      = row[4]
                joke_submitter_id = row[5]
            elif joke_source[0] == 'D':
                joke_text         = row[1]
                joke_category     = row[2]
                joke_subject      = row[3]
                joke_type         = row[4]
                joke_submitter_id = None
            else:
                print("A WEIRD ROW GOT IN:", row)
        except Exception as e:
            print("Invalid row:", row, e)
            continue

        # try to create the joke (and include the joke rater if there was one)
        try:
            if joke_submitter_id:
                joke_rater = JokeRater.objects.get(joke_submitter_id=joke_submitter_id)
                Joke.objects.create(
                    joke_source=joke_source,
                    category=joke_category,
                    subject=joke_subject,
                    joke_text=joke_text,
                    joke_type=joke_type,
                    joke_submitter=joke_rater
                )
            else:
                Joke.objects.create(
                    joke_source=joke_source,
                    category=joke_category,
                    subject=joke_subject,
                    joke_text=joke_text,
                    joke_type=joke_type
                )
        except Exception as e:
            print("Error with joke {0}: {1}".format(row, e))
            continue

    csvfile.close()

def populate_ratings(filename='ratings.csv'):
    '''
    '''
    import csv
    from api.models import Joke, JokeRater, JokeRating

    csvfile = open(filename, 'r')
    reader = csv.reader(csvfile, delimiter=',')

    firstline = True
    for row in reader:
        if firstline == True:
            firstline = False
            joke_identifiers = row[2:]
            print("identifiers:", joke_identifiers)
            continue
        elif not row:
            continue

        try:
            joke_rater = JokeRater.objects.get(joke_submitter_id=row[1])
        except:
            print("Couldn't insert ratings for {0}.".format(row[1]))
            continue

        print("RATER: {0}".format(joke_rater))
        for index, rating in enumerate(row[2:]):
            # if they skipped a joke
            if not rating: continue

            try:
                joke = Joke.objects.get(joke_source=joke_identifiers[index])
            except Exception as e:
                print("Couldnt find joke {0}: {1}".format(joke_identifiers[index], e))
                continue
            print("Index: {0} | Rating: {1} | JokeID: {2}".format(
                    index, rating, joke.joke_source
                ))

            JokeRating.objects.create(
                    joke=joke,
                    joke_rater=joke_rater,
                    rating=int(rating)
                )

        print("\n")

    csvfile.close()


