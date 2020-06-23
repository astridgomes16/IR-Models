# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 01:02:35 2019

@author: Astrid
"""

import json
# if you are using python 3, you should 
import urllib.request
import urllib.parse
#import urllib2

# change the url according to your own corename and query
inurl = "http://18.223.117.41:8983/solr/DRF/select?q={}&fl=id%2Cscore&wt=json&indent=true&rows=20"
#inurl = "http://18.223.117.41:8983/solr/BM25/select?q=text_en%3A{}%20OR%20text_ru%3A{}%20OR%20text_de%3A{}&fl=id%2Cscore&wt=json&indent=true&rows=20"
#outfn = "C:/Users/Astrid/Documents/IR/project3/project3_data/DRF/Outputfiles/DFR.txt"

# change query id and IRModel name accordingly
qid = ''
IRModel='DFR'
#outf = open(outfn, 'w', encoding='utf-8')

# get all queries
with open('test_queries.txt', encoding='utf-8') as qfile:
    q1 = qfile.readline()
    #q="001 Russia's intervention in Syria"
    while q1:
        q1 = q1.strip().replace(" ", "*", 1)
        query_str = q1.split('*')
        qid = query_str[0]
        query = query_str[1]
        query = urllib.parse.quote(query)
        final_url = inurl.format(query)
        qid_print=qid.lstrip("0")
        outfn=qid_print+'.txt'
        outf = open(outfn, 'w', encoding='utf-8')
        # if you're using python 3, you should use
        try:
            data = urllib.request.urlopen(final_url)
        except:
            continue

        docs = json.load(data)['response']['docs']
        # the ranking should start from 1 and increase
        rank = 1
        for doc in docs:
            outf.write(qid + ' ' + 'Q0' + ' ' + str(doc['id']) + ' ' + str(rank) + ' ' + str(doc['score']) + ' ' + IRModel + '\n')
            rank += 1
        q1 = qfile.readline()

qfile.close()
outf.close()