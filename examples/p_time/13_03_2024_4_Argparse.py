import argparse

def sum(num1,num2):
    return num1+num2

def main():
    parser =argparse.ArgumentParser(description='Add two numbers')
    parser.add_argument('num1',type=int,help='Enter first number')
    parser.add_argument('num2',type=int,help='Enter second number')
    args=parser.parse_args()
    summation=sum(args.num1,args.num2)
    print(summation)

if __name__=="__main__":
    main()
    
