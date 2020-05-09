# 密码管理系统
# 需求：
# 1.随机生成密码；
# 2.查看保存的密码；
# 3.取出密码（将密码复制到剪贴板）；
# 4.退出。
"""随机生成指定位数的密码，密码包含大、小写字母和数字"""
import random
import string
import re
import pyperclip
import os

# 将所有密码都保存这个列表里。
pwd_list = list()


def menu():
    print("-" * 5, "欢迎使用密码保管箱 V1.1", "-" * 5)
    print('1.随机生成密码')
    print('2.添加已有密码')
    print('3.查看保存的密码')
    print('4.修改已保存的密码')
    print('5.删除保存的密码')
    print('6.拷贝密码到剪贴板')
    print('7.退出密码保管箱')


# 将新生成的密码以字典类型保存到密码列表里
def pwd_write(pwd_name, pwd):
    pwd_dict = dict()
    pwd_dict['name'] = pwd_name
    pwd_dict['password'] = pwd
    pwd_list.append(pwd_dict)
    save_pwd()
    print("添加成功！")


# 生成新的密码
def pass_word_new():
    while True:
        pwd_name = input("请输入需要生成的密码服务于：")
        # 确保输入了是哪儿的密码
        if not pwd_name:
            print('一定要确认这是哪儿的密码。')
            continue
        break

    #生成密码的位数大于12
    while True:
        # 确保一定要设定密码长度，并且长度大于2位。
        len_pw = input("请确定需要生成新密码的位数：")
        if len_pw.isdigit() and int(len_pw) > 2:
            break
        print('别闹，你还不如不设密码。')
        continue

    while True:
        tmp = random.sample(string.ascii_letters + string.digits, int(len_pw))
        pwd = ''.join(tmp)
        if re.search('[0-9]', pwd) \
                and re.search('[a-z]', pwd) \
                and re.search('[A-Z]',pwd)\
                and pwd[0] in string.ascii_uppercase:
            print("生成的密码是：", pwd)
            pyperclip.copy(pwd)
            break

    pwd_write(pwd_name, pwd)


def pass_word_old():
    pwd_name = (input("请输入需要生成的密码服务于："))
    pwd= input('请输入要保存的密码：')

    pwd_write(pwd_name, pwd)


# 显示所有密码
def show_pwd():
    print('=' * 50)
    for index, pwd_dict in enumerate(pwd_list):
        index += 1
        print('序号:{},{}，密码：{}'.format(index, pwd_dict['name'], pwd_dict['password']))
    print('=' * 50)
# 保存密码信息到文件。


def save_pwd():
    file = open(r'C:\Program Files\system.sys','w',encoding='utf-8')
    result = str(pwd_list)
    file.write(result)
    file.close()


# 读取保存在文件中的信息
def load_pwd():
    if os.path.exists(r'C:\Program Files\system.sys'):
        file = open(r'C:\Program Files\system.sys','r',encoding='utf-8')
        pl = file.read()
        new_list = eval(pl)
        pwd_list.extend(new_list)
        file.close()


# 将要复制的密码拷贝到剪贴板
def pwd_copy():
    i = int(input('请选择要复制的密码：'))
    if 0 < i <= len(pwd_list):
        pwd_dict = pwd_list[i - 1]
        # 读取要拷贝的密码
        pwd = pwd_dict['password']
        pyperclip.copy(pwd)
        print('已拷贝到剪贴板')

# 修改已保存的密码
def pwd_mod():
    i = int(input('请选择要修改的密码：'))
    index = i - 1
    # 判断下标是否合法
    if 0 <= index < len(pwd_list):
        pwd_dict = pwd_list[index]
        pwd_new = input('请输入新的密码：')
        pwd_dict['password'] = pwd_new
        print('序号{}，{}的密码已修改为{}。'.format(i,
                                         pwd_dict['name'],
                                         pwd_dict['password']))


# 删除已保存的密码
def pwd_del():
    i = int(input('请选择要删除的密码：'))
    index = i - 1
    # 判断下标是否合法
    if 0 < i <= len(pwd_list):
        # 提示是否删除该密码
        pwd_dict = pwd_list[index]
        print('是否删除{}的密码？'.format(pwd_dict['name']))
        n = input("按'y'删除：")
        if n == 'y':
            pwd_del = pwd_list.pop(index)
            print('已删除{}的密码。'.format(pwd_del['name']))

    show_pwd()


# 程序主入口
def start():
    # 读取以文本中的历史数据
    load_pwd()
    while True:
        # 开始运行程序
        menu()
        choice = int(input('需要我做什么？：'))
        if choice == 1:
            pass_word_new()
        elif choice == 2:
            pass_word_old()
        elif choice == 3:
            show_pwd()
        elif choice == 4:
            pwd_mod()
        elif choice == 5:
            pwd_del()
        elif choice == 6:
            pwd_copy()
        elif choice == 7:
            save_pwd()
            break
        else:
            print('输入不合法，Once more!')
            continue

if __name__ == "__main__":
    start()





