import json
import collections
from datetime import datetime
import numpy as np
from post_identification_func import other, dailyActivitiesPost, sharedFeeling, uploadedPhoto, uploadedVideo, sharedNews

directory = 'D:/githubrepository/FBCrawl/extracted/'
# presentFile = '271_user.json'
presentFile = '271_all_post_processed.json'

avgPostPerMonth_arr = []

countSharedFeeling_arr = []
countUploadedPhoto_arr = []
countUploadedVideo_arr = []
countDailyAct_arr = []

postTitle = []

countDailyAct = 0
countSharedFeeling = 0
countUploadedPhoto = 0
countUploadedVideo = 0

# with open(directory+'/'+presentFile) as data_file:
with open(presentFile) as data_file:
    json_data = json.load(data_file)
    # json_data = data_file.readlines()
    for username in json_data:
        totalpost = len(json_data[username])
        # print "totalpost : ", totalpost

        for x in json_data[username]:
            if x[2] not in postTitle:
                postTitle.append(x[2])
    # print postTitle
    print "identifikasi daily activities "
    print 'username \t earliest_date \t latest_date \t dailyAct \t feeling \t uploaded photo \t uploaded video \t shared posts \t other posts\t total posts \t number of posts/month \t number of comments per post'

    for username in json_data:
        # print username
        score1 = 0
        score2 = 0
        score3 = 0
        score4 = 0
        score5 = 0
        score6 = 0
        countDailyAct_arr = []
        result = 0
        dateUpdated = []
        numOfComments = []
        wordlength = []
        for x in json_data[username]:
            # print "usertype ", x[65]
            # print x[2]
            # link sharing source x[25]
            # jumlah comment x[32]
            # print 'daily : ', dailyActivitiesPost(x[2]), 'feeling : ', sharedFeeling(x[2]), 'photo : ', uploadedPhoto(x[2]), 'video : ', uploadedVideo(x[2]), 'shared : ', sharedNews(x[2]), 'other : ', other(x[2])
            coba = other(x[2], x[25])
            # print 'hasil other : ', coba


            if other(x[2], x[25])[0] != 'no':
                hasil = other(x[2], x[25])
                if 'video' in hasil[0]:
                    score4 += hasil[1]
                else:
                    score5 += hasil[1]
            if dailyActivitiesPost(x[2]) > 0 :
                score1 += dailyActivitiesPost(x[2])
            if sharedFeeling(x[2]) > 0:
                score2 += sharedFeeling(x[2])
            if uploadedPhoto(x[2]) > 0:
                score3 += uploadedPhoto(x[2])
            if uploadedVideo(x[2]) > 0:
                score4 += uploadedVideo(x[2])
            if sharedNews(x[2]) > 0:
                score5 += sharedNews(x[2])
            if type(x[12]) is int:
                wordlength.append(x[12])
            # average per bulan
            monthyear = x[5].split(', ')[1].split(' ')[0]+" "+x[5].split(', ')[2].split(' at ')[0]

            d = datetime.strptime(monthyear, '%B %Y')
            day_string = d.strftime('%Y/%m')

            dateUpdated.append(day_string)
            numOfComments.append(x[32])

            groupByDate = collections.Counter(dateUpdated)

        # print 'tanggal awal', min(dateUpdated)
        # print 'tanggal akhir', max(dateUpdated)
        # print groupByDate

        avgWordLength = np.true_divide(sum(wordlength), len(wordlength))
        avgCommentsPerPost = np.true_divide(sum(numOfComments), len(json_data[username]))
        avgPostPerMonth = len(json_data[username])//len(groupByDate.keys())
        # print "tanggal update", dateUpdated

        latest_date = max(dateUpdated)
        earliest_date = min(dateUpdated)

        # print wordlength
        print username, '\t', earliest_date, '\t', latest_date , '\t', score1, '\t', score2, '\t', score3, '\t', score4, '\t', score5, '\t', score6, '\t', len(json_data[username]),'\t', avgPostPerMonth, '\t', avgCommentsPerPost, '\t', avgWordLength
        # print 'dailyAct ', score1, 'feeling', score2, 'uploaded photo', score3, 'uploaded video', score4, 'shared posts', score5, 'other posts', score6, 'total posts', len(json_data[username])