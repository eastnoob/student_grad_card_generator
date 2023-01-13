import os
import subprocess
import time

class ExportPDf:
    
    def __init__(self, file_path:str, file_name:str) -> None:
        self.file_name = file_name
        
        # 读取文件路径
        self.file_path = file_path
        # while True:
        #     path = f.read().strip()
        #     if os.path.exists(path):
        #         break
        #     with open(self.file_path) as f:
        
        #     # 检查目录是否存在
        #     else:
        #         # 提示输入有效路径
        #         if input("请输入一个有效路径: ") == '':
        #             continue
    # '''
    def exportPDF(self):
        # # 构建命令，并执行
        # change path = 'start "" "{}"'.format(path)
        # os.system(command_string)

        # # 执行命令
        # markdown_path = "\markdowns"
        # os.system(f"cd {markdown_path}")
        
        command_string = f'npx @marp-team/marp-cli@latest --html --pdf {self.file_path} -o final_pdfs\\{self.file_name}.pdf'
        os.system(command_string)
        # subprocess.call(command_string)
        # os.wait()
        

        
        print(f"{self.file_name} 完成")

        # a = "npx @marp-team/marp-cli@latest --html --pdf .\{slide-deck}.md -o final_pdfs\output.pdf"

        # os.system('exit')
        # os.wait()
    # '''

        
        
    '''
    def exportPdf(self):
        if os.path.exists(f"final_pdf\\{self.file_name}.pdf"):
            os.remove(f"final_pdf\\{self.file_name}.pdf")
        process = subprocess.Popen(["npx", "@marp-team/marp-cli@latest", self.file_path, "-o", f"final_pdf\\{self.file_name}.pdf"])
        process.wait()
    
    '''


        
        # export_pdf("markdown/x.md")