import schedule
import time


def job(name):
    print("her name is : ", name)


name = 'xiaona'
schedule.every(3).seconds.do(job,name)
schedule.every(10).minutes.do(job, name)
schedule.every().hour.do(job, name)
schedule.every().day.at("10:30").do(job, name)
schedule.every(5).to(10).days.do(job, name)
schedule.every().monday.do(job, name)
schedule.every().wednesday.at("13:15").do(job, name)

while True:
    schedule.run_pending()
    time.sleep(1)


#每隔3秒执行一次任务
# 每隔十分钟执行一次任务
#
# 每隔一小时执行一次任务
#
# 每天的10:30执行一次任务
#
# 每周一的这个时候执行一次任务
#
# 每周三13:15执行一次任务
#
# run_pending：运行所有可以运行的任务

