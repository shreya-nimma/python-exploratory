import argparse

def add(operands):
    operands = [float(i) for i in operands]
    print("Result of addition is: {}".format(sum(operands)))

def subtract(operands):
	operands = [float(i) for i in operands]
	print("Result of subtraction is: {}".format(operands[0] - operands[1]))

def multiply(operands):
	operands = [float(i) for i in operands]
	result = 1
	for i in operands:
		result *= i
	print("Result of multiplication is: {}".format(result))

def divide(args):
    if args.remainder:
        operands = [int(i) for i in args.div_operands]
        print("Result of integer division is: {}".format(operands[0]/operands[1]))
        print("Remainder is: {}".format(operands[0] % operands[1]))
    else:
        operands = [float(i) for i in args.div_operands]
        print("Result of float division is: {}".format(operands[0] / operands[1]))

parser = argparse.ArgumentParser(description="A simple calculator tool.")
subparsers = parser.add_subparsers(dest="operation")

# Parser Configuration
addition_parser = subparsers.add_parser('add')
addition_parser.add_argument('add_operands', nargs="*")

subtraction_parser = subparsers.add_parser('subtract')
subtraction_parser.add_argument('sub_operands', nargs=2)

multiplication_parser = subparsers.add_parser('multiply')
multiplication_parser.add_argument('mult_operands', nargs="*")

division_parser = subparsers.add_parser('divide')
division_parser.add_argument('div_operands', nargs=2)
division_parser.add_argument('-r', "--remainder", action="store_true")

args = parser.parse_args()

if hasattr(args, 'add_operands'):
    add(args.add_operands)
elif hasattr(args, 'sub_operands'):
    subtract(args.sub_operands)
elif hasattr(args, 'mult_operands'):
    multiply(args.mult_operands)
elif hasattr(args, 'div_operands'):
    divide(args)
else:
    print("Please enter an operation followed by operands.")

