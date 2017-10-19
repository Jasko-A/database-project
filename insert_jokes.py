# insert_jokes.py
# script to insert jokes from joke csv to our db

def insert_jokes(filename='jokes.csv'):
	import csv
	from api.models import Joke

	TEXT = 2
	CATEGORY = 3
	SUBJECT = 4
	TYPE_OF_JOKE = 5
	JOKE_LENGTH = 6
	NSFW = 8

	with open(filename, 'r') as csvfile:
		reader = csv.reader(csvfile)
		num = 0
		firstline = True
		for row in reader:

			if firstline:
				firstline = False
				continue

			joke_text = row[TEXT]
			joke_category = row[CATEGORY].lower()
			joke_subj = row[SUBJECT]
			joke_type = '_'.join(row[TYPE_OF_JOKE].lower().split(' '))
			joke_length = row[JOKE_LENGTH].lower()
			joke_nsfw = True if row[NSFW].lower() == 'yes' else False

			try:
				Joke.objects.create(
						category=joke_category,
						joke_type=joke_type,
						joke_length=joke_length,
						nsfw=joke_nsfw,
						subject=joke_subj,
						joke_text=joke_text
					)
			except Exception as e:
				print "joke {0} | {1}".format(num, e)

			num += 1

