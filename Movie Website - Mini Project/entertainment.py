import media
import fresh_tomatoes

toy_story = media.Movie("Life of entrepreneur",
                        "See what he do throughout the day",
                        "http://3.bp.blogspot.com/-8m9pjSAwZxM/U3hrWorccEI/AAAAAAAAOxU/2p-u_eGSPJo/s1600/Life-of-Entrepreneur-infographic.jpg",
                        "https://www.youtube.com/watch?v=h-KHWUq3B7I")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://resizing.flixster.com/wmwaS9C76fnLpML3UAj0i3l6djw=/206x305/v1.bTsxMTE3Njc5MjtqOzE3NDU0OzEyMDA7ODAwOzEyMDA",
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

yjhd = media.Movie("YJHD",
                   "Yeh Jawani Hai Diwani",
                   "http://www.cinehindi.com/wp-content/uploads/2015/08/fsada.png",
                   "https://www.youtube.com/watch?v=PUpHeOBV1FU")

movies = [toy_story, avatar, yjhd]
fresh_tomatoes.open_movies_page(movies)

