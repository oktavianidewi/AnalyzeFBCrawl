import csv
import os

new_row = []
filename = '1allpost_subj_pol.csv'
data_file = open(filename, 'rb')
csv_data = csv.reader(data_file, lineterminator = '\n')

data_write = open(filename, 'wb')
# csv_write = csv.writer(data_write, delimiter=',')
csv_write = csv.writer(data_write, lineterminator = '\n')
csv_write.writerow(next(csv_data))
csv_write.writerow(new_row)

for i, x in enumerate(csv_data):
    # print x
    # header = next(csv_data)
    new_row.append('SenLev')
    # if i == 0 :
    #    print x

    if i > 0 :
        subj_val = float(x[5])
        pol_val = float(x[7])
        print subj_val
        print pol_val
        if (subj_val < 0.0) and ( pol_val < 0.0):
            status = 'SenLev-1'
        elif (subj_val == 0.0) and ( pol_val == 0.0):
            status = 'SenLev0'
        elif ( 0.0 < subj_val <= 0.567) and ( 0.0 < pol_val < 0.481):
            status = 'SenLev1'
        elif ( 0.567 < subj_val <= 0.752 and pol_val <= 0.850 ) or ( 0.481 < pol_val < 0.850 and subj_val <= 0.752 ):
            status = 'SenLev2'
        elif ( 0.753 < subj_val <= 1) or ( 0.850 < pol_val < 1):
            status = 'SenLev3'
        else:
            status = ''
            # print status
        new_row.append(status)

data_file.close()


data_write.close()