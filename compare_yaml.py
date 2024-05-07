import argparse
import yaml
import dictdiffer

parser = argparse.ArgumentParser(description='Convert two yaml files to dict and compare equality. Allows comparison of differently ordered keys.')
parser.add_argument('file_paths', type=str, nargs=2,
                    help='Full paths to yaml documents')
args = parser.parse_args()

print(f"File Path 1: {args.file_paths[0]}")
print(f"File Path 2: {args.file_paths[1]}")

with open(args.file_paths[0],'r') as rdr:
    data1=rdr.read()

with open(args.file_paths[1],'r') as rdr:
    data2=rdr.read()

data1_dict = yaml.load(data1,Loader=yaml.FullLoader)
data2_dict = yaml.load(data2,Loader=yaml.FullLoader)

if data1_dict == data2_dict:
    print("No difference detected")
else:
    print("Differences detected:")
    for diff in list(dictdiffer.diff(data1_dict, data2_dict)):
        print(diff)