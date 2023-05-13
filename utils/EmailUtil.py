import os
import datetime
import yaml
from email.mime.text import MIMEText
import  smtplib
from email.mime.multipart import MIMEMultipart
from email.header import Header

#初始化
#smtp地址，用户名，密码，接收邮件者，邮件标题，邮件内容，邮件附件
class SendEmail:
    def __init__(self,smtp_addr,username,password,send,recv,
                 title,msg_from,content=None,reportfile=None):
        self.smtp_addr = smtp_addr
        self.username = username
        self.password = password
        self.send=send
        self.recv = recv
        self.title = title
        self.msg_from=msg_from
        self.content = content
        self.reportfile = reportfile
#发送邮件方法
    def send_email(self):
        file_name = self.reportfile.split("\\")[-1]
        with open(self.reportfile, "rb") as f:
            mail_body = f.read()
        now = datetime.datetime.now().strftime("%Y-%m-%d %H%M%S")
        # 邮箱发送的服务器、邮箱账号密码、发送人、收件人、主题
        smtpserver = self.smtp_addr
        user = self.username
        password = self.password
        sender = self.send
        receiver = self.recv
        subject = self.title + now

        # 邮件类型
        msg = MIMEMultipart('mixed')

        # 添加邮件正文到msg对象
        msg_html1 = MIMEText(mail_body, 'html', 'utf-8')
        msg.attach(msg_html1)
        # 添加邮件附件到msg对象
        msg_html2 = MIMEText(mail_body, 'html', 'utf-8')
        msg_html2.add_header("Content-Disposition", "attachment", filename=("utf-8", "", file_name))
        # msg_html2['Content-Type'] = 'application/octet-stream'
        # msg_html2['Content-Disposition'] = "attachment; filename='%s'"%(reportfile)
        msg.attach(msg_html2)
        # 将发送人添加到msg对象
        msg['From'] = self.msg_from
        # 将收件人添加到msg对象
        msg['To'] = ";".join(receiver)
        # msg['Date'] = '2021-7-18'
        # 将主题添加到msg对象
        msg['Subject'] = Header(subject, 'utf-8')

        # 连接发送邮件
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver, 25)
        smtp.login(user, password)
        smtp.sendmail(sender, receiver, msg.as_string())
        smtp.quit()


