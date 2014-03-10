import turtle
import sys

N = 10**6

def main():
    angle_power, move_power, scale = parse_args()
    turtle.speed('fastest')
    for i in range(1, N):
        turtle.left(i**angle_power)
        turtle.forward(i**move_power / scale)

def parse_args():
    if len(sys.argv) < 3:
        print("\nThis programm should be called as follows:\
            \n\tpython %s <angle_power> <move_power> <scale>\n\
            \nfor example try one of these commands:\
            \n\tpython %s 1 1 1\
            \n\tpython %s 1 1 30\
            \n\tpython %s 1 1 1000\
            \n\tpython %s 2 1 1000\
            \n\tpython %s 1 1.5 1000\
            \n\tpython %s 1 2 1000\
            " % tuple([sys.argv[0]] * 7))
        sys.exit(1)

    angle_power = float(sys.argv[1])
    move_power = float(sys.argv[2])
    scale = float(sys.argv[3])
    return angle_power, move_power, scale

main()
