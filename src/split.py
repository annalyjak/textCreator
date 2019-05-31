import csv

path = "../data/"

file_input = "PoliMorf-0.6.7.tab"  # "testFile.tab" #
file_output_unique = "PoliMorf_for_sentencepiece_unique.txt"
file_output_all = "PoliMorf_for_sentencepiece.txt"

with open(path + file_input, newline = '') as file:
    file_reader = csv.reader(file, delimiter='\t')
    writer_all = csv.writer(open("../data/" + file_output_all, 'w'))

    new_file_with_repeat = []
    new_file_unique = []
    for f in file_reader:
        # print(f[0])
        new_file_with_repeat.append(f[0])
        writer_all.writerow([f[0]])
    writer_unique = csv.writer(open("../data/" + file_output_unique, "w"))
    new_file_unique = set(new_file_with_repeat)
    for row in new_file_unique:
        writer_unique.writerow([row])

    # print(new_file_unique)
