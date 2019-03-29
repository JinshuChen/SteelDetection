import csv

csv_path = '/home/c/workspace/tf_models/research/SteelDetection/train_data/nas_train_data_4.csv'

csv_reader = csv.reader(open(csv_path,'r'))
# print(csv_reader)
count_circle = 0
count_NH = 0
count_sigma = 0
count_TH = 0
count_all = 0

for lines in csv_reader:
    # print(lines[3])
    count_all = count_all + 1
    if lines[3] == 'circle_steel':
        count_circle = count_circle + 1
    elif lines[3] == 'NHsquare_steel':
        count_NH = count_NH + 1
    elif lines[3] == 'sigma_steel':
        count_sigma = count_sigma + 1
    elif lines[3] == 'THsquare_steel':
        count_TH = count_TH + 1
    else:
        pass
count_all = count_all - 1
print('count_circle = ', count_circle)
print('count_NH = ', count_NH)
print('count_sigma = ' , count_sigma)
print('count_TH = ', count_TH)
print('all = ', count_all)
if count_all == count_circle + count_NH + count_sigma + count_TH:
    print('verified!')
else:
    print('error!')