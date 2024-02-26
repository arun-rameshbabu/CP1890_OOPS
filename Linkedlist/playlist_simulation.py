from dataclasses import dataclass

with open('song_list.txt') as file:
    playlist = file.read().splitlines(', ')
@dataclass
class Song:
    title:object
    nextSong = None

    def __repr__(self):
        return f'Song: {self.title}'


@dataclass
class Playlist:

    currentSong=None
    songList = []
    def __repr__(self):
        return f'Current song: {self.songList[0].data} Next song: {self.songList[1].data}'

    def loadPlayList(self):
        current_song = self.currentSong
        while current_song is not None:
            next_song = Song(playlist.pop())
            self.songList.append(next_song)
            current_song = current_song.nextSong
        self.songList.append('Loading playlist')
    def nextSong(self):
        if len(self.songList) == 0:
            print('No songs')
        else:
            currentSong.next =.pop(0)




