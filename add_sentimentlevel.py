import csv
import os

new_row = []
data_file = open('2allpost_subj_pol.csv', 'rb')
csv_read = csv.reader(data_file, delimiter=',')

data_write = open('2allpost_subj_pol_sentlev.csv', 'wb')
csv_write = csv.writer(data_write, lineterminator = '\n')

all = []
row = next(csv_read)
row.append('OriSenLev')
all.append(row)

for i, row in enumerate(csv_read):
    if i > 0 :
        subj_val = float(row[4])
        pol_val = float(row[6])
        if ( (subj_val < 0) and (pol_val < 0) ):
            status = 'SenLev-1'
        elif ( (subj_val == 0.0) and (pol_val == 0.0) ):
            status = 'SenLev0'
        elif ( ( 0.0 < subj_val <= 0.567) and (0.0 < pol_val <= 0.481) ):
            status = 'SenLev1'
        elif ( (0.567 < subj_val <= 0.752 ) and ( 0.481 < pol_val <= 0.850) ):
            status = 'SenLev2'
        elif ( 0.752 < subj_val <= 1 ) and ( 0.850 < pol_val <= 1):
            status = 'SenLev3'
        else:
            status = ''
        row.append(status)
        all.append(row)
csv_write.writerows(all)
data_file.close()
data_write.close()