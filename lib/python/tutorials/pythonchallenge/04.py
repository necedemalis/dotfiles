import httplib2

h = httplib2.Http('.cache')

number = '12345'
for i in range(400):
    temp = ''
    resp, content = h.request (''.join(['http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=',number]), 'GET')
    content = content.decode('utf-8')
    for letter in content:
        if ord(letter) >= 48 and ord(letter) <= 57:
            temp += letter
    if temp == '':
        print(content)
    number = temp
    #print(number)
