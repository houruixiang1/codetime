from flask import Flask, render_template,g,redirect,url_for,request,session,jsonify
import utils

app = Flask(__name__)

@app.route('/show')
def show():
    return render_template("show.html")

@app.route('/main')
def main():
    return render_template("main.html")

@app.route('/time')
def get_time():
    return utils.get_time()

@app.route('/c1')
def get_data():
    import pymysql
    datalist1 = []
    datalist2 = []
    datalist3 = []
    host = 'localhost'
    user = 'root'
    password = '123456'
    db = '雪球基金'
    port = 3306
    try:
        db = pymysql.connect(host=host, user=user, password=password, port=port, db=db)
        cursor = db.cursor()
        sql1 = "select 基金分布.usernum from 基金分布 where name ='合计'"
        sql2 = "select 基金分布.fundnum from 基金分布 where name ='合计'"
        sql3 = "select 基金分布.scale from 基金分布 where name ='合计'"
        cursor.execute(sql1)
        for item in cursor.fetchall():
            datalist1.append(item)
        cursor.execute(sql2)
        for item in cursor.fetchall():
            datalist2.append(item)
        cursor.execute(sql3)
        for item in cursor.fetchall():
            datalist3.append(item)
        #print(datalist1, datalist2, datalist3)
        db.commit()
        #print('数据取出成功！')
    except pymysql.Error as e:
        print('数据取出失败：' + str(e))
        db.rollback()
    db.close()
    return jsonify({"usernum":datalist1[0],"fundnum":datalist2[0],"scale":datalist3[0]})

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/index")
def home():
    return index()

@app.route("/fund")
def fund():
    import pymysql
    datalist = []
    host = 'localhost'
    user = 'root'
    password = '123456'
    db = '雪球基金'
    port = 3306
    try:
        db = pymysql.connect(host=host, user=user, password=password, port=port, db=db)
        cursor = db.cursor()
        sql = "select * from 雪球基金"
        cursor.execute(sql)
        for item in cursor.fetchall():
            datalist.append(item)
            #print(datalist)
        db.commit()
        #print('数据取出成功！')
    except pymysql.Error as e:
        #print('数据取出失败：' + str(e))
        db.rollback()
    db.close()
    return render_template('fund.html',funds=datalist)

@app.route("/word")
def word():
    return render_template('word.html')

@app.route("/team")
def team():
    return render_template('team.html')

@app.route("/designer")
def designer():
    return render_template('designer.html')

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port='5000')



# @app.route('/book.html')
# def book():
#     datalist = []
#     db = pymysql.connect(host='localhost', user='root', password='lu123456', port=3306, db='douban')
#     cursor = db.cursor()
#     sql = 'select* from book'
#     cursor.execute(sql)
#     for item in cursor.fetchall():
#         datalist.append(item)
#     db.close()
#     cursor.close()
#     return render_template('book.html',books=datalist)

# @app.route('/ksh.html')
# def ksh():
#     score=[]
#     num=[]
#     db = pymysql.connect(host='localhost', user='root', password='lu123456', port=3306, db='douban')
#     cursor = db.cursor()
#     sql = 'select score,count(score) from book group by score'
#     cursor.execute(sql)
#     for item in cursor.fetchall():
#         score.append(item[0])
#         num.append(item[1])
#     db.close()
#     cursor.close()
#     return render_template('ksh.html',score=score,num=num)
#coding:utf-8

# from flask import Flask,render_template
#
# import json
#
# # 生成Flask实例
# app = Flask(__name__)
#
# # /test路由 接收前端的ajax请求
# @app.route('/test',methods=['POST'])
# def my_echart():
#     import pymysql
#     host = 'localhost'
#     user = 'root'
#     password = '123456'
#     db = 'book'
#     port = 3306
#     db = pymysql.connect(host=host, user=user, password=password, port=port, db=db)
#     cur = db.cursor()
#     sql = 'SELECT t.id,t.sb FROM test t'
#     cur.execute(sql)
#     u = cur.fetchall()
#
#     # 转换成JSON数据格式
#     jsonData = {}
#     xdays = []
#     yvalues = []
#
#     for data in u:
#         # xdays.append(str(data[0]))
#         xdays.append(data[0])
#         yvalues.append(data[1])
#     print(xdays)
#     print(yvalues)
#
#     jsonData['xdays']=xdays
#     jsonData['yvalues'] = yvalues
#     # json.dumps()用于将dict类型的数据转成str，因为如果直接将dict类型的数据写入json会发生报错，因此将数据写入时需要用到该函数。
#     j = json.dumps(jsonData)
#
#     # 在浏览器上渲染my_template.html模板（为了查看输出的数据）
#     return(j)
#
#
# if __name__ == '__main__':
#     # 运行项目
#     app.run(debug=True, host='127.0.0.1', port='5000')