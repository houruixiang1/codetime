import execjs

node = execjs.get()
ctc = node.compile(open(r'C:\CodeTime\js\国家医疗保障局.js',mode='r',encoding='utf-8').read())
funcName = 'get_data()'
data = ctc.eval(funcName)
print(data)