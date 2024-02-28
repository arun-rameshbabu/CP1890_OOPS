from dataclasses import dataclass

with open('song_list.txt') as file:
    playlist = file.read().splitlines(', ')
@dataclass
class Song:
    title:object
    nextSong = None

    def __repr__(self):
        return f'Song: {self.title}'






