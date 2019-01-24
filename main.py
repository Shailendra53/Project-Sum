import locationExtraction as le
import sys


if len(sys.argv) > 1:

	names, NCL, CL, CWL = le.return_entities(sys.argv[1])
	print(names)
	print(NCL)
	print(CL)
	print(CWL)

else:

	print("Supply Proper Arguments as follows:\n$ python main.py 'Text'")
