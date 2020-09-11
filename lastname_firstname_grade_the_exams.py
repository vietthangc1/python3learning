import numpy as np

filename = input('Enter a class file to grade (i.e. class1 for class1.txt): ')
answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
list_ans = answer_key.split(",")
list_diem = []
list_id = []

def tinh_diem(answer,key):
    diem = 0
    for i in range(len(key)):
        if answer[i] == '':
            pass
        elif answer[i] == key[i]:
            diem += 4
        else:
            diem -= 1
    return diem

try:
    _f = open('data/'+filename+'.txt','r', encoding = "utf-8")
    nd = _f.readlines()
    _f.close()

    count_invalid = [0 for i in range(len(nd))]
    index = 0

    print("Successfully opened ", filename, ".txt")
    print("**** ANALYZING ****")
    
    for line in nd:
        phay = line.count(",")
        id = line.split(",")[0]
        so_id = id[1:]
        
        if phay != 25:
            print('Invalid line of data: does not contain exactly 26 values:')
            print(line)
            count_invalid[index] = 1
        
        if (id[0] != "N") or (not so_id.isdigit()) or (len(so_id) != 8):
            print("Invalid line of data: N# is invalid")
            print(line)
            count_invalid[index] = 1
        
        if count_invalid[index] == 0:
            list_id.append(id)
            list_diem.append(tinh_diem(line.split(",")[1:],list_ans))

        index += 1
    
    if count_invalid.count(1) == 0:
        print("No errors found!")
    
    print("**** REPORT ****")

    valid_count = count_invalid.count(0)
    invalid_count = count_invalid.count(1)
    print("Total valid lines of data: ",valid_count)
    print("Total invalid lines of data: ",invalid_count)
    
    array_diem = np.array(list_diem)
    print('Mean (average) score: ', np.mean(array_diem))
    print('Highest score: ', np.max(array_diem))
    print('Lowest score: ', np.min(array_diem))
    print('Range of scores: ', np.max(array_diem) - np.min(array_diem))
    print('Median score: ', np.median(array_diem))

    with open('results/'+filename+'_grades.txt','w',encoding='utf-8') as _f:
        for i in range(valid_count):
            ghi = str(list_id[i]) + ',' + str(list_diem[i]) + '\n'
            _f.write(ghi)

except FileNotFoundError:
    print("Sorry, I can't find this filename")
