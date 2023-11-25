import csv

input_file = 'global_voices_en_fa.tsv'
output_file_s = 's.txt'
output_file_t = 't.txt'

with open(input_file, 'r', newline='', encoding='utf-8') as tsvfile, open(output_file_s, 'w', encoding='utf-8') as file_s, open(output_file_t, 'w', encoding='utf-8') as file_t:
    reader = csv.reader(tsvfile, delimiter='\t')
    for row in reader:
        file_s.write(row[0] + '\n')

        file_t.write(row[1] + '\n')
