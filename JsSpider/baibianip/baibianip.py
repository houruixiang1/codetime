import requests
import execjs
ip='ZGLmAQxkAQN4BGR5ZP4lZGNhZGLhZGNkZGL0ZmR2ZmHjAt=='
node = execjs.get()
ctc = node.compile(open(r'C:\CodeTime\js\baibianip.js',mode='r',encoding='utf-8').read())
funcName = 'get_ip("{0}")'.format(ip)
ip = ctc.eval(funcName)
print(ip)