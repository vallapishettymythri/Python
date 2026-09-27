from abc import ABC,abstractmethod
#Spotify
class spotify(ABC):
    @abstractmethod
    def play(self):
        pass
    def pause(self):
        pass
    def next(self):
        pass
class songs(spotify):
    def play(self):
        print("playing the yeshanagula")
    def pause(self):
        print("Paused the current song")
    def next(self):
        print("Playing the next song mallepoola pallaki")
class videos(spotify):
    def play(self):
        print("playing the video yeshanagula")
    def pause(self):
        print("paused the video")
    def next(self):
        print("playing the next video mallepula pallaki")
class podcast(spotify):
    def play(self):
        print("playing the podcast ")
    def pause(self):
        print("paused the podcast")
    def next(self):
        print("playing next podcast")


obj=songs()
obj.play()
obj=videos()
obj.next()
obj=podcast()
obj.pause()