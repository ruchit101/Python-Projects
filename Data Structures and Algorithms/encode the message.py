dict = {
    "A": "@",
    "B": "$", "C": "SEE", "D": "dEE", "E": "EEE", "F": "AF", "G": "JEE", "H": "AH", "I": "EYE",
    "J": "GEY", "K": "K@Y", "L": "@L", "M": "@M", "N": "@N", "O": "0", "P": "PEE", "Q": "QUEUE", "R": "MAIN",
    "S": "YES", "T": "TEA",
    "U": "YOU", "V": "WE", "W": "DBLU", "X": "EX", "Y": "WHY", "Z": "Z"
}


def encode(str):
    new_str = []
    for i in str.strip():
        new_str.append(dict[i])
    new_strng= "".join(new_str)
    print(new_strng)

strng = "HGDBFGDTGST"
print(encode(strng))
