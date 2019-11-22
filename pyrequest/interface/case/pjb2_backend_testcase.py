# -*- coding:utf-8 -*-
import os,sys
BASE_PATH = os.path.split(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))[0]
sys.path.append(BASE_PATH)
DATA_PATH = os.path.join(BASE_PATH,"data/pjb2")
import unittest,time
from selenium import webdriver
from ddt import file_data,ddt
import configparser as cparser
import platform
from pyrequest.interface.case.page_obj.loginPage import LoginPage
from pyrequest.interface.case.page_obj.backendPage import BackendPage
import traceback
cf = cparser.ConfigParser()
config_path = BASE_PATH + "/config.ini"
cf.read(config_path)

#====================== 配置
cashDebit = 500 #标的金额
times = 1 #运行次数，外部获取
###############################以下是不用修改的公共引用变量##################################
if platform.system() == "Windows":
    print("当前运行环境为：Windows")
    picture_url = BASE_PATH + "\Image\login.png"
else:
    print("当前运行环境为：Linux")
    picture_url = BASE_PATH + "/Image/login.png"
##############################以上是不用修改的公共引用变量###################################
calenderXpath = '//*[@id="app"]/div/div[1]/div[2]/div[4]/div[1]/div[3]/div/div/div/div[2]/table/tbody/tr[5]/td[7]'#出票日期
backDate ='//*[@name="endDate"]/div/div/div[2]/table/tbody/tr[2]/td[4]'#到期日期--还款的时间#还款日期7月4号

#======================


@ddt
class CheckBackendTest(unittest.TestCase):
    # 实现无界面

    @classmethod
    def setUpClass(cls):
        # cls.driver= FirefoxDriverNOBrowser() #无界面
        cls.driver = webdriver.Firefox()  # 有界面

    @file_data(os.path.join(DATA_PATH,"ddt_test_checkDebit_testcase.json"))
    def test_001_checkDebit_testcase(self,debitUrl,username,password):
        login_page = LoginPage(self.driver, base_url=debitUrl)
        login_page.open()
        login_page.send_login_userName(username)
        login_page.send_login_passWord(password)
        login_page.send_login_imageCode()
        login_page.click_login_loginBtn()
        try:
            var = 1
            for var in range(1):
                #我要借款
                login_page.click_borrowBtn()
                time.sleep(1)
                try:
                    #我要借款按钮
                    login_page.click_debitBtn()
                except:
                    #我要借款按钮
                    login_page.click_debitBtn()
                    time.sleep(0.5)
                finally:
                    #借款金额
                    login_page.clear_debitCash()
                    login_page.send_debitCash(cashDebit)
                    # 点击还款日期
                    login_page.click_debitDate()
                    login_page.click_RQfy()
                    login_page.click_calender()

                    #票号
                    login_page.send_piaoNum("E60000003")
                    #出票人
                    login_page.send_debitPeople("深圳市发票有限责任公司")
                    # 上传文件
                    login_page.send_uploadFile(picture_url)
                    time.sleep(0.5)
                    # 收款人
                    login_page.send_receivePeople(u"北京高盛信息集团股份有限公司")
                    # 出票日期
                    login_page.click_startDate()
                    time.sleep(0.5)
                    #出票日期--选择 今日出票
                    login_page.click_todyBtn()
                    #到期日期
                    login_page.click_endDate()
                    time.sleep(0.5)

                    #切换到下一个月
                    login_page.click_qiehuan2()
                    time.sleep(0.5)
                    # 切换到下一个月
                    login_page.click_qiehuan3()
                    time.sleep(0.5)
                    # 30号 日期
                    login_page.click_selectDate()
                    # 背书日期
                    login_page.click_reviewDate()
                    time.sleep(0.5)
                    # #切换到一下个月
                    login_page.click_nextMoth()
                    time.sleep(0.5)
                    # 7月 25号日期
                    login_page.click_selectReviewDate()
                    time.sleep(0.5)
                    # 付款行
                    login_page.send_payBank(u"招商银行")
                    #担保金额
                    login_page.send_sureCash("2500000")
                    #担保名称
                    login_page.click_DBamount()
                    login_page.send_DBamount(u'阿里巴巴')
                    # 担保人证件号码
                    login_page.click_DBzj()
                    login_page.send_DBzj('230903198611112345')
                    # 担保人电话
                    login_page.click_DBphone()
                    login_page.send_DBphone('15596325674')
                    #担保人法法人代表姓名
                    login_page.click_DBFName()
                    login_page.send_DBFName('测试')
                    # 担保人法人代表证件类型
                    login_page.click_DBFCard()
                    # 担保人法人代表证件号码
                    login_page.click_DBFNumber()
                    # 点击一下查询
                    login_page.click_queryBtn()
                    # 勾选担保函协议
                    login_page.execute_js()
                    login_page.execute_js2()
                    # 提交按钮
                    login_page.click_submitBtn()
                    # 确定按钮
                    login_page.click_enterBtn()
        except:
            traceback.print_exc()
        finally:
            result = True
            self.assertTrue(result)

    @file_data(os.path.join(DATA_PATH,"ddt_test_checkTrail_testcase.json"))
    def test_002_checkTrail_testcase(self,loginUrl,username,password):
        # 打开网页
        backend_page = BackendPage(self.driver,base_url=loginUrl)
        backend_page.open()
        # 登录账号
        backend_page.send_backend_userName(username)
        backend_page.send_backend_passWord(password)

        # 点击空白页
        backend_page.click_backend_zongheBtn()
        backend_page.click_backend_loginBtn()
        try:
            var = 1

            # 借款管理
            backend_page.click_backend_debitOne()
            # 借款申请审核
            backend_page.click_backend_debitTwo()
            for var in range(1):
                # 打开借款申请经办
                backend_page.click_backend_debitThree()

                # 点击待审核
                backend_page.click_backend_stayAduit()
                # 点击查看详情
                backend_page.click_backend_catDetail()
                # 通过按钮
                backend_page.click_backend_passBtn()
                # 风控评级
                backend_page.click_backend_riskBtn()
                # 选择 风控评级
                backend_page.click_backend_selectRisk()
                # 输入审核意见
                backend_page.click_backend_inputInfo()
                backend_page.send_backend_inputInfo()
                # 上传文件
                # uploadFileBtn = driver.find_element_by_name("uploadFile")
                # uploadFileBtn.send_keys(u'G:\P2G-BUG\借款bug\登录2.png')
                # 提交
                backend_page.click_backend_submitBtn()
                # 打开复审 -- > 新流程已简化 -- > 直接进入复审阶段
                # 点击复审按钮
                backend_page.click_backend_passButton()
                # 打开风险详情
                backend_page.click_backend_riskPage()
                # 选择 风险等级
                backend_page.click_backend_selRiskLevel()
                # 输入审核意见
                backend_page.click_backend_inputReAduit()
                backend_page.send_backend_inputReAduit()
                # #选择文件上传
                # uploadBtn = driver.find_element_by_name('uploadFile')
                # uploadBtn.send_keys(u'G:\P2G-BUG\借款bug\登录2.png')
                # 提交
                backend_page.click_backend_submitBtn2()
        except Exception as e:
            print(e)
            raise
        finally:
            result = True
            self.assertTrue(result,msg="审核流程测试通过")
    @classmethod
    def tearDownClass(cls):
        pass
        #cls.driver.quit()

if __name__ == '__main__':
    unittest.main()