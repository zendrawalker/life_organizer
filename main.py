
def motivational_quote():
    from random import choice
    with open('motivational_quotes','r') as m:
        #readlines not readline, to read the file line by line
        #we used only choice() instead of random.choice() bec we used from ... import
        quote = choice(m.readlines())
        print(quote)


'''
#didn't work, works better with number, because numbers can be written as strings but not vice versa
def to_do_list():
    try:
        to_do_list =[]
        while True:
            to_do_list.append(input())
    except:
        print(to_do_list)
'''





def toady_agenda():
    to_do_list()
    data_base = {
        'daily habits': ['Exercise', 'study', 'programming', 'hacking'],
        'to do': to_do_list
                 }
    for i in data_base.keys():
        print(i)
    choice = input('enter the name of data you want to view: ').lower()

    if choice == 'daily habits':
        for i in data_base[choice]:
            print(i)
    elif choice == 'to do':
        for i in data_base[choice]:
            print(i)




if __name__ == '__main__':
    motivational_quote()

