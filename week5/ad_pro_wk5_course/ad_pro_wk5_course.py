import sys
from argparse import ArgumentParser
import pdb
def breakdown(amount: float):
    bills = [] 
    if amount != int(amount):  
        coin_par = amount - int(amount)
        bill_par = int(amount)
    else:
        bill_par = amount
        coin_par = 0
    #the start of the bill computation
    add = 0
    hundred_num = bill_par // 100
    bills.append(hundred_num)
    add = hundred_num * 100

    fifty_num = (bill_par - add) // 50
    bills.append(fifty_num)
    add += fifty_num * 50

    twenty_num = (bill_par - add) // 20
    bills.append(twenty_num)
    add += twenty_num * 20

    ten_num = (bill_par - add) // 10
    bills.append(ten_num)
    add += ten_num * 10

    five_num = (bill_par - add) // 5
    bills.append(five_num)
    add += five_num * 5

    one_num = (bill_par - add) // 1
    bills.append(one_num)
    #the end of the bill computation
    
    #the start of the coin computation
    coins=[]
    coin_par=coin_par*100
    add = 0
    quarter_num = coin_par // 25
    coins.append(quarter_num)
    add = quarter_num * 25

    dimes_num = (coin_par - add) // 10
    coins.append(dimes_num)
    add += dimes_num * 10

    nickels_num = (coin_par - add) // 5
    coins.append(nickels_num)
    add += nickels_num * 5

    pennies_num = (coin_par - add) // 1
    coins.append(pennies_num)
    #the end of the coin computation
    return coins,bills
    
if __name__ == '__main__':
    #num = float(input('---this is a program to calculate your bills---\nwhat number do u wanna convert?'))
    # num=float(sys.argv[1])
    parser=ArgumentParser()
    parser.add_argument('--amount',type=float,default=123.21,help='just input that number')
    args=parser.parse_args()
    num=args.amount
    if num > 999.99:
        print('unable to calculate, type number less than 1000!')
    else:
        coins,bills = breakdown(num) 
        num_dict = { 0.0:'no',
            1.0: 'one',
            2.0: 'two',
            3.0: 'three', 
            4.0: 'four',
            5.0: 'five',
            6.0: 'six',
            7.0: 'seven',
            8.0: 'eight',
            9.0: 'nine',
            10.0: 'ten'}
        print(num_dict[bills[0]],'100$ bills,',
                num_dict[bills[1]],'50$ bills,',
                num_dict[bills[2]],'20$ bills,',
                num_dict[bills[3]],'10$ bills,',
                num_dict[bills[4]],'5$ bills,',
                num_dict[bills[5]],'1$ bills.\nAnd the coin part is',
                num_dict[coins[0]],'quarters',
                num_dict[coins[1]],'dimes',
                num_dict[coins[2]],'nickels',
                num_dict[coins[3]],'pennies',)