name = input('请输入你的名字: ')
age = input('请输入你的年龄: ')
height = input('请输入你的身高: ')
question = input('你是不是男性: ')

msg = '''
-----------Person Info-----------
Name    : %s
Age     : %s
Height  : %s
Answer  : %s
-----------End-------------------
''' % (name, age, height, question)

print(msg)
