# -*- coding: utf-8 -*-
import csv
import sys

DEFAULT_DAT = "th_th_TH_v2.dat"

def usage():
	print("Usage: {} <csv-data-file> [<out-dat-file>]"
	        .format(sys.argv[0]))
	print("If omitted, <out-dat-file> defaults to {}."
	        .format(DEFAULT_DAT))

if len(sys.argv) not in [2, 3]:
	usage()
	sys.exit()
data_csv = sys.argv[1]
out_dat = DEFAULT_DAT
if len(sys.argv) == 3:
	out_dat = sys.argv[2]

dat = {}
with open(data_csv, "r", encoding="utf-8-sig") as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	next(csv_reader, None)
	for row in csv_reader:
		word, pos, syn = row
		if word not in dat:
			dat[word] = []
		dat[word].append({"pos" : pos, "syn" : syn.split('|')})

THES_POS = {
	"n" :   "น.",
	"v" :   "ก.",
	"adj" : "ว.",
	"adv" : "ว.",
}

with open(out_dat, "w", encoding="utf-8") as out:
	out.write("UTF-8\n")
	for word in dat:
		out.write("{}|{}\n".format(word, len(dat[word])))
		for sense in dat[word]:
			out.write("{}|{}\n".format(THES_POS[sense["pos"]],
			                             "|".join(sense["syn"])))
