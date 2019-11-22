from .base import Page
from selenium.webdriver.common.by import By
class BackendPage(Page):

    url = "/"

    backend_userName_loc = (By.XPATH,'//*[@id="app"]/div/div/div[1]/input')
    def click_backend_userName(self):
        self.find_element(*self.backend_userName_loc).click()

    def send_backend_userName(self,username):
        self.find_element(*self.backend_userName_loc).send_keys(username)

    # 登录账号
    backend_passWord_loc = (By.XPATH,'//*[@id="app"]/div/div/div[2]/input')
    def click_backend_passWord(self):
        self.find_element(*self.backend_passWord_loc).click()

    def send_backend_passWord(self,password):
        self.find_element(*self.backend_passWord_loc).send_keys(password)

    # 点击空白页
    backend_zongheBtn_loc = (By.XPATH,'//*[@id="app"]/div/h1')
    def click_backend_zongheBtn(self):
        self.find_element(*self.backend_zongheBtn_loc).click()

    backend_loginBtn_loc = (By.XPATH,'//*[@id="app"]/div/div/button')
    def click_backend_loginBtn(self):
        self.find_element(*self.backend_loginBtn_loc).click()

    backend_debitOne_loc = (By.XPATH,'/html/body/div/div/div[1]/div[2]/ul/li[2]/div')
    def click_backend_debitOne(self):
        self.find_element(*self.backend_debitOne_loc).click()

    # 借款申请审核
    backend_debitTwo_loc = (By.XPATH,'/html/body/div/div/div[1]/div[2]/ul/li[2]/ul/li[5]/div')
    def click_backend_debitTwo(self):
        self.find_element(*self.backend_debitTwo_loc).click()

    backend_debitThree_loc = (By.XPATH,'/html/body/div/div/div[1]/div[2]/ul/li[2]/ul/li[5]/ul/li[1]')
    def click_backend_debitThree(self):
        self.find_element(*self.backend_debitThree_loc).click()
        # 点击待审核
    backend_stayAduit_loc =(By.XPATH,'//*[@id="app"]/div/div[3]/div/div[2]/div[1]/div[2]/button/span')
    def click_backend_stayAduit(self):
        self.find_element(*self.backend_stayAduit_loc).click()

        # 点击查看详情
    backend_catDetail_loc = (By.XPATH,'//*[@id="app"]/div/div[3]/div/div[3]/div[1]/div[5]/div[2]/table/tbody/tr[1]/td[24]/div/button/span')
    def click_backend_catDetail(self):
        self.find_element(*self.backend_catDetail_loc).click()

        # 通过按钮
    backend_passBtn_loc = (By.XPATH,'/html/body/div/div/div[3]/div/div[3]/div/div[1]/button')
    def click_backend_passBtn(self):
        self.find_element(*self.backend_passBtn_loc).click()

        # 风控评级
    backend_riskBtn_loc =(By.XPATH,'//*[@id="app"]/div/div[3]/div/div[5]/div/div[2]/div/form/div[1]/div/div/div[1]/input')
    def click_backend_riskBtn(self):
        self.find_element(*self.backend_riskBtn_loc).click()

        # 选择 风控评级
    backend_selectRisk_loc =(By.XPATH,'/html/body/div[3]/div/div[1]/ul/li[1]')
    def click_backend_selectRisk(self):
        self.find_element(*self.backend_selectRisk_loc).click()

        # 输入审核意见
    backend_inputInfo_loc = (By.XPATH,'//*[@id="app"]/div/div[3]/div/div[5]/div/div[2]/div/form/div[2]/div/div[1]/textarea')
    def click_backend_inputInfo(self):
        self.find_element(*self.backend_inputInfo_loc).click()

    def send_backend_inputInfo(self,info=u"初审审核通过"):
        self.find_element(*self.backend_inputInfo_loc).send_keys(info)
        # 上传文件
        # uploadFileBtn = driver.find_element_by_name("uploadFile")
        # uploadFileBtn.send_keys(u'G:\P2G-BUG\借款bug\登录2.png')
        # 提交


    backend_submitBtn_loc = (By.XPATH,'//*[@id="app"]/div/div[3]/div/div[5]/div/div[2]/div/form/div[4]/div/div/div[1]/button/span')
    def click_backend_submitBtn(self):
        self.find_element_wait(*self.backend_submitBtn_loc).click()

            # 打开复审 -- > 新流程已简化 -- > 直接进入复审阶段
            # 点击复审按钮
    backend_passButton_loc = (By.XPATH,'/html/body/div/div/div[3]/div/div[3]/div/div[1]/button')
    def click_backend_passButton(self):
        self.find_element(*self.backend_passBtn_loc).click()

            # 打开风险详情
    backend_riskPage_loc = (By.XPATH,'//*[@id="app"]/div/div[3]/div/div[5]/div/div[2]/div/form/div[1]/div/div/div[1]/input')
    def click_backend_riskPage(self):
        self.find_element(*self.backend_riskPage_loc).click()

            # 选择 风险等级
    backend_selRiskLevel_loc = (By.XPATH,'/html/body/div[3]/div/div[1]/ul/li[1]')
    def click_backend_selRiskLevel(self):
        self.find_element(*self.backend_selRiskLevel_loc).click()

            # 输入审核意见
    backend_inputReAduit_loc = (By.XPATH,'//*[@id="app"]/div/div[3]/div/div[5]/div/div[2]/div/form/div[2]/div/div[1]/textarea')
    def click_backend_inputReAduit(self):
        self.find_element(*self.backend_inputReAduit_loc).click()
    def send_backend_inputReAduit(self,reAduit=u"复审审核通过"):
        self.find_element(*self.backend_inputReAduit_loc).send_keys(reAduit)

            # #选择文件上传
            # uploadBtn = driver.find_element_by_name('uploadFile')
            # uploadBtn.send_keys(u'G:\P2G-BUG\借款bug\登录2.png')
            # 提交
    backend_submitBtn2_loc = (By.XPATH,'//*[@id="app"]/div/div[3]/div/div[5]/div/div[2]/div/form/div[4]/div/div/div[1]/button/span')
    def click_backend_submitBtn2(self):
        self.find_element_wait(*self.backend_submitBtn2_loc).click()
