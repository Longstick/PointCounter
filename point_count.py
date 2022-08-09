# coding=utf-8
from dis import dis
import os, time
from datetime import datetime

class PointCounter(object):
    def __init__(self):
        pass

    def count_getup_time(self):
        while True:
            getup_point = 0
            is_late = False
            typein = input("今天有早起吗？：")
            if typein.find(":") == -1:
                print ("格式有误， 如 8:30")
                continue
            getuptime = datetime.strptime(typein, "%H:%M")
            basetime = datetime.strptime("8:30", "%H:%M")
            tdelta = (getuptime - basetime).seconds / 3600
            if getuptime >= basetime:
                tdelta = (getuptime - basetime).seconds / 60
                is_late = True
            else:
                tdelta = (basetime - getuptime).seconds / 60

            if tdelta < 30:
                print ("今天准时起床，再接再厉")
            else:
                getup_point = int(tdelta / 30) * 5
                if is_late: 
                    print ("今天起晚惹，不要松懈呀")
                    getup_point = - getup_point
                else:
                    print ("今天早起啦！真棒，继续保持！")
            print ("今天的早起分值为：%d\n" % getup_point)
            return getup_point

    def count_gobed_time(self):
        while True:
            gobed_point = 0
            is_late = False
            typein = input("今天几点上的床呢？：")
            if typein.find(":") == -1:
                print ("格式有误， 如 12:00")
                continue
            gobedtime = datetime.strptime(typein, "%H:%M")
            basetime = datetime.strptime("12:00", "%H:%M")
            tdelta = (gobedtime - basetime).seconds / 3600
            if gobedtime.hour <= 5:
                basetime = datetime.strptime("0:00", "%H:%M")
                tdelta = (gobedtime - basetime).seconds / 60
                is_late = True
            else:
                tdelta = (basetime - gobedtime).seconds / 60

            if tdelta < 30:
                print ("今天准时睡觉，再接再厉")
            else:
                gobed_point = int(tdelta / 30) * 5
                if is_late: 
                    print ("今天睡晚了！快点早睡哦！")
                    gobed_point = - gobed_point
                else:
                    print ("今天早睡啦！太棒辽！继续保持！")
            print ("今天的早睡分值为：%d\n" % gobed_point)
            return gobed_point

    def count_learning_time(self):
        while True:
            learning_time_point = 0
            learning_time = float(input("今天学习了多久呢？："))
            if learning_time <= 0:
                print ("请输入正确的时长")
                continue
            else:
                if learning_time < 6:
                    learning_time_point = 0
                    print ("今天学习时长达到目标，请继续努力吧")
                elif learning_time < 8:
                    learning_time_point = 10
                    print ("今天学习了很久哦，状态火热，棒！")
                elif learning_time < 10: 
                    learning_time_point = 20
                    print ("今天非常努力！！！太棒啦！")
                else:
                    learning_time_point = 30
                    print ("今天学疯了，超级棒！！！但是要注意休息！")
                print ("今天的学习时长分值为：%d\n" % learning_time_point)
                return learning_time_point

    def count_words(self):
        while True:
            words_point = 0
            words_num = int(input("今天记了多少单词呢？："))
            if words_num <= 0:
                print ("请输入正确的数量")
                continue
            else:
                if words_num < 200:
                    words_point = -10
                    print ("今天单词记的有点少呢，再接再厉！")
                elif words_num < 250:
                    print ("今天单词达到目标啦！继续努力！")
                elif words_num < 300:
                    words_point = 10
                    print ("今天单词背了很多哦，棒棒！加油加油")
                else:
                    words_point = 15
                    print ("今天记忆力超乎常人，牛皮哇")                    
                print ("今天的背单词分值为：%d\n" % words_point)
                return words_point

    def count_readings(self):
        while True:
            reading_point = 0
            err_num = int(input("今天阅读怎么样，错了几个呢？："))
            if err_num < 0:
                print ("请输入正确的数量")
                continue
            else:
                if err_num == 0:
                    reading_point = +10
                    print ("哇哦今天阅读全对！厉害厉害")
                elif err_num == 1:
                    print ("今天只错了一个，还不错，继续加油！")
                else:
                    reading_point = -10
                    print ("今天的阅读有点难度哦，再接再厉吧")                    
                print ("今天的阅读分值为：%d\n" % reading_point)
                return reading_point

    def count_workout(self):
        while True:
            workout_point = 0
            workout_time = int(input("今天有运动不？："))
            if workout_time < 0:
                print ("请输入正确的时长")
                continue
            else:
                if workout_time == 0:
                    print ("学习辛苦偶尔还是要动一动哦")
                elif workout_time < 30:
                    print ("时间有点太短啦！还是要多运动一会儿")
                elif workout_time < 60:
                    workout_point = 20
                    print ("不错不错，今天有好好运动保持状态哦")
                else:
                    workout_point = int(workout_time / 30)
                    print ("哇塞，今天超级棒！身体倍儿棒，感觉是不是很好")                    
                print ("今天的运动分值为：%d\n" % workout_point)
                return workout_point

    def count_tasks(self):
        while True:
            task_point = 0
            discomplete = int(input("今天学习任务完成的咋样，有未完成吗？："))
            if discomplete < 0:
                print ("请输入正确的数量")
                continue
            else:
                if discomplete == 0:
                    task_point = 10
                    print ("今天任务都清完啦，很不错")
                elif discomplete < 3:
                    task_point = -5 * discomplete
                    print ("今天有未完成哦！要分析一下原因捏")
                else:
                    task_point = -5 * discomplete
                    print ("太多未完成了！今天状态不好哦，不可以这样！")                    
                print ("今天的完成度分值为：%d\n" % task_point)
                return task_point

    def count_items(self):
        while True:
            item_point = 0
            items = int(input("有没有完成大项呢？："))
            if items < 0:
                print ("请输入正确的数量")
                continue
            elif items > 0:
                item_point = items * 100
                print("今天有辛苦啦！又干掉一门，耶耶")
            else:
                print ("继续努力吧")
            print ("今天的大项分值为：%d\n" % item_point)
            return item_point

if __name__ == "__main__":
    pc = PointCounter()
    today = input("今天日期是?：")
    points = {
        '早起' : pc.count_getup_time(),
        '早睡' : pc.count_gobed_time(),
        '学习时长' : pc.count_learning_time(),
        '背单词' : pc.count_words(),
        '阅读正确率' : pc.count_readings(),
        '锻炼' : pc.count_workout(),
        '任务完成度' : pc.count_tasks(),
        '大项bonus' : pc.count_items()
    }
    sumtotal = sum(points.values())
    print ("======== %s 总结 ========" % today)
    for point in points:
        if point != 0:
            print ("%s得分为:%d" % (point, points[point]))
    print ("=========================")
    print ("今天总共得分为：%d" % sumtotal)

    
