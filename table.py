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
        
    def checkTableLength(table):
        num_cols = len(table.split('<th>')) - 1

        if num_cols > 6:
            # Split table into multiple tables
            tables = []
            for i in range(0, num_cols, 6):
                tables.append(table[:table.find('</tr>')+5] + '\n')
                table = table[table.find('</tr>')+5:]

                for j in range(i, min(i+6, num_cols)):
                    tables[-1] += matches[j] + '\n'

                tables[-1] += '</tr>\n</table>'

            # Return list of tables
            return ''.join(tables)

        else:
            return table
    
    def center_text_in_table(html_table):
        soup = BeautifulSoup(html_table, 'html.parser')
        td_list = soup.find_all('td')
        for td in td_list:
            td['style'] = 'text-align:center'
        return soup.prettify()
    # print(center_text_in_table('<table> <tr> <td>语文</td> <td>数学</td> <td>英语</td> <td>道德与法治</td> <td>科学</td> <td>地理</td> <td>历史</td> </tr> <tr> <td>优秀</td> <td>合格</td> <td>优秀</td> <td>优秀</td> <td>良好</td> <td>优秀</td> <td>优秀</td> </tr> </table>'))
    
    def bold_text_in_first_row(html_table):
        soup = BeautifulSoup(html_table, 'html.parser')
        first_row_tds = soup.find_all('tr')[0]('td')
        for td in first_row_tds:
            td['style'] = 'font-weight:bold'
        return soup.prettify()
        # print(bold_text_in_first_row('<table> <tr> <td>语文</td> <td>数学</td> <td>英语</td> <td>道德与法治</td> <td>科学</td> <td>地理</td> <td>历史</td> </tr> <tr> <td>优秀</td> <td>合格</td> <td>优秀</td> <td>优秀</td> <td>良好</td> <td>优秀</td> <td>优秀</td> </tr> </table>') )
        
    def projection_effect(table):
        table.style.background_gradient(cmap='Greys')
        table.style.set_properties(**{'border-collapse': 'collapse'})
        table.style.set_properties(**{'border': '2px solid black'})
        
        return table
    
    def getTable(self):
        return self.table

# # print(html)
# a = TableGenerator(testdict).getTable()
# print(a)