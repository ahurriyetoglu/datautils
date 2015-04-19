import pandas as pd

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

		
	

if __name__ == "__main__":
	pass
