# # The data to render in the template
# testdict = {
#     1: 0,
#     2: 0,
#     3: 0,
#     4: 0,
#     5: 0
# }

class TableGenerator:
    def __init__(self, my_dict):
        self.my_dict = my_dict
        
        self.table = self.generateTable()
        # return table
        
    def getDict(self):
        return self.my_dict

    def makeHeaderRow(self,keys):
        html = "<tr>\n"
        for key in keys:
            html += "<td>{}</td>\n".format(key)
        html += "</tr>\n"
        return html

    def makeDataRow(self,values):
        html = "<tr>\n"
        for value in values:
            html += "<td>{}</td>\n".format(value)
        html += "</tr>\n"
        return html

    def generateTable(self):
        # mydict = self.getDict()
        
        html = "<table>\n"
        html += self.makeHeaderRow(self.my_dict.keys())
        html += self.makeDataRow(self.my_dict.values())
        html += "</table>\n"
        
        return html
    
    def getTable(self):
        return self.table

# # print(html)
# a = TableGenerator(testdict).getTable()
# print(a)