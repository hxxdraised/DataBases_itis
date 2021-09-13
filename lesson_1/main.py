from objects import *
from backup import *

artists, albums, musics, users, playlists = [], [], [], [], []
artists.append(Artist("ABBA", "*description*"))
musics.append(Music("Gimme! Gimme! Gimme!", 0, 4.52, "1979-01-01"))
albums.append(Album("Voulez-Vouz", 0, 0, "1979-01-01"))

artists.append(Artist("Boney M.", "desc"))
musics.append(Music("Daddy Cool", 1, 3.28, "1976-01-01"))
albums.append(Album("Take The Heat Off Me", 1, 1, "1976-01-01"))

users.append(User("Murat", "itiskfu", "qwerty123", [0, 1]))
playlists.append(Playlist("My retro playlist", "retro songs", users[0]))
playlists[0].add_music(musics[0])
playlists[0].add_music(musics[1])

write_backup_file("backup.json", artists, albums, musics, users, playlists)
