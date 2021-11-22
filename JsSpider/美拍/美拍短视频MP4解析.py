import execjs
node = execjs.get()
### 两种方法均可   第一种为自己构造   第二种为直接调用
ctc = node.compile(open(r'C:\CodeTime\js\meipai.js',mode='r',encoding='utf-8').read())
# ctc = node.compile(open(r'C:\CodeTime\js\meipai2.js',mode='r',encoding='utf-8').read())
funcName = 'get_mp4()'
mp4_url = ctc.eval(funcName)
print(mp4_url)