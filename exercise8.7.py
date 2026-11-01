def make_album(artist, title, songs=None):
    album = {
        "artist": artist,
        "title": title
    }
    if songs is not None:
        album["songs"] = songs
    return album

album1 = make_album("bruno mars", "doo wops & hooligans")
album2 = make_album("olivia rodrigo", "sour")
album3 = make_album("ed sheeran", "divide")
album4 = make_album("one direction", "made in the a.m.", 12)

print(album1)
print(album2)
print(album3)
print(album4)