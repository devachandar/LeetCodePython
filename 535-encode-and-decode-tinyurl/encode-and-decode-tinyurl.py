class Codec:

    def __init__(self):
        self.url = ""
        # self.counter = 0

    def encode(self, longUrl: str) -> str:
        # self.counter += 1
        # short_key = str(self.counter)
        self.url = longUrl
        return "http://tinyurl.com/1"

    def decode(self, shortUrl: str) -> str:
        short_key = shortUrl.split("/")[-1]
        return self.url
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))