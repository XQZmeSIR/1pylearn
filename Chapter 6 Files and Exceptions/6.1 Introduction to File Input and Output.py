# def main():
#     """
#     Purpose: 
#     """
    
# # end def
#     file_variable = open('teeeext.txt', 'r')
#     # file_variable.write('Your skills are increadble!')
#     ab = file_variable.read()
#     print(ab)
#     file_variable.close()

# main()
def main():
    infile = open('friends.txt', 'r')

    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()

    line1 = line1.rstrip('\n')
    line2 = line2.rstrip('\n')
    line3 = line3.rstrip('\n')

    print(line1)
    print(line2)
    print(line3)

main()

    
