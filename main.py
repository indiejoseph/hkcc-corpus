# -*- coding: utf-8 -*-

import urllib2
import re
import os
import sys
from bs4 import BeautifulSoup as Soup
import codecs

def main():

  if "SESS_ID" not in os.environ:
    print "No SESS_ID..."
    sys.exit(1)

  SESS_ID = os.environ["SESS_ID"]
  url_template = "http://corpus.ied.edu.hk/hkcc/corpus/sentence.php?sentid=%s&wordid="
  sent_range = (14648, 29294) # first movie transcript is beginning 14648
  header = "Id, Artist, Type, Text\n"
  current_movie_id = 0
  movie_file = None

  for sentid in xrange(*sent_range):
    url = url_template % sentid

    try:
      opener = urllib2.build_opener()
      opener.addheaders.append(("Cookie", "PHPSESSID={0}".format(SESS_ID)))
      data = opener.open(url)
    except urllib2.URLError as e:
      # Retry
      print ('Connection perhaps lost !! Trying one more time...')
      try:
        data = opener.open(url)
      except:
        print ('Connection really lost !! Bailing out..')
        print (e) # print outs the exception message

    # Moive info
    soup = Soup(data, "lxml")
    movie = soup(attrs={"href": re.compile(r"^movie\.php")})[0]
    movie_title = movie.text.strip()
    movie_id = int(re.search('movieid=([0-9]+)', movie["href"]).group(1))
    sent_indexes = soup.select(".link")[1].text.split("/")
    sent_index = int(sent_indexes[0].strip())
    sent_total = int(sent_indexes[1].strip())
    artist = soup(attrs={"href": re.compile(r"actor\.php\?actorid=")})[0].text
    sent_type = 0 if soup.select('table .oddrow')[1].text.rstrip() == u"說" else 1
    text = soup.select('table .oddrow')[2].text.strip()
    line = u"{0}, {1}, {2}, {3}\n".format(sent_index, artist, sent_type, text)

    # Debug
    # params = (movie_title.split(u" (")[0], movie_id, sent_index, sent_total, artist.split(" (")[0], sent_type, u"".join(text.split(" ")))
    # print url
    # print u"{0}, {1}, {2}, {3}, {4}, {5}, {6}".format(*params)

    if current_movie_id != movie_id:
      print u"Movie({1}): {0}".format(movie_title, movie_id)

      if movie_file != None:
        movie_file.close()

      # create movie file
      movie_file = codecs.open("./corpus/movie_%d.csv" % movie_id, "w", "utf-8")
      movie_file.truncate()
      movie_file.write(header)
      current_movie_id = movie_id

    print u"Sent: {0} / {1}".format(sent_index, sent_total)
    movie_file.write(line)

if __name__ == "__main__":
  main()
