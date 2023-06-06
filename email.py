from csv_open import open_csv
from massage import read_message

def main():
    data = open_csv()
    names1, school1, rating1, missing_task1 = data
    file = 'message.txt'
    message = read_message(file)
    file2 = 'message1.txt'
    message1 = read_message(file2)


    for i in range(len(names1)):
        names = names1[i]
        school = school1[i]
        missing_task = int(missing_task1[i])
        rating = int(rating1[i])


        if rating > 5:
            message_out = message1.format(names1[i], school, missing_task, rating)
        else:
            message_out = message.format(names1[i], school1[i], missing_task, rating, rating+1)
        print(message_out)

        print('*'*150)

if __name__ == '__main__':
    main()