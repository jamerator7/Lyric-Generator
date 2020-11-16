# My project will ask the user for a song and then give them the lyrics to the song.
import lyricsgenius


def main():
    list = ["none", 0, "n"]
    artist1 = str(input("Who is your favorite musical artist? "))
    list[0] = artist1
    list[2] = input("Do you want to know some of their songs? (y/n) ")
    genius = lyricsgenius.Genius("0wYb-xsVfpkx1CtxOyk_-FfAMqAiIXhYLHg8blCZ3qvmrpJgOwV1ycvQSgM_1Kb4")
    if list[2] == "y":
        print("How many", list[0], "songs do you wanna know?")
        list[1] = int(input(""))
    try:
        artist = genius.search_artist(list[0], max_songs=list[1], sort="popularity")
    except AttributeError:
        return print("ERROR No Artist Found")
    while True:
        print(" ")
        print("What", artist1, "song do you want to know the lyrics to? ")
        title = str(input(""))
        try:
            song = genius.search_song(title, artist.name)
            print(" ")
            print(song.lyrics)
        except AttributeError:
            print("No song found")
        print(" ")
        print(" ")
        print("Done. Do you want to know a new artist or know more", artist1, "(y/n)")
        decide = input("")
        if decide == "y":
            print(" ")
            main()
        elif decide == "n":
            print(" ")
        else:
            print("Unknown command. Artist will remain.")


if __name__ == '__main__':
    main()
