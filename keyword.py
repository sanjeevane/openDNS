import rake;
import operator;
import os;
import re;
import time;

rake = rake.Rake("SmartStoplist.txt")
writeDir = "keyWords"
for filename in os.listdir("crawlDump"):
	with open('crawlDump/' + filename, 'r') as f:
		text = f.read();
		urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)		
	keywords = rake.run(str(text[1:]))
	with open('keyWords/file_' + str(time.time()) , 'wb') as writeFile:
		if len(keywords) < 5:
			writeFile.write("%s \n" %(urls[0]));
			writeFile.write("%s" %(keywords[:][0][0]));
			
		else:
			writeFile.write("%s \n" %(urls[0]));
			writeFile.write("%s" %(keywords[:5][0][0]));
			
