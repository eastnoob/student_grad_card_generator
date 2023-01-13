import os

class MarkDownPPT:
    theme = 'default'
    bg_imag = ''
    bg_opacity = '100'
    
    markdown_path = 'markdowns'
    export_path = 'final_pdfs'
    
    def __init__(self, stu_name, stu_id, score_table, comment) -> None:
        
        self.stu_name = stu_name
        self.stu_id = stu_id
        self.score_table = score_table
        self.comment = comment
        
        self.marp_file = self.marpInit() # 一个markdown文件
    
    def marpInit(self):
        init_text = '---\nmarp: true\ntheme: default\n---\n\n'
        filename = self.stu_id + self.stu_name + '.md'

        # Check if the file exists
        if os.path.exists(filename):
            # Delete the file if it exists
            os.remove(filename)

        # Create a new file
        # Use with statement to open and write to the file
        with open(filename, "w") as f:
            # Add content to the file
            f.write(init_text)
        
        return filename
    def generateScorePage(self):
        with open(self.stu_id + self.stu_name, 'a+') as f:
            f.write('# 七年级上-第一学期期末成绩单' + '\n')

            f.write('学生姓名：' + self.stu_name + '\n')
            f.write('学生学号：' + self.stu_id + '\n')
            
            f.write(self.score_table + '\n')
            
            f.write('--- \n')