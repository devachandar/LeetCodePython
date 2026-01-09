class Codec:

    def __init__(self):
        self.url_map = {}
        self.counter = 0

    def encode(self, longUrl: str) -> str:
        self.counter += 1
        short_key = str(self.counter)
        self.url_map[short_key] = longUrl
        return "http://tinyurl.com/" + short_key

    def decode(self, shortUrl: str) -> str:
        short_key = shortUrl.split("/")[-1]
        return self.url_map[short_key]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))