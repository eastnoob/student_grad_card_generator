from table import TableGenerator

class Score:
    
    def __init__(self, row) -> None:
        # self.excel_file = excel_file
        self.row = row
    
    def getInfoAndScores(self, row) -> dict:
        # df = pd.read_excel(self.excel_file) 
        
        info = ["学生姓名",  "学生学号"]
        # for row in df.iterrows():  # 获取每行数据 
        student_score_dict = {} 
        
        # 获取学生信息
        student_info = row[1]
        for index in student_info.index:
            if index not in info:
                student_info = student_info.drop(index)
        
        student_info_dict = {}
        
        for index in student_info.index:
            student_info_dict[index] = student_info[index]
        
        # 获取成绩信息
        # score_data = row[1].drop("学生班级名称")
        # score_data = score_data.drop("学生上海市学籍号")
        # score_data = score_data.drop("学生身份证件号")
        
        score_data = row[1]
        
        labels = [ 
                "语文", 
                "数学", 
                "英语", 
                "道德与法治", 
                "科学", 
                "地理", 
                "历史", 
                "音乐", 
                "美术", 
                "体育与健身", 
                "探究", 
                "劳动技术", 
                "物理", 
                "化学", 
                "生物"
                "体育与健康"]
        for label in score_data.keys():
        # for label in data.keys():
            if label not in labels:
                score_data.drop(label)
        
        # for index in score_data.index:
        #     if index in info:
        #         score_data = score_data.drop(index)
        
        # 获得单个同学的所有成绩
        for index in score_data.index:
            student_score_dict[index] = score_data[index]
        
        return student_info_dict, student_score_dict
        # a = TableGenerator(student).getTable()
    
    def generateScoreTables(self):
        '''
        Generate a HTML table containing all course and its score of a single student
        output: [student's name, student's id, scores table]
        '''
        
        student_info = self.getInfoAndScores(self.row)[0]
        student_score = self.getInfoAndScores(self.row)[1]
        
        name = student_info["学生姓名"]
        studentid = student_info["学生学号"]
        
        score_table = TableGenerator(student_score).getTable()
        
        return name, studentid, score_table

    

#     student[stu_num] = data   # 存储每个学号及其相关标签数据

# print (students) # 输出查看结果