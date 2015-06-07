import media
import fresh_tomatoes

# Create instances of the Movie class to hold information of my favourite movies
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life.",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

seven_lucky_kids = media.Movie("7 Lucky Kids",
                               "Seven kids with superior martial arts skills stumble into excitement and adventure",
                               "http://ia.media-imdb.com/images/M/MV5BMTI5MTg1NTIzOV5BMl5BanBnXkFtZTYwNDg2Njg4._V1__SX640_SY720_.jpg",
                               "https://www.youtube.com/watch?v=MYXNpYexk1A")

matrix = media.Movie("Matrix",
                     "A movie about the reality of life itself.",
                     "http://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
                     "https://www.youtube.com/watch?v=m8e-FF8MsqU")

back_to_the_future = media.Movie("Back to the Future",
                                 "A young man is accidentally sent 30 years into the past in a time-traveling DeLorean.",
                                 "http://upload.wikimedia.org/wikipedia/en/d/d2/Back_to_the_Future.jpg",
                                 "https://www.youtube.com/watch?v=yosuvf7Unmg")

teza = media.Movie("Teza",
                   "The story of a young Ethiopian as he returns from West Germany a postgraduate.",
                   "http://www.discoverafricancinema.com/wp-content/uploads/2014/03/teza-film-poster.jpg",
                   "https://www.youtube.com/watch?v=3X24urlexuo")

footloose = media.Movie("Footloose",
                        "A story of an upbeat Chicago teen who moves to a small town.",
                        "http://upload.wikimedia.org/wikipedia/en/e/e4/FootloosePoster.jpg",
                        "https://www.youtube.com/watch?v=xxOuSqokKok")


above_the_rim = media.Movie("Above the Rim",
                            "A promising New York City high school basketball star and his relationships with two people.",
                            "http://upload.wikimedia.org/wikipedia/en/b/b6/Above_the_rim_poster.jpg",
                            "https://www.youtube.com/watch?v=sEsCXWD7-Cc")


space_jam = media.Movie("Space Jam",
                        "Fun Movie with Michael Jordan and Bugs Bunny",
                        "http://upload.wikimedia.org/wikipedia/en/1/14/Space_jam.jpg",
                        "https://www.youtube.com/watch?v=oKNy-MWjkcU")

indiana_jones = media.Movie("Indiana Jones",
                            "Indiana Jones against a group of Nazis who are searching for the Ark of the Covenant.",
                            "http://upload.wikimedia.org/wikipedia/en/4/4b/Raiders.jpg",
                            "https://www.youtube.com/watch?v=bbEtZ8LNMAA")

the_10_commandments = media.Movie("Moses",
                                  "The story of how God delivered Israel from 400 years slavery.",
                                  "http://upload.wikimedia.org/wikipedia/en/d/d1/10Command56.jpg",
                                  "https://www.youtube.com/watch?v=OqCTq3EeDcY")

# Add the instances to a list
movies = [
    toy_story,
    seven_lucky_kids,
    matrix,
    back_to_the_future,
    teza, footloose,
    above_the_rim,
    space_jam,
    indiana_jones,
    the_10_commandments
]

# Generate a web page that displays the movies in the list
fresh_tomatoes.open_movies_page(movies)