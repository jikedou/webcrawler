# coding:utf-8
# 专门用来提取html中内容的
from bs4 import BeautifulSoup
import requests
import MySQLdb
import json
import time

# url = 'https://www.lagou.com/jobs/list_python?city=%E5%85%A8%E5%9B%BD&cl=false&fromSearch=true&labelWords=&suginput='
# url='https://www.lagou.com/'
"""ddddddd"""


def get_deatail(id):
    url = "https://www.lagou.com/jobs/%d.html" % id
    # print url
    headers = {
        "Host": "www.lagou.com",
        "Referer": "https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=",
        "Upgrade - Insecure - Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
    }

    req = requests.get(url, headers=headers)
    # 需要安装xml
    soup = BeautifulSoup(req.content, "lxml")
    detail = soup.find("dd", attrs={"class": "job_bt"})
    # 判断detail是否为None，true则返回空，false则返回内容
    if detail is None:
        return ""
    # print detail.text
    return detail.text


def getUrlStr():
    # 第1层过滤
    # 请求的头部信息
    headers = {
        # 一般会判断cookie host等
        # 代表向服务器发送请求的人--这个是必须要加上去的
        # 特别重要
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0",
        # "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
        "Host": "www.lagou.com",
        # 从哪一个网站上跳过来的
        "Referer": "https://www.lagou.com/jobs/list_python?city=%E5%85%A8%E5%9B%BD&cl=false&fromSearch=true&labelWords=&suginput=",
        #
        "X-Anit-Forge-Code": "0",
        "X-Anit-Forge-Token": None,
        "X-Requested-With": "XMLHttpRequest"
    }

    url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false&isSchoolJob=0'
    positions = []
    for x in range(1, 10):
        # 第二层过滤
        form_data = {
            # "first": "true",
            # 访问的页码
            "pn": x,
            # 访问的关键字
            "kd": "python"
        }

        # 请求方式为get
        # result = requests.get(url, headers=headers)
        # 请求方式为post
        result = requests.post(url, headers=headers, data=form_data)
        position_page = result.json()["content"]["positionResult"]["result"]
        time.sleep(5)
        for position in position_page:
            # 提取一部分信息，没用的就不要了
            position_dic = {
                "positionId": position["positionId"],
                "positionName": position["positionName"],
                "education": position["education"],
                "city": position["city"],
                "district": position["district"],
                "companyId": position["companyId"],
                "companyFullName": position["companyFullName"],
                "companyShortName": position["companyShortName"],
                "salary": position["salary"],
                "workYear": position["workYear"]
            }
            positionid = position["positionId"]
            position_dic["positionDetail"] = get_deatail(positionid)

            positions.append(position_dic)
            # 出现操作频繁，请稍后再试的解决办法，让他睡一会儿
            time.sleep(5)

        # 保存到文件
        lines = json.dumps(positions, ensure_ascii=False)
        with open("lagou_python.json", "w") as fp:
            fp.write(lines.encode("utf-8"))

    def toDB():
        conn = MySQLdb.connect(host="127.0.0.1", passwd="123456", user="root", db="lagou", port=3306, charset="utf8")
        # 创建游标，传入游标的类型是DictCursor, 意味着查询出的结果是Dict类型，默认是tuple类型
        curs = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        # query = """
        #             select * from positions
        #         """
        # curs.execute(query)
        # result = curs.fetchall()
        # print result
        # 插入数据
        insert_sql = """
                    insert into positions VALUES (
                    '%d', '%s', '%s', '%s', '%s', '%d', '%s', '%s', '%s'，'%s', 
                    '%s', '%s', '%s', '%d', '%d', '%s', '%s', '%s', '%d'，'%s', 
                    '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%d', '%d'，'%s', 
                    '%s', '%s', '%s', '%d', '%d', '%d', '%s', '%s', '%s'，'%s', 
                    '%d', '%s', '%s', '%s', '%d', '%s'
                    )
                """
        try:

            for line in str:
                print "================="
                # print line["positionName"]
                # 执行SQL
                result = curs.execute(insert_sql % (
                    # line["companyId"],line["companyId"],line["companyId"],line["companyId"],line["companyId"],
                    # line["companyId"],line["companyId"],line["companyId"],line["companyId"],line["companyId"],
                    # line["companyId"],line["companyId"],line["companyId"],line["companyId"],line["companyId"],
                    # line["companyId"],line["companyId"],line["companyId"],line["companyId"],line["companyId"],
                    # line["companyId"],line["companyId"],line["companyId"],line["companyId"],line["companyId"],
                    # line["companyId"],line["companyId"],line["companyId"],line["companyId"],line["companyId"],
                    # line["companyId"],line["companyId"],line["companyId"],line["companyId"],line["companyId"],
                    # line["companyId"],line["companyId"],line["companyId"],line["companyId"],line["companyId"],
                    # line["companyId"],line["companyId"],line["companyId"],line["companyId"],line["companyId"],
                    # line["companyId"]
                    9, "01", "01", "01", "01", 9, "01", "01", "01", "01",
                    "01", "01", "01", 9, 9, "01", "01", "01", 9, "01",
                    "01", "01", "01", "01", "01", "01", "01", 9, 9, "01",
                    "01", "01", "01", 9, 9, 9, "01", "01", "01", "01",
                    9, "01", "01", "01", 9, "01"

                ))
                # 提交事务
                conn.commit()
                print type(result), result
        except MySQLdb.Error, e:
            # 事务回滚
            conn.rollback()
        finally:
            # 打印影响的行
            curs.close()
            conn.close()


if __name__ == '__main__':
    getUrlStr()
