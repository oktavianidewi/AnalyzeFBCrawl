# -*- coding: utf-8 -*-
# read spss file
import savReaderWriter
from pprint import pprint
import simplejson as json
import string

from scipy.io.idl import readsav

savFileName = "LYH Dataset/271_all_post_processed.sav"
# savFileName = "LYH Dataset/271_all_post_processed_coba.sav"
# savFileName = "LYH Dataset/sampleSharer1.sav"

date_posttime_arr = []
dict_date_posttime_arr = {}

posts = []
newposts = []
users = []


newlist = {}

all = {}

def writeToTextFile(data, textfile):
    text_file = open(textfile, "w")
    text_file.write(data)
    text_file.close()
    return True

def writeToJsonFile(data, jsonfile):
    with open(jsonfile, 'w') as file:
        file.write( json.dumps(data, ensure_ascii=False, encoding='latin1') )
        file.close()
    return True

reader = savReaderWriter.SavReader(savFileName)

with savReaderWriter.SavReader(savFileName) as username_reader:
    for i in username_reader:
        # memindahkan hasil baca file sav ke array posts
        # posts.append(i)
        # memindahkan hasil baca user file sav ke array users
        if i[2] not in users:
            users.append(i[2])

        k = []
        for idet in i :

            # k.append(idet.encode('ascii').strip())
            # if type(idet) != float and idet is not None :
            # posts.append(idet)


            if (type(idet) != float) and (idet is not None):
                if idet.isalpha():
                    # idet_bener = str(idet).strip()
                    idet_bener = str(idet).strip()

                else:
                    idet_bener = str(idet)
                    # print str(idet).encode('ascii', 'ignore').decode('ascii')
                    # print idet.encode('utf8', 'replace')
            elif (idet is None):
                idet_bener = 'null'
            else:
                idet_bener = float(idet)
            k.append( idet_bener )
        posts.append(k)
    # print len(posts)
    # print posts
    # quit()

    postId = ''
    usernewlist = {}
    for i in users:
        # print i
        postsPerUser = []
        for j in posts:
            if i == j[2]:
                # postId -> usernumber_postnumber
                postId = str(int(j[1]))+'_'+str(int(j[0]))
                # print 'bandingkan ', i, '==', j[2]
                # print i == j[2]
                postsPerUser.append([postId] + j[2:])
                newlist[i] = postsPerUser
    writeToJsonFile(newlist, '271_all_post_processed_wPostId.json')
    # print newlist