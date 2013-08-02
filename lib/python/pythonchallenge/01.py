sentence = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

sentence2 =''
for letter in sentence:

    ascii = ord(letter)
    if ascii >= 97 and ascii <= 122:
        ascii += 2
        if ascii > 122:
            ascii -= 26
    sentence2 += chr(ascii)

print(sentence2)



