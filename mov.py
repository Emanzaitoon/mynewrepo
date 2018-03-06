import webbrowser
class Movie():
    """this class is using for show movies in web sit"""
    def __init__(self,movie_title,movie_storyline,poster_image,trailer_youtube):
        self.title=movie_title
        self.storyline=movie_storyline
        self.poster_image_url=poster_image
        self.trailer_youtube_url=trailer_youtube
    def show(self):
        webbrowser.open(self.trailer_youtube_url)
    def imageshow(self):
        webbrowser.open(self.poster_image_url)

toy_story=Movie("bakena khaifeen","afraid","https://www.google.com.eg/imgres?imgurl=https%3A%2F%2Fi.ytimg.com%2Fvi%2F36Fkzc2mXXQ%2Fhqdefault.jpg&imgrefurl=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3D36Fkzc2mXXQ&docid=SRLpp-CqQucD-M&tbnid=0kp09jm6qXM3dM%3A&vet=10ahUKEwjJsp3-68PZAhVSDewKHeslBNMQMwgwKAEwAQ..i&w=480&h=360&bih=662&biw=1366&q=%D8%A8%D9%82%D9%8A%D9%86%D8%A7%20%D8%AE%D8%A7%D9%8A%D9%81%D9%8A%D9%86&ved=0ahUKEwjJsp3-68PZAhVSDewKHeslBNMQMwgwKAEwAQ&iact=mrc&uact=8","https://www.youtube.com/watch?v=w4x2_4Pa1nA&list=RDMMw4x2_4Pa1nA")
print(toy_story.storyline)
toy_story.show()
toy_story.imageshow()

