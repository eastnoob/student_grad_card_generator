import os

class MarkDownPPT:
    theme = 'default'
    bg_imag = ''
    bg_opacity = '100'
    
    markdown_path = 'markdowns'
    export_path = 'final_pdfs'
    
    def __init__(self, stu_name, stu_id, score_table, comment:str) -> None:
        
        '''
        最后参数comment接收字符串
        '''
        
        self.stu_name = stu_name
        self.stu_id = str(stu_id)
        self.score_table = score_table
        self.comment = comment
        
        self.file_name = self.stu_id + self.stu_name
        self.file_path = 'markdowns\\' + self.file_name + '.md'
        
        # self.marp_file = self.marpInit() # 一个markdown文件
    
    def marpInit(self):
        init_text = '---\nmarp: true\ntheme: default\n---\n\n\n'

        # Check if the file exists
        if os.path.exists(self.file_path):
            # Delete the file if it exists
            os.remove(self.file_path)

        # Create a new file
        # Use with statement to open and write to the file
        with open(self.file_path, "w", encoding="utf-8") as f:
            
            # Add content to the file
            f.write(init_text)
    
    def generateScorePage(self):
        with open(self.file_path, 'a+', encoding="utf-8") as f:
            f.write('![bg opacity:.40](bg6.png)' + '\n')
            
            f.write('# 七年级上 第一学期期末成绩单' + '\n')

            f.write('* **' + '<p align="left">学生姓名：' + self.stu_name + '**' + '\n')
            f.write('* **' + '<p align="left">学生学号：' + self.stu_id + '**' + '\n')
            
            f.write(self.score_table + '\n')
            
            f.write('--- \n')
    
    def generateCommentPage(self):
        with open(self.file_path, 'a+', encoding="utf-8") as f:
            f.write('![bg opacity:.40](bg6.png)' + '\n')
            f.write('# 成长寄语 \n')
            f.write(self.comment)
    
    def generateMarkdownFile(self):
        self.marpInit()
        self.generateScorePage()
        self.generateCommentPage()
    
    def getFileName(self):
        return self.file_name
    
    def getFilePath(self):
        return self.file_path

