class Article():

	def __init__(self, title):
		self.title = title
		self.location = ""
		self.geocode = (0, 0)
		self.url = ""
		self.snippet = ""

	def getJSONData(self):
		return {'title' : self.title, 'location' : self.location, 'coordinates' : self.geocode, 'snippet' : self.snippet, 'url' : self.url}