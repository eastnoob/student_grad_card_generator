# -*- coding: utf-8 -*-  

import pandas as pd
import os
import time

import score
import comment
import markdownPPT
import exportCLI

# 必要内容：
teacher = '何老师 & 田老师'


score_excel = 'tables\\学生成绩.xlsx' 
comment_excel = 'tables\\学生评语.xlsx' 

score_df = pd.read_excel(score_excel) 
comment_df = pd.read_excel(comment_excel)

# comment = 

# 生成成绩表
for row in score_df.iterrows(): 
    # os.wait()
    
    student = score.Score(row).generateScoreTables()
    stu_name = student[0]
    stu_id = student[1]
    stu_score_table = student[2]
    
    # comment_txt = None
    # 获取评语文字
    if comment_df.loc[row[0]]['学生姓名'] == stu_name:
        comment_txt = comment_df.loc[row[0]]['学生评语']
    
    # 生成格式化的评语
    student_comment = comment.Comment(stu_name, comment_txt, teacher, 2023, 1, 6)
    stu_comment = student_comment.getComment()
    
    # 建立markdown
    markdown = markdownPPT.MarkDownPPT(stu_name, stu_id, stu_score_table, stu_comment)
    file_path = markdown.getFilePath()
    file_name = markdown.getFileName()
    
    markdown.generateMarkdownFile()
    
    YESSSSSSSSS = None
    if os.path.exists(file_path):
        YESSSSSSSSS = True
    else:
        YESSSSSSSSS - False
    
    # 导出
    exporter = exportCLI.ExportPDf(file_path, file_name)
    exporter.exportPDF()
    
    # time.sleep(5)
    # os.waitpid()
    
    # os.wait()
    

# 1. 打开成绩单
# 2. 提取人名，成绩
# 3. 将人名、成绩写入一页

# 1. 打开评语
# 2. 将人名，评语写在第二页

# a = input("ccc")
# print(type(a))

# print("test")

# # 输入日期：
# def getTime():
#     year = input("请输入年：")
#     month = input("请输入月：")
#     day = input("请输入日：")
    
#     time = year + "年" + month + "月" + day + "日"
    
#     # print("请确认日期是否正确：Y/N： " + time)
    
#     return time

# 输入姓名：



# from comment import Comment

# a = Comment("1", "2", "3")

# print(a.result)

# # print(a.comment_joint())