import pyodbc
import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf as bpdf
import numpy as np


class Server:

	ages = {}
	majors = {}
	genders = {}
	birth_countries = {}
	preferred_joke_types = {}
	favorite_movie_genres = {}
	favorite_music_genres = {}
	preferred_joke_genres = {}

	def __init__(self):
		self.server = 'ecs171jokedb.database.windows.net'
		self.database = 'jokedb'
		self.username = 'test'
		self.password = 'Password3'
		self.driver = '{ODBC Driver 13 for SQL Server}'
		self.cnxn = pyodbc.connect(self.connect_profile())
	
	def connect_profile(self):
		return 'DRIVER=' + self.driver + ';PORT=1433;SERVER=' + self.server + ';PORT=1443;DATABASE=' + self.database + ';UID=' + self.username + ';PWD=' + self.password

	def update_vals(self, row):
		if row.age not in self.ages:
			self.ages.update({row.age:1})
		else:
			self.ages[row.age] += 1

		if row.major not in self.majors:
			self.majors.update({row.major:1})
		else:
			self.majors[row.major] += 1

		if row.gender not in self.genders:
			self.genders.update({row.gender:1})
		else:
			self.genders[row.gender] += 1;

		if row.preferred_joke_type not in self.preferred_joke_types:
			self.preferred_joke_types.update({row.preferred_joke_type:1})
		else:
			self.preferred_joke_types[row.preferred_joke_type] +=1

		if row.preferred_joke_genre not in self.preferred_joke_genres:
			self.preferred_joke_genres.update({row.preferred_joke_genre:1})
		else:
			self.preferred_joke_genres[row.preferred_joke_genre] += 1

		if row.preferred_joke_genre2 not in self.preferred_joke_genres:
			self.preferred_joke_genres.update({row.preferred_joke_genre2:1})
		else:
			self.preferred_joke_genres[row.preferred_joke_genre2] += 1

		if row.favorite_music_genre not in self.favorite_music_genres:
			self.favorite_music_genres.update({row.favorite_music_genre:1})
		else:
			self.favorite_music_genres[row.favorite_music_genre] += 1

		if row.favorite_movie_genre not in self.favorite_movie_genres:
			self.favorite_movie_genres.update({row.favorite_movie_genre:1})
		else:
			self.favorite_movie_genres[row.favorite_movie_genre] += 1

		if row.birth_country not in self.birth_countries:
			self.birth_countries.update({row.birth_country:1})
		else:
			self.birth_countries[row.birth_country] += 1


	def print_info(self):
		f = open("goyal_shaifali_user_counts.txt", "w")
		f.write('AGES:\n')
		f.write(str(self.ages))
		f.write('\n\nGENDERS:\n')
		f.write(str(self.genders))		
		f.write('\n\nBIRTH_COUNTRIES:\n')
		f.write(str(self.birth_countries))
		f.write('\n\nMAJORS:\n')
		f.write(str(self.majors))		
		f.write('\n\nPREFERRED_JOKE_TYPES:\n')
		f.write(str(self.preferred_joke_types))
		f.write("\n\nPREFERRED_JOKE_GENRES:\n")
		f.write(str(self.preferred_joke_genres))
		f.write("\n\nPREFERRED_MOVIE_GENRES:\n")
		f.write(str(self.favorite_movie_genres))
		f.write("\n\nPREFERRED_MUSIC_GENRES:")
		f.write(str(self.favorite_music_genres))
		f.close()

	def make_plots(self):
		pdf = bpdf.PdfPages('goyal_shaifali_user_distributions.pdf')
		
		plt.figure(1)
		plt.title('Ages')
		plt.bar(np.arange(len(self.ages.keys())), self.ages.values(), align='center')
		plt.xticks(np.arange(len(self.ages.keys())), self.ages.keys(), rotation=90)
		plt.tight_layout()
		plt.ylabel('number of people')
		plt.xlabel('ages')
		pdf.savefig()

		plt.figure(2)
		plt.title('Genders')
		plt.bar(np.arange(len(self.genders.keys())), self.genders.values(), align='center')
		plt.xticks(np.arange(len(self.genders.keys())), self.genders.keys(), rotation=90)
		plt.tight_layout()
		plt.ylabel('number of people')
		plt.xlabel('genders')
		pdf.savefig()

		plt.figure(3)
		plt.title('Major Distributions')
		plt.bar(np.arange(len(self.majors.keys())), self.majors.values(), align='center')
		plt.xticks(np.arange(len(self.majors.keys())), self.majors.keys(), rotation=90)
		plt.tight_layout()
		plt.ylabel('number of people')
		plt.xlabel('majors')
		pdf.savefig()

		plt.figure(4)
		plt.title('Birth Country Distributions')
		plt.bar(np.arange(len(self.birth_countries.keys())), self.birth_countries.values(), align='center')
		plt.xticks(np.arange(len(self.birth_countries.keys())), self.birth_countries.keys(), rotation=90)
		plt.tight_layout()
		plt.ylabel('number of people')
		pdf.savefig()

		plt.figure(5)
		plt.title('Preferred Joke Types')
		plt.bar(np.arange(len(self.preferred_joke_types.keys())), self.preferred_joke_types.values(), align='center')
		plt.xticks(np.arange(len(self.preferred_joke_types.keys())), self.preferred_joke_types.keys(), rotation=90)
		plt.tight_layout()
		plt.ylabel('number of people')
		pdf.savefig()

		plt.figure(6)
		plt.title('Preferred Joke Genres')
		plt.bar(np.arange(len(self.preferred_joke_genres.keys())), self.preferred_joke_genres.values(), align='center')
		plt.xticks(np.arange(len(self.preferred_joke_genres.keys())), self.preferred_joke_genres.keys(), rotation=90)
		plt.tight_layout()
		plt.ylabel('number of people')
		pdf.savefig()

		plt.figure(7)
		plt.title('Preferred Movie Genres')
		plt.bar(np.arange(len(self.favorite_movie_genres.keys())), self.favorite_movie_genres.values(), align='center')
		plt.xticks(np.arange(len(self.favorite_movie_genres.keys())), self.favorite_movie_genres.keys(), rotation=90)
		plt.tight_layout()
		plt.ylabel('number of people')
		pdf.savefig()

		plt.figure(8)
		plt.title('Preferred Music Genres')
		plt.bar(np.arange(len(self.favorite_music_genres.keys())), self.favorite_music_genres.values(), align='center')
		plt.xticks(np.arange(len(self.favorite_music_genres.keys())), self.favorite_music_genres.keys(), rotation=90)
		plt.tight_layout()
		plt.ylabel('number of people')
		pdf.savefig()
		pdf.close()


if __name__ == "__main__":
	server = Server()
	cursor = server.cnxn.cursor()

	num_users = cursor.execute('select COUNT(*) from JokeRater').fetchval()
	print 'NUM_USERS:' + str(num_users)

	row = cursor.execute('select * from JokeRater')

	row = cursor.fetchone()
	while row:
		server.update_vals(row)
		row = cursor.fetchone()

	server.print_info()
	server.make_plots()

