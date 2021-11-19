import execjs
node = execjs.get()
ctc = node.compile(open(r'C:\CodeTime\JsSpider\login\js\当乐网login.js',mode='r',encoding='utf-8').read())
funcName = 'get_pwd()'
ras = ctc.eval(funcName)
print(ras)