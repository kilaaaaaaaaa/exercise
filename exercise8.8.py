def make_album(artist, title):
    return {
        "artist": artist,
        "title": title
    }

while True:
    print("enter album information (enter 'quit' to quit):")
    artist = input("artist name: ")
    if artist == "quit":
        break
    title = input("album title: ")
    if title == "quit":
        break
    album = make_album(artist, title)
    print(album)