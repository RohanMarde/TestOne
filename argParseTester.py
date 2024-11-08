import argparse

parser = argparse.ArgumentParser(
    description = "Divide two integers"
)

parser.add_argument('--dividend', required=True, type=int, metavar='<int>', help="the number you want to divide")

parser.add_argument('--divisor', required=True, type=int, metavar="<int>", help="the number you want to divide by")

arg = parser.parse_args()

result = arg.dividend/arg.divisor

print(result)