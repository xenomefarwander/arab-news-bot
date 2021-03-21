# arab-news-bot

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

Note: If you don't already have Beautiful Soup 4, visit the following website for instructions on how to download and set up on your system: https://www.crummy.com/software/BeautifulSoup/bs4/doc/

FAQ

Q: How do I input the links that I want to search?
A: There are two ways:
    1) Simply open the file "arab_news_urls.txt" and insert and/or replace the links that you want the program to search through. Make sure
    to put one link per line.
 
    2)If you have another filename that you wish to use, you can change the code to look for your file instead of the default "arab_news_urls.txt" 
   
       filename_urls = "arab_news_urls.txt"  

    Change the name of the .txt input file to the name of the file that contains your links. The file containing your links should be in the same
    directory as the program itself.
   
Q: How do I change the terms that I want to search?
A: Same as above, but instead of "arab_news_urls.txt", you'll want to use "arab_news_search_terms.txt". In the program, this is designated as 
    filename_urls = "arab_news_urls.txt"
    
For any questions or comments, feel free to drop me a message on Twitter @brandon_roddey https://twitter.com/brandon_roddey. I'm still learning, so any feedback or advice is much appreciated!
