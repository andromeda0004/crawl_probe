import requests #for the actual get requests which pull the content out of a given page.
from bs4 import BeautifulSoup #used to pull data out of html documents and present it in a way such that navigating the site is easier 
from urllib.parse import urljoin #for creating absolute links for the spider to naviagte easily
import time #to use for delays and re-connections

visited_nodes = set() #so that duplicates are eliminated while the recursive function keeps running
matches_count = 0
matched_urls = []

def spider(url,keyword,depth): #increases every iteration by 1, so that the depth is maintained and the function can backtrack when it reaches the depth limit.
	
	global matches_count #important to make sure that the scope of matches_count is global for it to be used anywhere for increments.

	if matches_count >= depth:
		return
	
	# this block is in case an http error is encountered
	try:
		res = requests.get(url, timeout=5) #if greater than 5 assume failure and give up, go to exception
	except requests.exceptions.RequestException as e:
		print(f"Network/Request error for {url}: {e}")
		print("Retrying in 5 seconds...\n")
		time.sleep(10)  #wait for 10 seconds to retry
		return

	# if the connection is successful, i.e, 200 http status code, the actual process begins.
	if res.status_code == 200:
		soup = BeautifulSoup(res.content, 'html.parser') #this is an important class used to pull data of the webpage, syntax is BeautifulSoup(site, typeofparser)
		
		a_href = soup.find_all("a") #to find all the links in the pulled site page where anchor tags were used. this is stored in a variable called a_href

		urls = [] #empty list where the urls from the for loop below will be stored one by one in order for it to be used to fill the visited_nodes set.

		#this for loop will be used to point out the href part of the link. for example if a href="\contact.html", only the \contact.html part will be stored in the urls list.
		for i in a_href:
			href = i.get("href") #fetches the value of every href in every iteration. this href value will now be appended to urls list.
			if href is not None and href != "": #href shouldnt be empty and the value itself shouldnt be equal to any empty/dummy value with no name for it.
				urls.append(href)

		#core recursive search logic and also unique link logic.
		for i in urls:
			if matches_count>=depth:
				return #for each time when the spider goes through recursion. to avoid extra prints.
			url_join = urljoin(url,i) #creates an absolute link for the given href link from the urls list. joins the both arguments.
			if url_join not in visited_nodes: #for unique links 
				visited_nodes.add(url_join) #for better and robust link generation which is absolute
				print("Visiting: ", url_join) #all urls being visited
				if keyword.lower() in url_join.lower():
					print("Matched: ", url_join)  #only matching keyword urls being shown separately
					matched_urls.append(url_join)	
					matches_count=matches_count+ 1
					if matches_count>=depth:
						print("Limit reached. Stopping the crawl") #for internal loop where it is depth first
						return
				spider(url_join,keyword,depth) #recursively running function which goes depth first before backtracking to perform further operations.
	
user_url=input("enter a site: \n")
user_keyword=input("enter relevant keyword: ")
search_depth = int(input("enter search depth (no of matches to be listed): "))
spider(user_url,user_keyword,search_depth)

user_prompt = input("Would you like a copy of the URL files? y/n: \n")
if user_prompt == 'y':
	with open("url.txt", "w") as f:

		for items in matched_urls:
				f.write("%s\n" %items)
		print("file written successfully.")

	f.close()
else:
	pass

#sample site to scrape => https://books.toscrape.com/index.html
#sample keyword => catalogue