import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#LOCATION OF USER PROFILE FILE IN SYSTEM
#all rows with empty values for certain user categories were manually removed
#from file
#Top row with column names also manually removed
#All rows with empty values were also manually removed
dataFileLoc = b'C:\Users\Ronen\Downloads\UserProfile.csv'

df = pd.read_csv(dataFileLoc, names = ['Timestamp', 'Gender', 'Age', 'Country', 'Major', 'Preferred', '2nd Preferred', 'PreferredType', 'MusicGenre', 'MovieGenre', 'ID'])
print(len(df.index))

def plotGenderAndGenres():
    #males plot
    maleGenres = []
    for i in range(len(df.index)):
        if(df.Gender[i]=="Male"):
            maleGenres.append(df.Preferred[i])

    maleGenreFrequencies = [maleGenres.count("Nerd"), maleGenres.count("Animal"), maleGenres.count("Programming"), maleGenres.count("Politics"),
                        maleGenres.count("School"), maleGenres.count("Other"), maleGenres.count("Sports"), maleGenres.count("Math"), maleGenres.count("Medicine/Doctor")]

    #females plot
    femaleGenres = []
    for i in range(len(df.index)):
        if(df.Gender[i]=="Female"):
            femaleGenres.append(df.Preferred[i])

    femaleGenreFrequencies = [femaleGenres.count("Nerd"), femaleGenres.count("Animal"), femaleGenres.count("Programming"), femaleGenres.count("Politics"),
                        femaleGenres.count("School"), femaleGenres.count("Other"), femaleGenres.count("Sports"), femaleGenres.count("Math"), femaleGenres.count("Medicine/Doctor")]

    fig, ax = plt.subplots()
    index = np.arange(9)
    bar_width = 0.35
    opacity = 0.8
 
    rects1 = plt.bar(index, maleGenreFrequencies, bar_width,
                 alpha=opacity,
                 color='b',
                 label='Male')
 
    rects2 = plt.bar(index + bar_width, femaleGenreFrequencies, bar_width,
                 alpha=opacity,
                 color='g',
                 label='Female')
 
    plt.xlabel('Gender')
    plt.ylabel('Popular Joke Genres')
    plt.title('Genres By Gender')
    plt.xticks(index + bar_width, ('Nerd', 'Animal', 'Programming', 'Politics', 'School', 'Other', 'Sports', 'Math', 'Medicine/Doctor'))
    plt.legend()
 
    plt.tight_layout()
    plt.show()

#plotGenderAndGenres()

def plotAgeAndGenres():
    ageGenres = []
    for i in range(19, 31):
        subArr = []
        for j in range(len(df.index)):
            if(df.Age[j]==i):
                subArr.append(df.Preferred[j])
        ageGenres.append(subArr)

    ageGenreFreqs = []
    genreList = ["Nerd", "Animal", "Programming", "Politics", "School", "Other", "Sports", "Math", "Medicine/Doctor"]
    for i in range(12):
        subArr = []
        for j in range(len(genreList)):
            subArr.append(ageGenres[i].count(genreList[j]))
        ageGenreFreqs.append(subArr)
            
    fig, ax = plt.subplots()
    index = np.arange(9)
    bar_width = 0.1    
    opacity = 0.9        

    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
    for i in range(7):
        rects = plt.bar(index + bar_width*i, ageGenreFreqs[i], bar_width,
                 alpha=opacity,
                 color=colors[i],
                 label=str(i + 19))

    plt.xlabel('Age')
    plt.ylabel('Popular Joke Genres')
    plt.title('Genres By Age')    
    plt.xticks(index + bar_width, genreList)
    plt.legend()
 
    plt.tight_layout()
    plt.show()

#plotAgeAndGenres()


def plotMajorsAndGenres():
    majors = ["Computer Science/CSE", "Physics", "Statistics", "Electrical Engineering", "Math"]
    majorGenres = []
    for i in range(len(majors) + 1):
        subArr = []
        for j in range(len(df.index)):
            userMajor = df.Major[j]
            if(userMajor=="Computer Science and Physics"):
                userMajor = "Physics"
            if(userMajor=="EE/CE" or userMajor=="Electrical"):
                userMajor = "Electrical Engineering"
            if(i < len(majors)):
                if(userMajor==majors[i]):
                    subArr.append(df.Preferred[j])
            else:
                if(userMajor not in majors):
                    subArr.append(df.Preferred[j])
        majorGenres.append(subArr)

    majorGenreFreqs = []
    genreList = ["Nerd", "Animal", "Programming", "Politics", "School", "Other", "Sports", "Math", "Medicine/Doctor"]
    for i in range(len(majors) + 1):
        subArr = []
        for j in range(len(genreList)):
            subArr.append(majorGenres[i].count(genreList[j]))
        majorGenreFreqs.append(subArr)
            
    fig, ax = plt.subplots()
    index = np.arange(9)
    bar_width = 0.1    
    opacity = 0.9        

    majors = ["Computer Science/CSE", "Physics", "Statistics", "Electrical Engineering", "Math", "Other"]
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
    for i in range(len(majors)):
        rects = plt.bar(index + bar_width*i, majorGenreFreqs[i], bar_width,
                 alpha=opacity,
                 color=colors[i],
                 label=str(majors[i]))

    plt.xlabel('Major')
    plt.ylabel('Joke Genre Popularity')
    plt.title('Genre Popularity By Major')    
    plt.xticks(index + bar_width, genreList)
    plt.legend()
 
    plt.tight_layout()
    plt.show()

#plotMajorsAndGenres()

def plotCategoriesAndGenres():
    categories = ["Puns", "Punch line", "Question", "Fun fact", "One-Liner", "Dialogue"]
    categoryGenres = []
    for i in range(len(categories)):
        subArr = []
        for j in range(len(df.index)):
            if(df.PreferredType[j]==categories[i]):
                subArr.append(df.Preferred[j])
        categoryGenres.append(subArr)

    categoryGenreFreqs = []
    genreList = ["Nerd", "Animal", "Programming", "Politics", "School", "Other", "Sports", "Math", "Medicine/Doctor"]
    for i in range(len(categories)):
        subArr = []
        for j in range(len(genreList)):
            subArr.append(categoryGenres[i].count(genreList[j]))
        categoryGenreFreqs.append(subArr)
            
    fig, ax = plt.subplots()
    index = np.arange(9)
    bar_width = 0.1    
    opacity = 0.9        

    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
    for i in range(len(categories)):
        rects = plt.bar(index + bar_width*i, categoryGenreFreqs[i], bar_width,
                 alpha=opacity,
                 color=colors[i],
                 label=str(categories[i]))

    plt.xlabel('Preferred Joke Category')
    plt.ylabel('Joke Genre Popularity')
    plt.title('Joke Genre Popularity By Preferred Joke Category')    
    plt.xticks(index + bar_width, genreList)
    plt.legend()
 
    plt.tight_layout()
    plt.show()

#plotCategoriesAndGenres()
