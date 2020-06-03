print('''


                               __      __ __  |    __  
 /| |__| _| _   |   _  _  _   |__)    (_ |_ | |_/ /  \ 
  |    |(_|(_|\/|__(_)(_)|_)  |__)\/  __)|__| | \ \__/ 
              /          |        /                  


''')
print('                                                      BY SEIKO')
print('-----------------------------------------------------------------------')
print('                                                      INSTGRAM : 6_b_p')
a = input('\033[1;37m'+'user name ==> ')
b = int(input('Enter Number ==> '))

file = open(a,'w')
for A in range(b):
    file.write(a+"\n")
file.close()
file = open(a,'r')
for line in file.readlines():
    print(line)
file.close()
