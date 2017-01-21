import webbrowser

class movie():
    # the following function used for intializing the objects attributes
    def __init__(self,movie_title,movie_storyline,poster_image,trailer):
        # setting value of title to value passed
        self.title=movie_title

        # setting value of storyline to value passed
        self.storyline=movie_storyline

        # setting value of poster_url to value passed
        self.poster_image_url=poster_image

        # setting value of url to value passed
        self.trailer_youtube_url=trailer

