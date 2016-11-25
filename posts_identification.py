import simplejson as json
import collections

import numpy as np
import scipy.stats as stats
import pylab as pl

def normalDist(arraydata):
    h = sorted(arraydata)  #sorted
    print h
    fit = stats.norm.pdf(h, np.mean(h), np.std(h))  #this is a fitting indeed
    pl.plot(h, fit,'-o')
    pl.hist(h, facecolor="Yellow", alpha = 0.75, normed=True) #use this to draw histogram of your data
    pl.title(r'$\mathrm{Histogram\ of\ Average Posts/Month:}\ \mu=%s,\ \sigma=np.std(h)$')
    # pl.title(r'$\mathrm{Histogram\ of\ Average Posts/Month:}\ \mu='np.mean(h)',\ \sigma='+np.std(h)+'$')
    pl.xlabel("Average Posts/Month")
    pl.ylabel("Frequency")
    pl.grid(True)
    pl.show()


directory = 'D:/githubrepository/FBCrawl/extracted/'
presentFile = 'english_Hiking With Dogs.json'

avgPostPerMonth_arr = []
countShared_arr = []
countPPUpdated_arr = []
countCPUpdated_arr = []

with open(directory+'/'+presentFile) as data_file:
    json_data = json.load(data_file)
    for username in json_data:
        totalpost = len(json_data[username]['timeline'])
        print username
        print "totalpost : ", totalpost


        countShared = 0
        countPPUpdated = 0
        countCPUpdated = 0
        dateUpdated = []

        for x in json_data[username]['timeline']:
            # print x
            if "shared" in x[3]:
                countShared += 1

            if "cover photo" in x[3]:
                countCPUpdated += 1

            if "profile picture" in x[3]:
                countPPUpdated += 1

            # average per hari
            # dateUpdated.append(x[6].split(' at ')[0])

            # average per bulan
            dateUpdated.append(x[6].split(', ')[1].split(' ')[0]+" "+x[6].split(', ')[2].split(' at ')[0])

        print "tanggal update", dateUpdated

        groupByDate = collections.Counter(dateUpdated)
        print sum(groupByDate.values())
        print len(groupByDate.keys())
        # print "average posts/day : ", sum(groupByDate.values())//len(groupByDate.keys())

        avgPostPerMonth = sum(groupByDate.values())//len(groupByDate.keys())
        avgPostPerMonth_arr.append(avgPostPerMonth)

        countShared_arr.append(countShared)
        countPPUpdated_arr.append(countPPUpdated)
        countCPUpdated_arr.append(countCPUpdated)

    print "average posts/month : ", avgPostPerMonth_arr
    # normalDist(avgPostPerMonth_arr)

    """
    print "countShared : ", countShared_arr
    print "countPPUpdated : ", countPPUpdated_arr
    print "countCPUpdated : ", countCPUpdated_arr
    """



