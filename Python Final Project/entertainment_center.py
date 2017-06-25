import media
import fresh_tomatoes

#creating the list of movie object by calling the constructor to instantiate movie objects
tubelight = media.Movie("Tubelight",
             "https://upload.wikimedia.org/wikipedia/en/0/04/Tubelight_Poster.jpg",
             "https://www.youtube.com/watch?v=PGQRNKHJwH4&vl=en")
bahubali = media.Movie("Bahubali-2",
            "https://i1.wp.com/www.mazale.in/wp-content/uploads/2017/04/baahubali-2-2.jpg",
            "https://www.youtube.com/watch?v=qD-6d8Wo3do")
raees = media.Movie("Raees",
         "http://www.bollywoodlife.com/wp-content/uploads/2016/08/16-Raees-srk-poster.jpg",
         "https://www.youtube.com/watch?v=J7_1MU3gDk0")
phillauri = media.Movie("Phillauri",
             "http://static.koimoi.com/wp-content/new-galleries/2017/02/phillauri-movie-1.jpg",
             "https://www.youtube.com/watch?v=uCTr7MGFK0U")
ADHM = media.Movie("Ae Dil Hai Mushkil",
        "http://www.filmyfolks.com/movie/images/ae-dil-hai-mushkil-movie-3.jpg",
        "https://www.youtube.com/watch?gl=IN&hl=sk&v=Z_PODraXg4E&itct=CAoQpDAYBSITCOL204TwwM8CFQ1fTgodQswIazIHcmVsYXRlZEjvjOH0zrev0Hc%3D&client=mv-google-%27N")
YJHD = media.Movie("Yeh Jawani Hai Diwani",
        "http://www.cinehindi.com/wp-content/uploads/2015/08/fsada.png",
        "https://www.youtube.com/watch?v=Rbp2XUSeUNE")
rockstar = media.Movie("Rockstar",
            "http://www.watch-bollywood-movies.com/wp-content/uploads/2011/12/Rockstar-2011-download-mp3-songs.jpg",
            "https://www.youtube.com/watch?v=rHsesDDDaa4")
barfi = media.Movie("Barfi",
         "https://upload.wikimedia.org/wikipedia/en/2/2e/Barfi%21_poster.jpg",
         "https://www.youtube.com/watch?v=Y5MRdAhLTbc")
tamasha = media.Movie("Tamasha",
           "https://cdn.pinkvilla.com/files/styles/contentpreview/public/CPPUFYYUYAA9Snp.jpg?itok=knLTFxRR",
           "https://www.youtube.com/watch?v=o-e5eWVCzx8")

#storing the list of movie objects in variable
movies = [tubelight, bahubali, raees, phillauri, ADHM, YJHD, rockstar, barfi, tamasha]

#passing the list of movies to generate the webpage
fresh_tomatoes.open_movies_page(movies)
