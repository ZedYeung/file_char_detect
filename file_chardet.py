import codecs
import chardet
import argparse

# commandline args
parser = argparse.ArgumentParser(description="check the encoding of file")
parser.add_argument('file', help="file to check--abs path")
# get args
args = parser.parse_args()
FILE = args.file


def file_chardet(file):
	with codecs.open(file, "rb") as f:
		data = f.read()
		encodeInfo = chardet.detect(data)
		print(encodeInfo["encoding"])

if __name__ == '__main__':
	file_chardet(FILE)
