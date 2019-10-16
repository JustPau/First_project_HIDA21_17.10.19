import csv
import re
from nltk.util import ngrams
import os


with open('Paulines-Kinadata_for_python.csv') as file:
    reader = csv.reader(file)
    gay_kina_list = list(reader)
    #print(gay_kina_list)

s = gay_kina_list
s = str(s)
s = s.lower()
s = re.sub(r'[^a-zA-Z0-9\s]', ' ', s)
tokens = [token for token in s.split(" ") if token != ""]
output = list(ngrams(tokens, 3))
data_list = output
print(data_list)

with open('data.csv', 'w', newline='') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerows(data_list)

myfile.close()






