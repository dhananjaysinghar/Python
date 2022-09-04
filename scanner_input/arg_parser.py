# pip install argparse
import argparse
# Create the parser
parser = argparse.ArgumentParser()
# Add an argument
parser.add_argument('--name', type=str, required=True)
# Parse the argument
args = parser.parse_args()
# Print "Hello" + the user input argument

print('Hello,',args.name)

#print(parser.print_help())
