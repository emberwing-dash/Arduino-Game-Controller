def readAnlog():
    val1 = pin1.read()
    val2 = pin2.read()
    return (val1,val2)

# def readJump():
#     val3= pin3.read()
#     return val3

from pyfirmata import Arduino, util

port = "COM6"
board = Arduino(port)

# read value from analog pin A0
pin1 = board.get_pin('a:0:i')
pin2 = board.get_pin('a:1:i')
# pin3 = board.get_pin('d:8:i')

it = util.Iterator(board)
it.start()

# while (True):
#     val = read_move_input()
#     print(val)
#     time.sleep(1)

