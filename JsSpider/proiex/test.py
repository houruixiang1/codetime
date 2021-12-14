import json
import re
import sys
import threading
import time
import os

from service.utils_proiex import Proxy_pool

DIR_BASE = os.path.dirname(os.path.abspath(__file__)) + '/../..'
os.chdir(DIR_BASE)
sys.path.append(DIR_BASE)

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
# }


'''
    github大佬仓库：https://github.com/srx-2000/spider_collection
    代理大佬仓库：https://github.com/jhao104/proxy_pool
    运行代理：python proxyPool.py server
    *特别注意端口的正确*
    *尤其注意下边存入txt文件时，路径的正确*

'''


class zhihu_answer():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
    }
    proxy_pool = Proxy_pool()
    def get_answer(self):
        url = 'https://list.jd.com/list.html?cat=11729,11730,6908'
        response = self.proxy_pool.get_response(url, headers=self.headers)
        print(response.text)
if __name__ == '__main__':
    task = zhihu_answer()
    task.get_answer()
#             json_result = json.loads(response.content)
#             data = json_result["data"]
#             print("爬取进度:" + str(round(i / (total_num // limit) * 100, 2)) + "%")
#             for i in data:
#                 content_list.append(i["content"])
#                 author_name_list.append(i['author']['name'])
#                 author_id_list.append(i['author']['id'])
#                 author_url_token_list.append(i['author']['url_token'])
#         dict["content_list"] = content_list
#         dict["author_name_list"] = author_name_list
#         dict["author_id_list"] = author_id_list
#         dict["author_url_token_list"] = author_url_token_list
#         return dict
#
#     def get_total(self, question_id):
#         url = "https://www.zhihu.com/api/" \
#               "v4/questions/{question_id}/answers?include=data%5B*%5D." \
#               "is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_co" \
#               "llapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse" \
#               "_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_co" \
#               "unt%2Ccan_comment%2Ccontent%2Ceditable_content%2Cattachment%2Cvote" \
#               "up_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2C" \
#               "updated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Cis_labe" \
#               "led%2Cpaid_info%2Cpaid_info_content%2Crelationship.is_authorized%2Cis_author%" \
#               "2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_recognized%3Bdata%5B*%5D.mark_infos%5B*%5D" \
#               ".url%3Bdata%5B*%5D.author.follower_count%2Cbadge%5B*%5D.topics%3Bdata%5B*%5D.settings." \
#               "table_of_content.enabled&offset=&limit={limit}&sort_by=default&platform=desktop".format(
#             question_id=str(question_id), limit=20)
#         response = self.proxy_pool.get_response(url, headers=self.headers)
#         time.sleep(1)
#         json_result = json.loads(response.content)
#         next_json = json_result
#         total_num = next_json['paging']['totals']
#         return total_num
#
#     def format_content(self, content_list):
#         text_list = []
#         pre = re.compile('>(.*?)<')
#         for i in content_list:
#             text = ''.join(pre.findall(i))
#             text_list.append(text)
#         return text_list
#
#     def get_question_title(self, question_id):
#         url = "https://www.zhihu.com/api/" \
#               "v4/questions/{question_id}/answers?include=data%5B*%5D." \
#               "is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_co" \
#               "llapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse" \
#               "_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_co" \
#               "unt%2Ccan_comment%2Ccontent%2Ceditable_content%2Cattachment%2Cvote" \
#               "up_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2C" \
#               "updated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Cis_labe" \
#               "led%2Cpaid_info%2Cpaid_info_content%2Crelationship.is_authorized%2Cis_author%" \
#               "2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_recognized%3Bdata%5B*%5D.mark_infos%5B*%5D" \
#               ".url%3Bdata%5B*%5D.author.follower_count%2Cbadge%5B*%5D.topics%3Bdata%5B*%5D.settings." \
#               "table_of_content.enabled&offset=&limit={limit}&sort_by=default&platform=desktop".format(
#             question_id=str(question_id), limit=20)
#         response = self.proxy_pool.get_response(url, headers=self.headers)
#         json_result = json.loads(response.content)
#         # print(json_result)
#         data = json_result["data"]
#         title = data[0]['question']['title']
#         return title
#
#     def single_answer(self, question_id):
#         question_title = self.get_question_title(question_id)
#         print("全部回答数量:" + str(self.get_total(question_id)))
#         print("爬取的问题：" + question_title + "——问题id为：" + str(question_id))
#         print("爬取ing.....请等待，等待时间依据回答数量而定")
#         result_dict = self.get_answer(question_id)
#
#         # self.get_answer(question_id)
#         text_list = self.format_content(result_dict['content_list'])
#         try:
#             print("爬取正常！！！")
#             with open(os.getcwd() + '\\result\\' + question_title + ".txt", mode="w", encoding='utf-8') as f:
#                 f.write("问题：" + question_title + "\n")
#                 f.write("问题id：" + str(question_id) + "\n\n")
#                 for i in range(0, len(text_list)):
#                     f.write("回答者id：" + result_dict["author_id_list"][i] + "\n")
#                     f.write("回答者空间地址：" + result_dict["author_url_token_list"][i] + "\n")
#                     f.write("回答者昵称：" + result_dict["author_name_list"][i] + "\n")
#                     f.write("回答的内容：" + text_list[i] + "\n\n")
#             f.close()
#         except:
#             print("爬取异常！！！")
#             pass
#         finally:
#             print("爬取完成")
#
#     def get_next_question(self, question):
#         url = "https://www.zhihu.com/api/v4/questions/{question_id}/similar-questions?include=data%5B*%5D.answer_count%2Cauthor%2Cfollower_count&limit=5".format(
#             question_id=question)
#         # print(url)
#         response = self.proxy_pool.get_response(url, headers=self.headers)
#         # print(response.text)
#         json_result = json.loads(response.content)
#         url_list = json_result['data']
#         # with open("questions_id.txt", mode="a", encoding='utf-8') as f:
#         for i in url_list:
#             if not self.copy_list.__contains__(i['id']):
#                 self.similar_question_url_list.append(i['id'])
#                 self.copy_list.append(i['id'])
#                 # self.copy_list.append(i['id'])
#                 # f.write(str(i['id'])+"\n")
#                 print(i['id'])
#                 if len(self.copy_list) >= self.question_count:
#                     return
#                 self.get_parse_question()
#             # return self.similar_question_url_list
#         # f.close()
#
#     def get_parse_question(self):
#         for i in self.similar_question_url_list:
#             try:
#                 self.get_next_question(i)
#                 self.similar_question_url_list.remove(i)
#             except:
#                 pass
#             if len(self.copy_list) >= self.question_count:
#                 return
#
#     def download_all_similar_question(self):
#         threads = []
#         # time.sleep(5)
#         if len(self.copy_list) >= self.question_count:
#             for i in self.copy_list:
#                 th = threading.Thread(target=self.single_answer, args=(i,))
#                 # print(th.name)
#                 th.start()
#                 threads.append(th)
#             for th in threads:
#                 th.join()
#         elif (len(self.copy_list) == 0):
#             self.get_next_question(self.begin_id)
#             self.download_all_similar_question()
#         else:
#             self.get_next_question(self.copy_list[len(self.copy_list) - 1])
#             self.download_all_similar_question()
#
#
# if __name__ == '__main__':
#     model = input("请输入想要选取的模式:1.爬取单个问题  2.爬取相关问题\n")
#     id = input("请输入想要爬取的问题的id，或相关问题的起点问题的id:\n")
#     if int(model) == 1:
#         zhihu = zhihu_answer(id, id)
#         zhihu.single_answer(id)
#     elif int(model) == 2:
#         count = 20
#         count = input("请输入想要爬取的相关问题的个数（默认为20，最大为400，知乎超过500会有反爬验证）:\n")
#         zhihu = zhihu_answer(id, id, int(count))
#         zhihu.download_all_similar_question()
#     else:
#         print("请输入规范数字1或2")