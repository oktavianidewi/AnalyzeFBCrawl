# to combine user 271 and my user
import savReaderWriter

filename = '271_text_post_list_dw.sav'
filenametowrite = 'all_text_post_list_dw.sav'

newrow = []


with savReaderWriter.SavReader(filename) as reader:
    # for i, line in enumerate(reader):
    for i in range(0, 2):
        newline = []
        newline.append(reader[i][2]) # username
        newline.append(reader[i][12]) # posttext
        newline.append(reader[i][17]) # posttextpolarity
        newline.append(reader[i][18]) # posttextsubjectivity
        newline.append(reader[i][66]) # clustername
    newrow.append(newline)
    # print newline

varNames = ['UserName', 'PostText', 'PostTextPolarity', 'PostTextSubjectivity', 'ClusterName']
varTypes = {'UserName': 1, 'PostText': 1, 'PostTextPolarity': 0, 'PostTextSubjectivity': 0, 'ClusterName': 1}
# varTypes = {'UserName': 5, 'v2': 0, 'v3': 0}

with savReaderWriter.SavWriter(filenametowrite, varNames, varTypes) as writer :
    for x in newrow:
        writer.writerows(x)

"""

"""
"""
# username -> [2]
# posttext -> [12]
# polarity -> [17]
# subjectivity -> [18]
# clustername -> [66]
newline.append(line[2])
newline.append(line[12])
newline.append(line[17])
newline.append(line[18])
newline.append(line[66])
newrow.append(newline)
"""

# print newrow