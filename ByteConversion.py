def h2h(hexStr):
    chars = []
    for i in range(len(hexStr)):
        chars.append(hexStr[i])
    returnString = ''
    for char in chars:
        hexStr = str(hex(char))[2:]
        hexStr = '0' + hexStr if len(hexStr) == 1 else hexStr
        returnString += hexStr + ' '
    return returnString[:-1]

def h2s(hexStr):
    hexList = hexStr.split(' ')
    returnString = ''
    for hexItem in hexList:
        char = chr(int(hexItem, 16))
        returnString += (char + ' ') if char != ' ' else ('SPACE ')
    return returnString[:-1]

def h2b(hexStr, width=32):
    bytes = []
    hexStr = ''.join( hexStr.split(" ") )
    for i in range(0, len(hexStr), 2):
        bytes.append( chr( int (hexStr[i:i+2], 16 ) ) )
    return ''.join( bytes )