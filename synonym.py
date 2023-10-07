# -*- coding: utf-8 -*-
import csv
data={}
temp=[]
i=0
with open('data.csv','r',encoding="utf-8-sig") as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	next(csv_reader, None)
	for row in csv_reader:
		for d in [i for i in row[-1].split("|") if i!=""]:
			for t in [i for i in row[-1].split("|") if i!="" and i!=d]:
				key={}
				key['word']=d
				key['synonym']=t
				temp.append(key)
			key={}
			key['word']=d
			key['synonym']=row[0]
			temp.append(key)
			key={}
			key['word']=row[0]
			key['synonym']=d
			temp.append(key)
data["data"]=temp
def search(word):
	return [a['synonym'] for a in data['data'] if a['word']==word]

if __name__ == "__main__":
	while True:
		text=input("Text : ")
		text_list=search(text)
		get = []
		get.append(text_list)
		if get!=[]:
			print("synonym : "+'|'.join(get))
		else:
			print("not found")
