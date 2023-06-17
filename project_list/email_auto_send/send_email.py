import win32com.client
from flask import render_template

# 自动群发邮件
def send_group_mail():
    outlook = win32com.client.Dispatch("Outlook.Application")
    # 创建一个邮件对象
    mail = outlook.CreateItem(0)
    # 对邮件的各个属性进行赋值
    mail.To = "jason.lin@pteamtech.com"  # 收件邮箱列表,如多人用;隔开
    mail.Subject = "品大科技_新年快樂"
    mail.BodyFormat = 2  # 2: Html format
    # mail.Body = "邮件正文"  # 如不需要HTML格式使用
    # 添加多个附件
    mail.Attachments.Add(r"C:\Users\User\pteam0118.jpg")
    # mail.Attachments.Add("附件2绝对路径")...
    mail.HTMLBody = """
    <body>
    Dear 林先生<br><br>
    嶄新的一年期待與您共同再創佳績!<br>
    🧨品大科技 恭祝大家🧨<br>
    兔年好運到 鴻兔大展一整年！<br><br>
    <font color="#C21C0A">🐰【2023玉兔迎新年 農曆春節假期】🐰</font><br>
    🧧1/20 至1/29 休假<br>
    🧧1/30 開市大吉<br><br>
    

    <div><img src="pteam0118.jpg" width="500" height="500"></div><br>
    <font color="#FF5809">
    林孟達/ Jason Lin<br>
    P-Team Technology Inc. 品大科技有限公司<br>
    Skype: live:fa52e5450fa6afa7<br>
    Website: https://www.pteamtech.com/<br>
    22175新北市汐止區新台五路一段93號28樓 (遠雄D棟)<br>
    TEL: +886-2-26975001 #2027  FAX: +886-2-26975575<br>
    <font color="#C21C0A">
    </body>"""
    
    # 邮件发送
    mail.Send()


if __name__ == '__main__':
    send_group_mail()
    print(123)