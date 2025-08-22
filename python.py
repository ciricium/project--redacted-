#its python
#just throw it into a web interpreter
#trust me its pain without

table = {"01": "a", "02": "b", "03": "c", "04": "d", "05": "e", "06": "f", "07": "g", "08": "h", "09": "i", "10": "j", "11": "k", "12": "l", "13": "m", "14": "n", "15": "o", "16": "p", "17": "q", "18": "r", "19": "s", "20": "t", "21": "u", "22": "v", "23": "w", "23": "w", "24": "x", "25": "y", "26": "z", "27": " "}

table_swap = {}

for i in table:
    table_swap[table[i]] = i

def decode(string):
    xto8 = string.replace("x", "8")
    yto4 = xto8.replace("y", "4")
    minus8 = str(int(yto4) - 8)
    div2 = str(int(minus8) // 2)
    flipped = div2[::-1]

    string = ""
    decoded = ""
    for i in flipped:
        string += i
        if len(string) == 2:
            decoded += table[string]
            string = ""
    return decoded

def encode(string):
    result = ""
    for i in string:
        result += table_swap[i]
    flipped = result[::-1]
    div2 = str(int(flipped) * 2)
    add8 = str(int(div2) + 8)
    yis4 = add8.replace("4", "y")
    eightis4 = yis4.replace("8", "x")

    return eightis4

while True:
    message = input("Enter message: ")
    try:
        print(encode(message))
    except:
        print(decode(message))
