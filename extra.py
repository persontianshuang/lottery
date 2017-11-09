# from lxml import html

# 双色球
class Shuangseqiu:
    def __init__(self,response):
        self.response = response
        self.id = '001'
        self.des = '双色球'

    def main(self):
        data = {
            'id': self.id,
            'des': self.des,
            'progress': self.get_progress(),
            'check_time': self.get_check_time(),
            'lottery_num': self.get_lottery_num(),
        }
        return data

    def get_progress(self):
        progress_xpath = '//*[@id="js_box_kj_tbody"]/tr[2]/td[2]'
        progress = self.response.xpath(progress_xpath)[0].xpath('string(.)').strip().strip('期')
        return progress

    def get_check_time(self):
        time_xpath = '//*[@id="js_box_kj_tbody"]/tr[2]/td[3]'
        time_ = self.response.xpath(time_xpath)[0].xpath('string(.)').strip()
        return time_

    def get_lottery_num(self):
        red_xpath = '//*[@id="js_box_kj_tbody"]/tr[2]/td[4]/span[@class="ball_1"]'
        blue_xpath = '//*[@id="js_box_kj_tbody"]/tr[2]/td[4]/span[@class="ball_2"]'

        red = [x.xpath('string(.)') for x in
                    self.response.xpath(red_xpath)]
        blue = [x.xpath('string(.)') for x in
                    self.response.xpath(blue_xpath)]
        num = ','.join(red) + '#' + ','.join(blue)
        return num


# 大乐透
class Daletou:
    def __init__(self,response):
        self.response = response
        self.id = '113'
        self.des = '大乐透'

    def main(self):
        data = {
            'id': self.id,
            'des': self.des,
            'progress': self.get_progress(),
            'check_time': self.get_check_time(),
            'lottery_num': self.get_lottery_num(),
        }
        return data

    def get_progress(self):
        progress_xpath = '//*[@id="js_box_kj_tbody"]/tr[3]/td[2]'
        progress = self.response.xpath(progress_xpath)[0].xpath('string(.)').strip().strip('期')
        return progress

    def get_check_time(self):
        time_xpath = '//*[@id="js_box_kj_tbody"]/tr[3]/td[3]'
        time_ = self.response.xpath(time_xpath)[0].xpath('string(.)').strip()
        return time_

    def get_lottery_num(self):
        red_xpath = '//*[@id="js_box_kj_tbody"]/tr[3]/td[4]/span[@class="ball_1"]'
        blue_xpath = '//*[@id="js_box_kj_tbody"]/tr[3]/td[4]/span[@class="ball_2"]'

        red = [x.xpath('string(.)') for x in
                    self.response.xpath(red_xpath)]
        blue = [x.xpath('string(.)') for x in
                    self.response.xpath(blue_xpath)]
        num = ','.join(red) + '#' + ','.join(blue)
        return num

# 福彩3d
class Fucai3d:
    def __init__(self,response):
        self.response = response
        self.id = '002'
        self.des = '福彩3d'

    def main(self):
        data = {
            'id': self.id,
            'des': self.des,
            'progress': self.get_progress(),
            'check_time': self.get_check_time(),
            'lottery_num': self.get_lottery_num(),
        }
        return data

    def get_progress(self):
        progress_xpath = '//*[@id="js_box_kj_tbody"]/tr[4]/td[2]'
        progress = self.response.xpath(progress_xpath)[0].xpath('string(.)').strip().strip('期')
        return progress

    def get_check_time(self):
        time_xpath = '//*[@id="js_box_kj_tbody"]/tr[4]/td[3]'
        time_ = self.response.xpath(time_xpath)[0].xpath('string(.)').strip()
        return time_

    def get_lottery_num(self):
        ball_xpath = '//*[@id="js_box_kj_tbody"]/tr[4]/td[4]'
        ball = self.response.xpath(ball_xpath)[0].xpath('string(.)').strip()

        num = ','.join(ball)
        return num

# 11选5江西
class Jiangxi11xuan5:
    def __init__(self,response):
        self.response = response
        self.id = '106'
        self.des = '11选5江西'

    def main(self):
        data = {
            'id': self.id,
            'des': self.des,
            'progress': self.get_progress(),
            'check_time': self.get_check_time(),
            'lottery_num': self.get_lottery_num(),
        }
        return data

    def get_progress(self):
        progress_xpath = '//*[@id="js_box_kj_tbody"]/tr[15]/td[2]'
        progress = self.response.xpath(progress_xpath)[0].xpath('string(.)').strip().strip('期')
        return progress

    def get_check_time(self):
        time_xpath = '//*[@id="js_box_kj_tbody"]/tr[15]/td[3]'
        time_ = self.response.xpath(time_xpath)[0].xpath('string(.)').strip()
        return time_

    def get_lottery_num(self):
        ball_xpath = '//*[@id="js_box_kj_tbody"]/tr[15]/td[4]'
        ball = self.response.xpath(ball_xpath)[0].xpath('string(.)').strip()

        num = ','.join(ball)
        return num

