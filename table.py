# # The data to render in the template
# testdict = {
#     1: 0,
#     2: 0,
#     3: 0,
#     4: 0,
#     5: 0
# }

from bs4 import BeautifulSoup
import re

class TableGenerator:
    def __init__(self, my_dict):
        self.my_dict = my_dict
        
        self.table = self.generateTable()
        self.final_table = self.adjestTable(self.table)
        # return table
        
    def getDict(self):
        return self.my_dict

    def makeHeaderRow(self,keys):
        html = "<tr>\n"
        for key in keys:
            html += "<th>{}</th>\n".format(key)
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
    
    #================================================================================
    def creatTable(self, table_labels, table_datas):
        try:
            table_creator = BeautifulSoup()
        except NameError:
            from bs4 import BeautifulSoup
        
        table_creator = BeautifulSoup()
        table = table_creator.new_tag('table')
        table['style'] = 'margin: 0 auto;'# 居中显示
        
        # 前半部分
        table_label_elem = table_creator.new_tag('tr')

        for label in table_labels:
            table_label_elem.append(label)
            table_label_elem.append('\n')
        table.append(table_label_elem)

        # 后半部分
        table_data_elem = table_creator.new_tag('tr')

        for data in table_datas:
            table_data_elem.append(data)
            table_data_elem.append('\n')
        table.append(table_data_elem)
        
        return table.prettify()
    #================================================================================
    
    def split_table(self, html_doc):
        
        # 使用BeautifulSoup处理HTML文档
        soup = BeautifulSoup(html_doc, 'html.parser')
        
        # 查找表格标签
        table = soup.find('table')

        # 判断表格的长度
        labels = table.find_all('th')
        datas = table.find_all('td')
        # print(labels)
        lenth = len(labels)
        
        if lenth <= 6:
            return soup
        else:
            table_creator = BeautifulSoup()
            
            # 拆分表格
            table1_labels = labels[:6]
            table1_datas = datas[:6]
            
            table2_labels = labels[6:]
            table2_datas = datas[6:]
            
            table1 = self.creatTable(table1_labels, table1_datas)
            table2 = self.creatTable(table2_labels, table2_datas)
            
            combined_table = table1 +'\n' + table2
            
            # print(combined_table)
            
            # soup = BeautifulSoup(combined_table, 'html.parser') 
            # final_table = soup.find("table")
            final_table = BeautifulSoup(combined_table, 'html.parser') 
            
            
            for row in final_table.find_all('tr'): 
                for cell in row.find_all('td'):
                    cell['style'] = 'width:150px'
                for cell in row.find_all('th'):
                    cell['style'] = 'width:150px'
            final_table.append('\n')
            
            
            return final_table
    

    
    def center_text_in_table(self, html_table):
        # soup = BeautifulSoup(html_table, 'html.parser')
        td_list = html_table.find_all('td')
        for td in td_list:
            td['style'] = 'text-align:center'
            
        return html_table.prettify()
        return html_table

    # print(center_text_in_table('<table> <tr> <td>语文</td> <td>数学</td> <td>英语</td> <td>道德与法治</td> <td>科学</td> <td>地理</td> <td>历史</td> </tr> <tr> <td>优秀</td> <td>合格</td> <td>优秀</td> <td>优秀</td> <td>良好</td> <td>优秀</td> <td>优秀</td> </tr> </table>'))
    '''
    def bold_text_in_first_row(html_table):
        soup = BeautifulSoup(html_table, 'html.parser')
        first_row_tds = soup.find_all('tr')[0]('td')
        for td in first_row_tds:
            td['style'] = 'font-weight:bold'
        return soup.prettify()
        # print(bold_text_in_first_row('<table> <tr> <td>语文</td> <td>数学</td> <td>英语</td> <td>道德与法治</td> <td>科学</td> <td>地理</td> <td>历史</td> </tr> <tr> <td>优秀</td> <td>合格</td> <td>优秀</td> <td>优秀</td> <td>良好</td> <td>优秀</td> <td>优秀</td> </tr> </table>') )
    '''
    
    def projection_effect(self, table):
        table.style.background_gradient(cmap='Greys')
        table.style.set_properties(**{'border-collapse': 'collapse'})
        table.style.set_properties(**{'border': '2px solid black'})
        
        return table.prettify()
    
    def center_the_table(self, soup):
        # soup = BeautifulSoup(table, 'html.parser')
        
        # Find the table and store in a variable
        # table_list = soup.find_all('table')
        for table in soup.find_all('table'):
            table['style'] = "margin: 0 auto;"

        # Add the CSS code to center the table
        
        return table.prettify()
    
    def adjestTable(self, table):
        splited_table = self.split_table(table)
        center_text_table = self.center_text_in_table(splited_table)
        # projected_table = self.projection_effect(center_text_table)
        # center_table = self.center_the_table(center_text_table)
        
        return center_text_table
    
    def getTable(self):
        return self.final_table

# # print(html)
# a = TableGenerator(testdict).getTable()
# print(a)