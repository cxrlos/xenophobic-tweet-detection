import csv 

# Calculate the special chatracters percentage in a tweet. 
def percentageSpecialChars(fp):
    with open(fp, newline='') as f:
        reader = csv.reader(f)
        data = list(reader)

    data[0].insert(21, "exclamation_counter")
    data[0].insert(22, "questionmark_counter")
    data[0].insert(23, "comma_counter")
    data[0].insert(24, "dot_counter")

    for i in range(1, len(data)):
        
        text_length = len(data[i][1])
        exclamation_counter = data[i][1].count('!') / text_length
        questionmark_counter = data[i][1].count('?') / text_length
        comma_counter = data[i][1].count(',') / text_length
        dot_counter = data[i][1].count('.') / text_length


        # print("! - ", exclamation_counter)
        data[i].insert(21, exclamation_counter)
        # print("? - ", questionmark_counter)
        data[i].insert(22, questionmark_counter)
        # print(", - ", comma_counter)
        data[i].insert(23, comma_counter)
        # print(". - ", dot_counter)
        data[i].insert(24, dot_counter)

    return data

def listToCSV(data, fp):
    with open(fp, 'w') as f: 
        write = csv.writer(f) 
        write.writerows(data)
