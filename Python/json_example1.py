import csv

txt_file = r"TRIAL1.txt"
csv_file = r"TRIAL1.csv"


in_txt = csv.reader(open(txt_file, "rb"), delimiter = '\t')
out_csv = csv.writer(open(csv_file, 'a'))

out_csv.writerows(in_txt)