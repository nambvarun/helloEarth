# helloEarth
An iOS app for reading news while browsing through articles on the globe

We have created a news app centered on focusing on displaying global news on a global stage. An interactive globe model, allows user to navigate around the world and look at news articles to various levels of depth. On the backend, we have created a scraper the scours the internet for articles to populate the globe. This content is updated every few minutes, and the ios app is pulling for this data over the web.

The app, this was written in Objective-C with the focus of taking in .json data from a the news scraper. The python script for the news scraper is running on a server, and constantly keeping the data up to date.

Credits: WhirlyGlobe - The map api that we used for the UI in this app. It is open source, and was a perfect fit for this project with the flexibility of maps and UI interaction features. http://mousebird.github.io/WhirlyGlobe/

Beautiful Soup - The HTML parser that we used in our python. It is an open source project that can be found here: http://www.crummy.com/software/BeautifulSoup/
