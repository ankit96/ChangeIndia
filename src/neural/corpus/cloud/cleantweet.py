import HTMLParser


import cPickle


def strip_non_ascii(string):
    ''' Returns the string without non ASCII characters'''
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)


def clean(tweet):
	stopwords=cPickle.load(open('stopwords.p', 'rb'))
	redundant=[':',",",")",".","(",";","/","|","-",'?','=','+',"...","!","\""]
	html_parser=HTMLParser.HTMLParser()
	tweet=html_parser.unescape(tweet).lower()
	tweet = strip_non_ascii(tweet) 
	tweet=tweet.decode("utf8").encode("ascii","ignore")
	#tweet = " ".join(re.findall('[A-Z][^A-Z]*', tweet))
	words=tweet.split()
	tweet=""
	i=0
	for word in words:
		for a in redundant:
			if a in word:
				i=word.index(a)
				if i==0:
					word=word[1:]
				elif i==len(word)-1:
					word=word[:-1]
				else:
					left=word[:i-1]
					right=word[i+1:]
					word=left+right
		#word=correct(word)
		if "'" in word and word[-1]=='s':
			sp=word.split("'")
			word=sp[0]
		
		elif "'" in word or word in stopwords:
			continue
		tweet=tweet+word+" "
	tweet=tweet.strip()
	return tweet
