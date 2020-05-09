# 密码管理系统
# 需求：
# 1.随机生成密码；
# 2.添加已有密码
# 3.查看保存的密码；
# 4.修改已保存的密码；
# 5.删除保存的密码；
# 6.拷贝密码到剪贴板；
# 7.退出密码保管箱。
"""随机生成指定位数的密码，密码包含大、小写字母和数字"""


import random
import string
import re
import pyperclip
import os


# 定义一个密码类
class Password(object):
    def __init__(self, name, pwd):
        self.name = name
        self.pwd = pwd


# 定义一个密码管理系统类
class PasswordManagerSystem(object):
    # 给创建好的对象添加属性
    # 将所有密码都保存这个属性（列表）里。
    def __init__(self):
        self.pwd_list = list()

    @staticmethod
    def sys_menu():
        print("-" * 5, "欢迎使用密码保管箱 V1.1(对象版)", "-" * 5)
        print('1.随机生成密码')
        print('2.添加已有密码')
        print('3.查看保存的密码')
        print('4.修改已保存的密码')
        print('5.删除保存的密码')
        print('6.拷贝密码到剪贴板')
        print('7.退出密码保管箱')

    def pwd_write(self, pwd):
        # 将新生成的密码对象保存到管理系统类的属性（列表）里
        self.pwd_list.append(pwd)
        self.save_pwd()
        print("添加成功！")

    # 生成随机密码
    def password_new(self):
        while True:
            pwd_name = input("请输入需要生成的密码服务于：")
            # 确保输入了是哪儿的密码
            if not pwd_name:
                print('一定要确认这是哪儿的密码。')
                continue
            break

        # 生成密码的位数大于1
        while True:
            # 确保一定要设定密码长度，并且长度大于2位。
            try:
                self.len_pw = int(input("请确定需要生成新密码的位数："))
                if self.len_pw > 2:
                    break
            except Exception:
                print('别闹，你还不如不设密码。')
                continue

        while True:
            tmp = random.sample(string.ascii_letters + string.digits, self.len_pw)
            pwd_new = ''.join(tmp)
            if re.search('[0-9]', pwd_new) \
                    and re.search('[a-z]', pwd_new) \
                    and re.search('[A-Z]', pwd_new)\
                    and pwd_new[0] in string.ascii_uppercase:
                print("生成的密码是：", pwd_new)
                pyperclip.copy(pwd_new)
                break

        # 生成密码对象
        pwd = Password(pwd_name, pwd_new)

        self.pwd_write(pwd)

    # 添加一个已有的密码
    def password_old(self):
        # 一定要输入需要保存的密码信息
        while True:
            pwd_name = (input("请输入需要生成的密码服务于："))
            # 确保输入了是哪儿的密码
            if not pwd_name:
                print('一定要确认这是哪儿的密码。')
                continue
            break

        while True:
            pwd_old = input('请输入要保存的密码：')
            print('你输入的密码是：', pwd_old)
            ans = input("你确定密码输入正确了吗？（正确按'y'）")
            if ans == 'y':
                break

        # 定义密码对象类
        pwd = Password(pwd_name, pwd_old)

        self.pwd_write(pwd)

    # 显示所有密码
    def show_pwd(self):
        print('=' * 50)
        for index, password in enumerate(self.pwd_list):
            index += 1
            print('序号:{},{}，密码：{}'.format(index, password.name, password.pwd))
        print('=' * 50)
    # 保存密码信息到文件。

    def save_pwd(self):
        file = open(r'D:\Program Files\system.sys','w',encoding='utf-8')
        # 这里读出来的是对象的指引，关闭文件后会清空内存，指引变无效。
        # 所以要把密码对象的属性转换成字典保存；
        # 把密码对象列表转换成密码字典列表。
        result = [pwd.__dict__ for pwd in self.pwd_list]
        file.write(str(result))
        file.close()

    # 读取保存在文件中的信息
    def load_pwd(self):
        if os.path.exists(r'D:\Program Files\system.sys'):
            file = open(r'D:\Program Files\system.sys','r',encoding='utf-8')
            pl = file.read()
            new_list = [p for p in eval(pl)]
            # 把密码字典列表转成密码对象列表
            pwd = [Password(**my_dict) for my_dict in new_list]
            self.pwd_list.extend(pwd)
            file.close()

    # 将要复制的密码拷贝到剪贴板
    def pwd_copy(self):
        i = int(input('请选择要复制的密码：'))
        if 0 < i <= len(self.pwd_list):
            password = self.pwd_list[i - 1]
            # 读取要拷贝的密码
            pwd = password.pwd
            pyperclip.copy(pwd)
            print('已拷贝到剪贴板')

    # 修改已保存的密码
    def pwd_mod(self):
        i = int(input('请选择要修改的密码：'))
        index = i - 1
        # 判断下标是否合法
        if 0 <= index < len(self.pwd_list):
            password = self.pwd_list[index]
            pwd_new = input('请输入新的密码：')
            password.pwd = pwd_new
            print('序号{}，{}的密码已修改为{}。'.format(i, password.name, password.pwd))

    # 删除已保存的密码
    def pwd_del(self):
        i = int(input('请选择要删除的密码：'))
        index = i - 1
        # 判断下标是否合法
        if 0 < i <= len(self.pwd_list):
            # 提示是否删除该密码
            password = self.pwd_list[index]
            print('是否删除{}的密码？'.format(password.name))
            n = input("按'y'删除：")
            if n == 'y':
                password = self.pwd_list.pop(index)
                print('已删除{}的密码。'.format(password.name))

        self.show_pwd()

    # 程序主入口
    def start(self):
        # 读取以文本中的历史数据
        self.load_pwd()
        while True:
            # 开始运行程序
            self.sys_menu()
            choice = input('需要我做什么？：')
            if choice == '1':
                self.password_new()
            elif choice == '2':
                self.password_old()
            elif choice == '3':
                self.show_pwd()
            elif choice == '4':
                self.pwd_mod()
            elif choice == '5':
                self.pwd_del()
            elif choice == '6':
                self.pwd_copy()
            elif choice == '7':
                self.save_pwd()
                break
            else:
                print('输入不合法，Once more!')
                continue

if __name__ == "__main__":
    soft = PasswordManagerSystem()
    soft.start()
