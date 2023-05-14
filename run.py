import os
import pytest
from common import Base
from config import Conf
from utils.EmailUtil import SendEmail


if __name__ == '__main__':
    '''
    二选一pytest原生生成报告或allure生成报告
    '''
    #pytest生成的邮箱报告
    # pytest.main()
    # report_path =Conf.get_report_path()
    # report_path = os.path.join(report_path,"report.html")

    #allure生成的邮箱报告
    report_path = Conf.get_report_path()+os.sep+"result"
    report_html_path = Conf.get_report_path()+os.sep+"html"
    pytest.main(["--alluredir",report_path])
    Base.allure_report(report_path,report_html_path)

    #发送邮件
    # con_info = Conf.ConfigYaml()
    # email_info = con_info.get_email_info()
    # smtp_addr = email_info["smtpserver"]
    # username = email_info["username"]
    # password = email_info["password"]
    # sender =  email_info["sender"]
    # recv = email_info["receiver"]
    # subject = email_info["subject"]
    # msg_from = email_info["msg_from"]
    # email = SendEmail(smtp_addr,username,password,sender,recv,subject,msg_from,reportfile=report_path)
    # email.send_email()


