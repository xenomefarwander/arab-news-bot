########################ARAB NEWS BOT.PY#####################################
#This program acts as a search engine for easy monitoring of key words of interest on Arabic news sites, for example 
#"Joe Biden" or "America". The information contained in the links is sufficient for giving the user an overview
#of most recent publications on the key words from a large number of sites without have to manually visit each of those
#sites and look for the key words. 

#The program logic reads in a list of urls (designated under 'filename_urls') and a list of search terms ('filename_terms' variable). 
#It then searches through links on the designated pages and prints the matching link to screen whenever a result is found. For websites
#that use relative links, the program will reconstitute the entire url to make it easier just to copy and paste into the web browser or 
#pipe into some other process. 
#############################################################################

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import string
import re

# Open page request, pull all anchor tags using BeautifulSoup, and store as list in page_soup_links
def page_retrieve(url):
	print(f"\nSearching for links on {urllib.parse.unquote(url)}")
	page_request = urllib.request.Request(url, headers=headers)
	page_soup_links = []
	url = urllib.parse.unquote(url)
	with urllib.request.urlopen(page_request) as page:
		soup = BeautifulSoup(page, 'html.parser')
		for anchor in soup.find_all('a'):
			page_soup_links.append(anchor.get('href'))
	return page_soup_links

# Loop through search terms, feed in search term, search through search results, print if found
def search_term_in_links(search_terms, page_soup_links):
	count = 0
	print("\t\t**********************************************")
	for term in search_terms:
		for item in page_soup_links:
			item_str = str(item)
			item_str = urllib.parse.unquote(item_str) # code to remove percent encode from urls
			if re.search(term, item_str):
				item_str = check_http(item_str)
				print("\t\t"+urllib.parse.unquote(item_str))
				count += 1
	if count == 0:
		print(f"\t\tNo matches found!")
		print("\t\t**********************************************")
	else: print("\t\t**********************************************")
	return count

# Checks if starts with https:// and if not, formats 
def check_http(result_found):
	if result_found.startswith('http'):
		return result_found
	else: 
		pivot_word_suffix = url_suffix_builder(result_found)
		result_found = url_builder(url, pivot_word_suffix) 
		return result_found

# Parses the url_suffix passed from check_http and picks out the first word "pivot word"
def url_suffix_builder(url_suffix):
	# percent encode url
	url_suffix = urllib.parse.quote(url_suffix)
	# split each element of url at /
	parts = url_suffix.split("/")
	# join the elements minus the overlapping word
	pivot_word = parts[1]
	joined_suffix = "/" + "/".join(parts[1:])
	return pivot_word, joined_suffix

# Takes a url and a tuple composed of a pivot word (word shared by url and url suffix) and the url suffix
# Returns a URL that begins with soup url and appends the location of search result. 
# Result can be entered into browser and will load the article
def url_builder(url, pivot_word_suffix): 
	# split url into parts, find the pivot word, then merge suffix to url to pivot word index + 1
	parts = url.split("/") # gives a list with each word as entry
	# find the index position of the "pivot word" in the soup url
	pivot_word = pivot_word_suffix[0]
	url_suffix = pivot_word_suffix[1]
	i = 0
	match_index = int()
	found_pivot = False
	for part in parts:
		if part == pivot_word: 
			match_index = i
			found_pivot = True
		i += 1
	# merge parts[:match_index]
	if found_pivot == True:
		middle = "/".join(parts[1:match_index])
		return "https:/"+middle+url_suffix
	else:
		return "https://"+parts[2]+url_suffix


# Open file containing search terms, pull search terms from file and store into list
filename_terms = "arab_news_search_terms.txt"
search_terms = [] #initialize search term variable
with open(filename_terms) as f:
	for line in f:
		line = line.rstrip()
		search_terms.append(line)

# Open file containing urls, pull urls from file and store into list
filename_urls = "arab_news_urls.txt" #Change file name here to input a different list of links
urls = []
with open(filename_urls) as f:
	for line in f:
		line = line.rstrip()
		urls.append(line)

# Ignore SSL certificate errors
# ssl._create_default_https_context = ssl._create_unverified_context #bypasses unable to get local user certificate error
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


# Assign header
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:84.0) Gecko/20100101 Firefox/84.0'}

results_count = 0
for url in urls:
	page_soup_links = page_retrieve(url)
	results_count = search_term_in_links(search_terms, page_soup_links) + results_count

print(f"Total matches found: {results_count}")

	

