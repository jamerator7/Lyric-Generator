# My project will ask the user for a song and then give them the lyrics to the song.
import lyricsgenius
genius = lyricsgenius.Genius("0wYb-xsVfpkx1CtxOyk_-FfAMqAiIXhYLHg8blCZ3qvmrpJgOwV1ycvQSgM_1Kb4")


def lyrics(artist, artist1):
    print(" ")
    print("What", artist1, "song do you want to know the lyrics to? ")
    title = str(input(""))
    try:
        song = genius.search_song(title, artist.name)
        print(" ")
        print(song.lyrics)
        print(" ")
    except AttributeError:
        return print("No song found")
    loop(artist, artist1)


def loop(artist, artist1):
    print("Done. Do you want a new artist (y) or know more", artist1, "(n)?")
    decide = input("")
    if decide == "y":
        print(" ")
        main()
    else:
        print(" ")
        lyrics(artist, artist1)


def main():
    song_finder = ["Artist Name", "Song Finder Amount", "Song Finder Confirmation"]
    song_finder[1] = 0
    artist1 = str(input("Who is your favorite musical artist? "))
    song_finder[0] = artist1
    song_finder[2] = input("Do you want to know some of their songs? (y/n) ")
    if song_finder[2] == "y":
        print("How many", song_finder[0], "songs do you wanna know?")
        song_finder[1] = int(input(""))
    try:
        artist = genius.search_artist(song_finder[0], max_songs=song_finder[1], sort="popularity")
        lyrics(artist, artist1)
    except AttributeError:
        print("ERROR No Artist Found")
        main()


if __name__ == '__main__':
    main()
