import pandas as pd
from collections import Counter
import json
from datetime import datetime
from html.parser import HTMLParser
import sys

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.strict = False
        self.convert_charrefs= True
        self.fed = []
        
    def handle_data(self, d):
        self.fed.append(d)

    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

def getlinelist(filename, striplines=True):
	with open(filename) as f:
		linelist = f.read().splitlines()
    
	if striplines:
		linelist = [l.strip() for l in linelist]
        
	return [l for l in linelist if len(l)>0] # Exclude blank lines!
    

def writelinelist(filename, mylist):
	with open(filename, 'w') as fw:
		for l in mylist[:-1]: # Write lines with new line, except the last line.
			fw.write(str(l)+'\n')
		fw.write(str(mylist[-1])) # Do not put new line for the last line!


def appendlineslist(appendFile, lines):
	with open(appendFile, "a") as myfile:
		if isinstance(lines,str):
			myfile.write(lines+"\n")
		elif isinstance(lines, list):
			for l in lines: # Write lines with new line, except the last line.
            			myfile.write(str(l)+'\n')
			#myfile.write(str(lines[-1])) # Put a new line for the last line!
		else:
			raise Exception("A problem occurred in appending to the file:",appendFile,"\nType of the input:",type(lines))

def read_twiqs_csv(twiqs_csv, how="basic"):
	"""
           This reads csv files that are downloaded from Twiqs.nl into a pandas.DataFrame
        """
	if how=='basic':
		return pd.read_table(twiqs_csv, parse_dates=[[0,1]], usecols=[2,3,6,7], encoding='utf-8',\
                               names=['dt','etime', 'user', 'ttext'], skiprows=1, quoting=3)
	elif how=='all':
		temp_df = pd.read_table(twiqs_csv, parse_dates=[[2,3]], usecols=[0,1,2,3,4,5,6,7], encoding='utf-8', quoting=3)
		temp_df.columns = [c.replace('#','') for c in temp_df.columns]
		return temp_df
	else:
		raise Exception("there is a problem in the --how-- parameter. Current value:",how)

		
def read_json_tweets_file(myjsontweetfile, reqlang='en', numLines=-1):
    ftwits = []
    lang_cntr = Counter()
    print("processed file:",myjsontweetfile)
    print("Language of the processed tweets:",reqlang)

    with open(myjsontweetfile) as jfile:
        for i, ln in enumerate(jfile):
            if i == numLines: # it will first <numLines> lines.
            	break
            
            try:
            	t = json.loads(ln)
            except:
            	print("Error in the line number:",i,"the line is:",t)
            	print("Unexpected error:", sys.exc_info()[0])
            	continue
            	#raise
            
            lang_cntr[t["lang"]] += 1
            
            if t["lang"] == reqlang:
                t["created_at"] = datetime.strptime(t["created_at"],"%a %b %d %H:%M:%S +0000 %Y")

                #if t["created_at"].strftime("%Y-%m-%d") in flood_AnomBreakoutDaysList:
                if "entities" in t:
                    if "media" in t["entities"]:
                        for tm in t["entities"]["media"]:
                            if tm["type"] == 'photo':
                                t["entity_type"] = 'photo'
                                break
                    # if it is empty, this field may not be present.
                    if "hashtags" in t["entities"]:
                        t["entity_hashtags"] = [ehs["text"] for ehs in t["entities"]["hashtags"]]
                	
                    if "user_mentions" in t["entities"]:
                        t["entity_mentions"] = [ems["screen_name"] for ems in t["entities"]["user_mentions"]]
                
                    if "urls" in t["entities"]:
                        t["entity_urls"] = [ers["display_url"] for ers in t["entities"]["urls"]]
                
                try:
                    if "place" in t:
                        t["country"] = t["place"]["country"]
                except:
                    pass
                    

                if "retweeted_status" in t:
                    t["is_retweet"] = True
                else:
                    t["is_retweet"] = False

                if "source" in t:
                    t["device"] = strip_tags(t["source"])

                t["user_id"] = t["user"]["id_str"]
                
                if "followers_count" in t["user"]:
                    t["user_followers"] = t["user"]["followers_count"]
                
                if "friends_count" in t["user"]:
                    t["user_following"] = t["user"]["friends_count"]

                t2 = {k:v for k,v in t.items() if k in ["entity_type","entity_hashtags","entity_mentions","entity_urls",\
                                                        "country","created_at","text","in_reply_to_user_id","id_str","user_id",\
                                                        "user_followers","user_following", "coordinates", "is_retweet","device"]}
                #print(i, end=',')
                ftwits.append(t2)#.splitlines()
        print(lang_cntr)
        return ftwits	

if __name__ == "__main__":
	pass
