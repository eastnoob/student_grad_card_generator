import pandas as pd
import score






score_excel = 'tables\\学生成绩.xlsx' 
comment_excel = 'tables\\学生评语.xlsx' 
time = getTime()

score_df = pd.read_excel(score_excel) 
comment_df = pd.read_excel(comment_excel)

comment = 

# 生成成绩表
for row in score_excel.iterrows(): 
    student = score.Score(row).generateScoreTables()
    stu_name = student[0]
    stu_id = student[1]
    stu_score_table = student[2]
    
    # 读取
    

# 1. 打开成绩单
# 2. 提取人名，成绩
# 3. 将人名、成绩写入一页

# 1. 打开评语
# 2. 将人名，评语写在第二页

# a = input("ccc")
# print(type(a))

# print("test")

# 输入日期：
def getTime():
    year = input("请输入年：")
    month = input("请输入月：")
    day = input("请输入日：")
    
    time = year + "年" + month + "月" + day + "日"
    
    # print("请确认日期是否正确：Y/N： " + time)
    
    return time

# 输入姓名：



from comment import Comment

a = Comment("1", "2", "3")

print(a.result)

# print(a.comment_joint())