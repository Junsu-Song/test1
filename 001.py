import sys

if len(sys.argv) != 2:
    print(f"usage: python {sys.arrgv[0] [num]")
    sys.exit()

num = int(sys.argv[1])
print(10 / num)

