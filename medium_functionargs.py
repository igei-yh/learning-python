
import sys


def args_check(args):
    if len(args) != 3:
        print('args error!!')
        sys.exit


def args_sum(args):
    n=0
    for i in range(1, 3):
        n += int(args[i])
    return n


args_check(sys.argv)
v = args_sum(sys.argv)
print(v)
