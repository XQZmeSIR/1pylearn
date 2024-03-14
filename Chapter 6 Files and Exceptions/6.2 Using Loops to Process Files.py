# def main():
#     """
#     Purpose: 
#     """
#     sales_file = open('files in Gaddis.txt', 'r')
#     line = sales_file.readline()

#     while line != '':
#         amount = float(line)
#         print(f'{amount:.2f}')
#         line = sales_file.readline()

#     sales_file.close()                  ggggggg

# def main():
#     sales_file = open('files in Gaddis.txt', 'r')

#     for line in sales_file:
#         amout = (float(line))
#         print(f'Values are: {amout:.2f}')
        
#     sales_file.close()



# if __name__ == "__main__":
#     main()


# def main():
#     num_video = int(input('How many projects do you have? '))
#     vidfile = open('video_time.txt', 'w')
#     print('Enter the lenght of the videos')

#     for count in range(1, num_video + 1):
#         lenght = float(input(f"Video #{count}: "))
#         vidfile.write(f'{lenght}\n')

#     vidfile.close()
#     print('Времена сохранены в video_times.txt.')

# main()


# def main():
#     vidfile = open('/home/solleks/Desktop/1pylearn/video_time.txt', 'r')

#     total = 0.0
#     count = 0

#     vidfile.readline()
#     print('Duration of videos:')

#     for line in vidfile:    
#         run_time = float(line)
#         count += 1

#         print('Video #', count, ': ', run_time, sep='')

#         total += run_time

#     vidfile.close()
#     print('Overall Duration is:', total)


# if __name__ == "__main__":
#     main()

# with open('checkpoint.txt', 'w') as file:
#     for number in range(1,11):
#         file.write(str(number) + '\n')

# with open('teeeext.txt', 'r') as file:
#     line = file.readline()  # первичное чтение нужно перед
#     while line != '':       # while но не перед for
#         print(line)
#         line = file.readline()

# with open('teeeext.txt', 'r') as file:
#     for line in file:
#         print(line.strip())









#