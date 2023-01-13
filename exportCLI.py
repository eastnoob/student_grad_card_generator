import os

class ExportPDf:
    
    def __init__(self, file_path:str, file_name:str) -> None:
        self.file_name = file_name
        
        # 读取文件路径
        self.file_path = file_path
        while True:
            with open(self.file_path) as f:
                path = f.read().strip()
            # 检查目录是否存在
            if os.path.exists(path):
                break
            else:
                # 提示输入有效路径
                if input("请输入一个有效路径: ") == '':
                    continue
    
    def exportPDF(self):
        # # 构建命令，并执行
        # change path = 'start "" "{}"'.format(path)
        # os.system(command_string)

        # 执行命令
        markdown_path = "\markdowns"
        os.system(f"cd {markdown_path}")
        
        command_string = f'npx @marp-team/marp-cli@latest {self.file_name}.md -o final_pdfs\\{self.file_name}.pdf'
        os.system(command_string)
        os.wait()
        
        print(f"{self.name} 完成")

        # a = "npx @marp-team/marp-cli@latest --html --pdf .\{slide-deck}.md -o final_pdfs\output.pdf"

        # os.system('exit')
        # os.wait()