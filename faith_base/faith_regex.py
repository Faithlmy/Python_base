import re
line = "cats are is; smaller than; dogs are de;"
k = re.findall(r';', line)
g = re.finditer(r';', line)
print(k)
print(g)
m = re.match(r'cat', line, re.M|re.I)
if m:
    print("match: ", m.group())
else:
    print("no match")
s = re.search(r'd', line, re.M|re.I)
if s:
    print("serch： ", s.group())
else:
    print("no serch")

"""====================================="""
"""
\d  匹配任何十进制数[0-9]
\D  匹配任何非数字字符[^0-9]
\s  匹配任何非空白字符
\S  匹配任何空白字符
\w  匹配任何非数字字母字符[^a-zA-Z0-9]
\W  匹配任何数字字母字符[a-zA-Z0-9]
match() 	決定 RE 是否在字符串剛開始的位置匹配
search() 	掃瞄字符串，找到這個 RE 匹配的位置
findall() 	找到 RE 匹配的所有子串，並把它們作為一個列表返回
finditer() 	找到 RE 匹配的所有子串，並把它們作為一個迭代器返回
split() 	將字符串在 RE 匹配的地方分片並生成一個列表
sub() 	找到 RE 匹配的所有子串，並將其用一個不同的字符串替換
subn() 	與 sub() 相同，但返回新的字符串和替換次數
re.I 	執行不區分大小寫的匹配。
re.L 	根據當前的語言環境解釋詞組。這種解釋影響字母組（w和W），以及單詞邊界的行為（和B）
re.M 	使$匹配一行（串的不隻是端部）的尾部，使^匹配的行（串不隻是開始）的開始
re.S 	使一個句號（點）匹配任何字符，包括換行符
re.U 	根據Unicode字符集解釋的字母。這個標誌會影響w, W, , B的行為。
re.X 	許可證“cuter”正則表達式語法。它忽略空格（除了一組[]或當用一個反斜杠轉義內），並把轉義＃作為注釋標記
"""

phone = "133-1234-5678 # This is Phone Numbe"
num1 = re.sub(r'#.*$', "", phone)
print(num1)
num2 = re.sub(r'\w', "", phone)
print(num2)

print("======match======"*50)
pattern = re.compile(r'\d+')
# m = pattern.match('one12twothree34four')
m = pattern.match('one12twothree34four',3,10)
print(m)
print(m.group())
print(m.group(0))
print("end: ", m.end(0))
print(m.start(0))
print(m.span(0))

print("+"*50)
pat = re.compile(r'([a-z]+) ([a-z]+)', re.I)
m = pat.match('Hello World Wide Web')
print(m.group())
print(m.start())
print(m.end())
print(m.span(2))

print("=====search====="*30)
pattern = re.compile('\d+')
m = pattern.search('one12twothree34four')
print(m.group())
m = pattern.search('one12twothree34four', 10, 30)
print(m.group())