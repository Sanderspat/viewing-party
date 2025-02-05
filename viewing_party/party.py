def create_movie(movie_title, genre, rating):
    create_movie_dict = {'title': movie_title, 'genre': genre, 'rating': rating}

    if movie_title and genre and rating:
        movie_dict = {'title':movie_title, 'genre':genre, 'rating':rating}
        return movie_dict
    else:
        return None


def add_to_watched(user_data, movie_title):
    watched_list = user_data['watched']
    watched_list.append(movie_title)
    return user_data


def add_to_watchlist(user_data, movie_title):
    add_watchlist = user_data['watchlist']
    add_watchlist.append(movie_title)
    return user_data


def watch_movie(user_data, movie_title):
    movies_watched = user_data['watched']
    movies_to_watch = user_data['watchlist']

    for movie in movies_to_watch:
        if movie_title == movie['title']:
            movies_watched.append(movie)
            movies_to_watch.remove(movie)
             
    return user_data 

### Wave 2

def get_watched_avg_rating(user_data):
    avg_rating = 0.0
    rating_sum = 0
    if user_data["watched"] == 0:
        return 0 
    else: 
        for movie in range(len(user_data['watched'])):
            rating_sum += user_data['watched'][]['rating']
    rating_sum/len(user_data['watched'])

    return avg_rating 


def get_most_watched_genre(user_data):
    most_recurring_genre = {}
    genre_count = 0
    max_genre = None

    if len(user_data["watched"])== 0:
        return None 
    for movie_dict in user_data["watched"]:
        if movie_dict["genre"] in most_recurring_genre:
            most_recurring_genre[movie_dict["genre"]] += 1
        else:
            most_recurring_genre[movie_dict["genre"]] = 1
    # max_genre = max(most_recurring_genre)
    
    for genre in most_recurring_genre.items():
        if most_recurring_genre[1] > genre_count:
            genre_count = most_recurring_genre[1]
            max_genre = most_recurring_genre[0]

    return max_genre

def get_unique_watched(user_data):
    friends_list =[]
    user_only_watched = []

    for watched_list in user_data["friends"]:
        for movie in watched_list["watched"]:
            friends_list.append(movie["title"])

    for movie in user_data["watched"]:
        if movie["title"] not in friends_list:
            user_only_watched.append(movie)
    
    return user_only_watched 

def get_friends_unique_watched(user_data):   
    movies_friends_watched = []

    for watched_list in user_data["friends"]:
        for movie in watched_list["watched"]:
            if movie not in user_data["watched"] and movie not in movies_friends_watched:
                movies_friends_watched.append(movie)
    return movies_friends_watched

def get_available_recs(user_data):
    host = user_data["subscriptions"] 
    friends_watched_list = []
    user_title = []
    rec_list = [] 
    
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_watched_list .append(movie)
    
    for user_movie in user_data["watched"]:
        user_title.append(user_movie["title"])
    
    for movie in friends_watched_list:
        if movie["title"] not in user_title:

            if movie["host"] in host:
               if movie not in rec_list:
                    rec_list.append(movie)

    return rec_list

def get_new_rec_by_genre(user_data):
    recommended_genre = []
    new_list = []
    fave_genre = get_most_watched_genre(user_data)

    for movie in user_data["friends"]:
        for i in movie["watched"]:
            new_list.append(i)
    for movie in new_list:
        if movie["genre"] == fave_genre:
            recommended_genre.append(movie)
    return recommended_genre

def get_rec_from_favorites(user_data):
    recs_from_faves = []
    unique_watched_list = get_unique_watched(user_data)
    faves = user_data["favorites"]

    for movie in unique_watched_list: 
        if movie in faves:
            recs_from_faves.append(movie)
    return recs_from_faves




    


    
       













