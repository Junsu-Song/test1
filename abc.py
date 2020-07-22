import sys

def read_txt(file_name: str):
    ret = ""
    with open(file_name, 'r') as handle:
        for line in handle:
            if line.startswith(">"):
                continue
            ret += line.strip()
        print(type(ret))
        return ret

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"#usage: python {sys.argv[0]} [string]")
        sys.exit()

    file_name = sys.argv[1]
    txt = read_txt(file_name)
    print(txt)
##################################################################
f = "head.txt"

with open(f , 'r') as handle:
    for line in handle:
        print(line.strip())
