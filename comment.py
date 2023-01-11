class Comment():

    def __init__(self, name: str, 
                    comment: str, 
                    teacher: str) -> str:
        
        self.name = name
        self.comment = comment
        self.teacher = teacher
        # self.time = time
        self.result = self.joinComment()
        
        # return joint
        
    def getTime(self):
        year = input("请输入年：")
        month = input("请输入月：")
        day = input("请输入日：")
        
        time = year + "年" + month + "月" + day + "日"
        
        print("请确认日期是否正确：Y/N： " + time)
        
        return time


    def joinComment(self) -> str:
        time = self.getTime()
        
        joint_result = ""
        joint_result += self.name + ": \n" + "  " + self.comment + self.teacher + "\n" + "<p align=\"right\">" + time + "</p>"

        return joint_result



