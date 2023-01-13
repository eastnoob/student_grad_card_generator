class Comment():

    def __init__(self, name: str, 
                    comment: str, 
                    teacher: str,
                    year: str,
                    month: str,
                    day: str) -> None:
        
        self.name = name
        self.comment = comment
        self.teacher = teacher
        self.time = str(year) + "年" + str(month) + "月" + str(day) + "日"
        
        # self.final_comment = self.joinComment()
        
        # return joint
        
    # def getTime(self):
    #     year = input("请输入年：")
    #     month = input("请输入月：")
    #     day = input("请输入日：")
        
    #     time = year + "年" + month + "月" + day + "日"
        
    #     print("请确认日期是否正确：Y/N： " + time)
        
    #     return time


    def joinComment(self) -> str:
        # time = self.getTime()
        
        # joint_result = ""
        
        head = "<body>" + self.name + "同学: " + "</body>" + "\n"
        body_style = "<style>" + "p {text-indent:1em;}" + "</style>" + "\n"
        body = "<p>" + self.comment + "\n\n"
        tail = "<p align=\"right\">" + self.teacher + "</p>" + "\n" + "<p align=\"right\">" + self.time + "</p>"
        
        
        joint_result = head + body_style + body + tail
        return joint_result
    
    def getComment(self) -> str:
        # '''
        # Generate a dict which contained student's name and its common
        # ourput: {student's nmae: connent of this student}
        # '''
        
        final_comment = self.joinComment()
        return final_comment
        
        # nameWithComment = {self.name: final_comment}
        
        # return nameWithComment



