from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from .base import Page
import time


class LoginPage(Page):
    """
    用户登陆页面
    """

    #页面路径
    url = "/debit/signin/"
    # 用户名
    login_userName_loc = (By.XPATH,'//*[@id="app"]/div/div[1]/div[2]/div/div/div[1]/input')
    # 密码
    login_passWord_loc = (By.XPATH,'//*[@id="app"]/div/div[1]/div[2]/div/div/div[3]/input')
    # 图片验证码
    login_imageCode_loc = (By.XPATH,'//*[@id="app"]/div/div[1]/div[2]/div/div/div[5]/input')
    # 登陆
    login_loginBtn_loc = (By.XPATH,'//*[@id="app"]/div/div[1]/div[2]/div/div/div[7]')

    def send_login_userName(self,username):
        self.find_element(*self.login_userName_loc).send_keys(username)

    def send_login_passWord(self,password):
        self.find_element(*self.login_passWord_loc).send_keys(password)

    def send_login_imageCode(self,imagecode="111111"):
        self.find_element(*self.login_imageCode_loc).send_keys(imagecode)

    def click_login_loginBtn(self):
        self.find_element(*self.login_loginBtn_loc).click()



    # 我要借款 按钮
    borrowButton_loc = (By.XPATH,'//*[@id="app"]/div/div[1]/div[1]/div[2]/div/div[2]/a[2]')

    def click_borrowBtn(self):
        self.find_element(*self.borrowButton_loc).click()


    # 我要借款按钮
    debitBtn_loc = (By.XPATH,'//*[@id="app"]/div/div[1]/div[1]/div[2]/div/div[2]/a[2]')

    def click_debitBtn(self):
        self.find_element(*self.debitBtn_loc).click()


    # 借款金额
    debitCash_loc = (By.NAME,"loanAmt")
    def send_debitCash(self,cashDebit):
        self.find_element(*self.debitCash_loc).send_keys(cashDebit)

    def clear_debitCash(self):
        self.find_element(*self.debitCash_loc).clear()

    # 点击还款日期
    debitDate_loc = (By.XPATH,'//*[@id="app"]/div/div[1]/div[2]/div[4]/div[1]/div[3]/div/input')
    def click_debitDate(self):
        self.find_element(*self.debitDate_loc).click()

    # 日期翻页
    RQfy_loc = (By.XPATH,'//*[@id="app"]/div/div[1]/div[2]/div[4]/div[1]/div[3]/div/div/div/div[1]/a[4]')
    def click_RQfy(self):
        self.find_element(*self.RQfy_loc).click()

    # 日历
    calender_loc = (By.XPATH,'//*[@id="app"]/div/div[1]/div[2]/div[4]/div[1]/div[3]/div/div/div/div[2]/table/tbody/tr[5]/td[7]')
    def click_calender(self):
        self.find_element(*self.calender_loc).click()

    def send_calender(self,calender):
        self.find_element(*self.calender_loc).send_keys(calender)

    # 票号
    piaoNum_loc = (By.NAME,'billNo')
    def click_piaoNum(self):
        self.find_element(*self.piaoNum_loc).click()

    def send_piaoNum(self,piaoNum):
        self.find_element(*self.piaoNum_loc).send_keys(piaoNum)

    # 出票人
    debitPeople_loc = (By.NAME,'borrower')
    def click_debitPeople(self):
        self.find_element(*self.debitPeople_loc).click()

    def send_debitPeople(self,debitPeople="深圳市发票有限责任公司"):
        self.find_element(*self.debitPeople_loc).send_keys(debitPeople)

    # 上传文件      #对于两个id一样的元素用一下方法定位，加上索引，用elements
    uploadFile_loc = (By.ID,'uploadFile')
    def send_uploadFile(self,picture_url):
        self.find_elements(*self.uploadFile_loc)[1].send_keys(picture_url)

    def click_uploadFile(self):
        self.find_elements(*self.uploadFile_loc)[1].click()

    # 收款人
    receivePeople_loc = (By.NAME,'beneficiary')
    def send_receivePeople(self,receiverPeople="北京高盛信息集团股份有限公司"):
        self.find_element(*self.receivePeople_loc).send_keys(receiverPeople)

    def click_receivePeople(self):
        self.find_element(*self.receivePeople_loc).click()

    # 出票日期
    startDate_loc = (By.NAME,'startDate')
    def click_startDate(self):
        self.find_element(*self.startDate_loc).click()

    # 出票日期--选择 今日出票
    todayBtn_loc = (By.NAME,'date')
    def click_todyBtn(self):
        self.find_element(*self.todayBtn_loc).click()

    # 到期日期
    endDate_loc = (By.NAME,'endDate')
    def click_endDate(self):
        self.find_element(*self.endDate_loc).click()

    # 切换到下一个月
    qiehuan2_loc = (By.XPATH,'//div[@class="mx-datepicker date-select"and @name="endDate"]//a[@class="mx-calendar__next-icon"][2]')
    def click_qiehuan2(self):
        self.find_element(*self.qiehuan2_loc).click()

    # 切换到下一个月
    qiehuan3_loc = (By.XPATH,'//div[@class="mx-datepicker date-select"and @name="endDate"]//a[@class="mx-calendar__next-icon"][2]')
    def click_qiehuan3(self):
        self.find_element(*self.qiehuan3_loc).click()

    # 30号 日期
    selectDate_loc =(By.XPATH,'//*[@name="endDate"]/div/div/div[2]/table/tbody/tr[2]/td[4]')
    def click_selectDate(self):
        self.find_element_wait(*self.selectDate_loc)

    #  背书日期
    reviewDate_loc = (By.NAME,'endorsementDate')
    def click_reviewDate(self):
        self.find_element(*self.reviewDate_loc).click()

    # 切换到下一月
    nextMoth_loc = (By.XPATH,'//*[@id="app"]/div/div[1]/div[2]/div[4]/div[1]/div[10]/table/tr[6]/td[2]/div/div/div/div[1]/a[4]')
    def click_nextMoth(self):
        self.find_element(*self.nextMoth_loc).click()

    # 7月 25号日期
    selectReviewDate_loc = (By.XPATH,'//*[@id="app"]/div/div[1]/div[2]/div[4]/div[1]/div[10]/table/tr[6]/td[2]/div/div/div/div[2]/table/tbody/tr[2]/td[4]')
    def click_selectReviewDate(self):
        self.find_element(*self.selectReviewDate_loc).click()

    # 付款行
    payBank_loc =(By.NAME,'creator')
    def send_payBank(self,bankName="招商银行"):
        self.find_element(*self.payBank_loc).send_keys(bankName)

    def click_payBank(self):
        self.find_element(*self.payBank_loc).click()

    # 担保金额
    sureCash_loc =(By.NAME,'guatantyAmt')
    def send_sureCash(self,guatantyAmt="2500000"):
        self.find_element(*self.sureCash_loc).send_keys(guatantyAmt)

    def click_sureCash(self):
        self.find_element(*self.sureCash_loc).click()

    # 担保名称
    DBamount_loc = (By.NAME,'securityName')
    def send_DBamount(self,securityName="阿里巴巴"):
        self.find_element(*self.DBamount_loc).send_keys(securityName)

    def click_DBamount(self):
        self.find_element(*self.DBamount_loc).click()

    # 担保人证件号码
    DBzj_loc = (By.NAME,"idNo")
    def send_DBzj(self,idNo="230903198611112345"):
        self.find_element(*self.DBzj_loc).send_keys(idNo)

    def click_DBzj(self):
        self.find_element(*self.DBzj_loc).click()

    # 担保人电话
    DBphone_loc = (By.NAME,'mobilePhone')
    def send_DBphone(self,mobilePhone="15596325674"):
        self.find_element(*self.DBphone_loc).send_keys(mobilePhone)

    def click_DBphone(self):
        self.find_element(*self.DBphone_loc).click()

    # 担保人法人代表姓名
    DBFName_loc = (By.NAME,'securityLegalName')
    def send_DBFName(self,securityLegalName="测试"):
        self.find_element(*self.DBFName_loc).send_keys(securityLegalName)

    def click_DBFName(self):
        self.find_element(*self.DBFName_loc).click()

    # 担保人法人代表证件类型
    DBFCard_loc = (By.NAME,'securityLegalIdType')
    def send_DBFCard(self,securityLegalIdType):
        self.find_element(*self.DBFCard_loc).send_keys(securityLegalIdType)

    def click_DBFCard(self):
        self.find_element(*self.DBFCard_loc).click()

    # 担保人法人代表证件号码
    DBFNumber = (By.NAME,'securityLegalIdNo')
    def send_DBFNumber(self,securityLegalIdNo="230903198611112345"):
        self.find_element(*self.DBFName_loc).send_keys(securityLegalIdNo)

    def click_DBFNumber(self):
        self.find_element(*self.DBFName_loc).click()

    # 点击一下查询
    queryBtn_loc = (By.CLASS_NAME,'searchBt')
    def click_queryBtn(self):
        self.find_element(*self.queryBtn_loc).click()


    # 勾选担保函协议
    js1_loc = 'document.getElementsByClassName("checkbox")[0].click();'
    def execute_js(self):
        self.script(self.js1_loc)

    # 勾选协议  使用js语法
    # js = "$('div>p>label').click();"#console控制台的jquery语法输入，但是不支持前端的vue框架，vue框架下需要用原版的js代码语句
    js2_loc = 'document.getElementsByClassName("checkbox")[1].click();'
    def execute_js2(self):
        self.script(self.js2_loc)

    # 提交按钮
    submitBtn_loc = (By.XPATH,'//*[@id="app"]/div/div[1]/div[2]/div[4]/div[2]/div')
    def click_submitBtn(self):
        self.find_element(*self.submitBtn_loc).click()

    # 确定按钮
    enterBtn_loc = (By.XPATH,'//*[@id="app"]/div/div[1]/div[2]/div[5]/div/div[2]/div/span')
    def click_enterBtn(self):
        self.find_element_wait(*self.enterBtn_loc)









