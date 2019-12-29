from APICallMethods import APICallMethods

api = APICallMethods()
print("Welcome to ITunes search API")

num = 1
while int(num) != 0:
    print("\nPlease choose what kind of search do tou want:")
    print("1. Regular search")
    print("2. Search with more than 1 key")
    print("3. Search Albums 1 and more")
    print("4. Search Artist 1 and more")
    print("0. For exit.")

    num = input()

    if int(num) == 1:
        text = input("\nEnter text for search: ")
        result = api.search(text)
        if result is not None:
            for (item) in result:
                print(item)
        else:
            print("No results")
        try:
            text = input("\nPress Enter to continiue")
        except:
            text = None
    elif int(num) == 2:
        text = input("\nEnter text for search: ")
        try:
            country = input("Enter country code for for search (optional): ")
        except:
            country = None
        try:
            media = input("Enter media type for for search (optional): \nMedia type could be: movie, podcast, music, "
                      "musicVideo, audiobook, shortFilm, tvShow, software, ebook or all")
        except:
            media = None
        result = api.searchMultipleKey(text, country, media)
        if result is not None:
            for item in result:
                print(item)
        else:
            print("No results")
        try:
            text = input("\nPress Enter to continiue")
        except:
            text = None
    elif int(num) == 3:
        text = input("\nEnter text for search Albums: ")
        result = api.getAlbums(text)
        if result is not None:
            for item in result:
                print(item)
        else:
            print("No results")
        try:
            text = input("\nPress Enter to continiue")
        except:
            text = None
    elif int(num) == 4:
        text = input("\nEnter text for search Artists: ")
        result = api.getArtists(text)
        if result is not None:
            for item in result:
                print(item)
        else:
            print("No results")
        try:
            text = input("\nPress Enter to continiue")
        except:
            text = None