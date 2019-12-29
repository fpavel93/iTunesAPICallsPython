import requests

from model.ResponseObject import ResponseObject


class APICallMethods:

    def __init__(self):
        # Holds the API URL
        self.apiUrl = "https://itunes.apple.com/search?"

    # Search 
    def search(self, search_text):
        search_text.replace(" ", "+")
        query1 = "term=" + search_text
        return self.searchQuery(query1)

    # Search with more than 1 key 
    def searchMultipleKey(self, search_text, country, media):
        search_text.replace(" ", "+")
        query1 = "term=" + search_text
        if country is not None:
            query1 = query1 + "&country=" + country
        if media is not None:
            query1 = query1 + "&media=" + media
        return self.searchQuery(query1)

    # Get Albums 1 and more 
    def getAlbums(self, search_text):
        search_text.replace(" ", "+")
        query1 = "term=" + search_text + "&entity=album&attribute=albumTerm"
        return self.searchQuery(query1)

    # Get Artist 1 and more
    def getArtists(self, search_text):
        search_text.replace(" ", "+")
        query1 = "term=" + search_text + "&entity=musicArtist&attribute=artistTerm"
        return self.searchQuery(query1)

    def searchQuery(self, query1):
        URL = self.apiUrl + query1
        r = requests.get(URL)
        results = None
        if r.status_code == 200:
            responseObject = ResponseObject.from_json(r.content)
            results = responseObject.results
        else:
            print("ERROR: Connection refused")
        return results