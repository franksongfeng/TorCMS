# -*- coding: utf-8

'''
发送Email的脚本
'''
from config import SMTP_CFG, email_cfg
from torcms.core.tool.send_email import send_mail
from torcms.model.user_model import MUser


def run_send_all(*args):
    '''
    Send email to all user.
    '''
    for user_rec in MUser.query_all():
        email_add = user_rec.user_email
        send_mail(
            [email_add],
            f"{SMTP_CFG['name']}|{email_cfg['title']}",
            email_cfg['content'],
        )


def run_send_nologin(*args):
    '''
    Send email to who not logged in recently.
    '''
    for user_rec in MUser.query_nologin():
        email_add = user_rec.user_email
        print(email_add)
        send_mail(
            [email_add],
            f"{SMTP_CFG['name']}|{email_cfg['title']}",
            email_cfg['content'],
        )
        MUser.set_sendemail_time(user_rec.uid)
