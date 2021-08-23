#coding=utf-8
import re,os,time,datetime
plans=[True, ['测试计划仅供参考', 1200, ['默写语文初一课内外古诗与文言文在田字格练字纸上', 'once', 120], ['阅读《西游记》和《水浒传》', 'once', 720], ['预习数学11单元并完成对应课内练习', 'once', 60], ['预习数学12单元并完成课内对应练习', 'once', 60], ['数学两道压轴题', 'every week', 8, 60, 26], ['阅读21世纪英语报2张并翻译，不懂的词记在笔记本上并背诵', 'every week', 8, 120, 26], ['按词性分类整理七上下册4个话题单词并背诵自测', 'every week', 8, 120, 26], ['背诵八上2个话 题单词', 'every week', 8, 120, 26], ['学唱一首英文歌', 'once', 60], ['观看一部英语电影', 'once', 120], ['成绩不足的抄单词', 'once', 60], ['观看电视剧《觉醒年代》并回答作业清单上的问题', 'once', 150], ['道法任选七下两个单元画思维导图', 'once', 120], ['观看《中国远征军》《大国崛起 》《我在故宫修文物》等并写一篇观后感', 'once', 180], ['整理地理七下思维导图', 'once', 120], ['生物任选作业清单上两个任务并完成', 'once', 60], ['任选作业清单上不同的3项进行体育锻炼并拍小视 频记录', 'every week', 8, 60, 26], ['任选作业清单上不同的3项进行体育锻炼并拍小视频记录', 'every week', 8, 60, 26], ['任选作业清单上不同的3项进行体育锻炼并拍小视频记录', 'every week', 8, 60, 26], ['任选作业清单上不同的3项进行体育锻炼并拍小视频记录', 'every week', 8, 60, 26], ['美术 任选作业清单上的主题一项并完成主题绘画一幅', 'once', 60], ['音乐以“建党100周年”为主题拍视频秀 才艺，具体请看作业清单', 'once', 60], ['信息技术以“建党100周年”为主题完成一份电子板报', 'once', 60]]]
#一个完善的文件删除行、写入行、查找行api
#好怕程序又出bug，这里放一个plans的原版吧
#plans=[True, ['初一年5班通用暑假计划', 1200, ['默写语文初一课内外古诗与文言文在田字格练字纸上', 'once', 120], ['阅读《西游记》和《水浒传》', 'once', 720], ['预习数学11单元并完成对应课内练习', 'once', 60], ['预习数学12单元并完成课内对应练习', 'once', 60], ['数学两道压轴题', 'every week', 8, 60, 26], ['阅读21世纪英语报2张并翻译，不懂的词记在笔记本上并背诵', 'every week', 8, 120, 26], ['按词性分类整理七上下册4个话题单词并背诵自测', 'every week', 8, 120, 26], ['背诵八上2个话 题单词', 'every week', 8, 120, 26], ['学唱一首英文歌', 'once', 60], ['观看一部英语电影', 'once', 120], ['成绩不足的抄单词', 'once', 60], ['观看电视剧《觉醒年代》并回答作业清单上的问题', 'once', 150], ['道法任选七下两个单元画思维导图', 'once', 120], ['观看《中国远征军》《大国崛起 》《我在故宫修文物》等并写一篇观后感', 'once', 180], ['整理地理七下思维导图', 'once', 120], ['生物任选作业清单上两个任务并完成', 'once', 60], ['任选作业清单上不同的3项进行体育锻炼并拍小视 频记录', 'every week', 8, 60, 26], ['任选作业清单上不同的3项进行体育锻炼并拍小视频记录', 'every week', 8, 60, 26], ['任选作业清单上不同的3项进行体育锻炼并拍小视频记录', 'every week', 8, 60, 26], ['任选作业清单上不同的3项进行体育锻炼并拍小视频记录', 'every week', 8, 60, 26], ['美术 任选作业清单上的主题一项并完成主题绘画一幅', 'once', 60], ['音乐以“建党100周年”为主题拍视频秀 才艺，具体请看作业清单', 'once', 60], ['信息技术以“建党100周年”为主题完成一份电子板报', 'once', 60]]]
def fileapi(fileplace,wait_to_write,the_goal,del_or_write_or_find):
    #del_or_write_or_find=="write"时wait_to_write参数必填，del_or_write_or_find!="write"时wait_to_write可不填
    file=open(fileplace,"r",encoding="utf-8")
    filelines=file.readlines()
    file.close()
    for i in range(len(filelines)):
        ii=re.search(the_goal,str(filelines[i]),re.X)
        if ii!=None :
            if del_or_write_or_find=="write":
                filelines[i]=wait_to_write
            elif del_or_write_or_find=="del":
                del(filelines[i])
            elif del_or_write_or_find=="find":
                return 0
            break
    if del_or_write_or_find=="find":
        return False
    file=open(fileplace,"w",encoding="utf-8")
    file.writelines(filelines)
    file.close()
    return 0

def 显示与控制中心(plan,today):
    see_plan(plan,today)
    this_week = today.isocalendar()[1]
    while True:
        ii=int(input("1.退出查询\n2.标记完成情况（支持补做）\n3.增加项目\n4.手动删除项目\n5.提前查看下一天的计划(即%s)\n6.与第五选项相对（即%s）\n请输入代码：" %(str(today+datetime.timedelta(days=1)),str(today-datetime.timedelta(days=1)))))
        if ii==1:
            return plan
        elif ii==2:
            while True:
                i=input("输入要求标记完成的代号（即上面显示的项目前面的编号）\n不想继续可以输入“exit”退出标记完成情况：")
                if i=="exit":break
                i=int(i)+1
                if plan[i][1] == "every day":
                    plan[i][4]=plan[i][4]+datetime.timedelta(days=1)
                    plan[i][2]=plan[i][2]-1
                    if plan[i][2]==0:
                        print("恭喜你完成了这个项目！已自动帮你从计划中清除。")
                        del plan[i]
                    else:
                        print("已登记，你还差"+str(plan[i][2])+"次，已完成日期到"+str(plan[i][4]))
                if plan[i][1] == "every week":
                    plan[i][4] = plan[i][4] + 1
                    plan[i][2] = plan[i][2] - 1
                    if plan[i][2] == 0:
                        print("恭喜你完成了这个项目！已自动帮你从计划中清除。")
                        del plan[i]
                    else:
                        print("已登记，你还差" + str(plan[i][2]) + "次，已完成周到" +str(plan[i][4])+"。（ps：当前是今年第"+str(this_week)+"个周）")
                if plan[i][1]=="once":
                    print("恭喜你完成了这个项目！已自动帮你从计划中清除。")
                    del plan[i]
                time.sleep(2)
                see_plan(plan,today)
        elif ii==3:
            plan=add_plans(plan,today)
        elif ii==4:
            while True:
                i=input('输入要删除的项目编号（即上面显示的项目前面的编号）\n不想继续可以输"exit"：')
                if i=="exit":
                    break
                else:del plan[int(i)+1]
                time.sleep(2)
                see_plan(plan,today)
        elif ii==5:
            today=today+datetime.timedelta(days=1)
            see_plan(plan, today)
        elif ii==6:
            today=today-datetime.timedelta(days=1)
            see_plan(plan, today)
    return plan
def see_plan(plan,today):
    os.system("cls")
    start=2
    this_week=today.isocalendar()[1]
    over=plan[1]-(datetime.datetime.now().hour*60+datetime.datetime.now().minute)
    #先显示每天必做
    print("\t"+str(today)+"的"+plan[0])
    for i in range(start,len(plan)):
        if plan[i][1]=="every day":
            print(str(i - 1), plan[i][0],"\t每天\t ",end="")
            if plan[i][4].__ge__(today):  # 超额完成
                print("今日已完成 你也可以提前看下一天的计划，还需要做" + str(plan[i][2]) + "次你就做完这项任务啦~")
            elif (today-datetime.timedelta(days=1)).__eq__(plan[i][4]):#需要完成
                over=over-plan[i][3]
                print("今日未完成")
            elif (today-datetime.timedelta(days=1)).__gt__(plan[i][4]):  # 需要完成
                over = over - plan[i][3]
                print("需要补做")
            elif plan[i][3]>over:
                print("今日时间余额已耗尽")
    #再显示每周必做
        if plan[i][1]=="every week":
            print(str(i-1), plan[i][0],"\t每周\t ",end="")
            if plan[i][4]>=this_week:  # 超额完成 26、27>=26
                print("本周已完成 你也可以提前看下一天的计划，还需要完成" + str(plan[i][2]) + "次你就做完这项任务啦~")
            elif this_week-1==plan[i][4]:#需要完成 26-1==25
                over=over-plan[i][3]
                print("本周未完成")
            elif this_week-1>plan[i][4]:  # 需要补做 26-1>24
                over = over - plan[i][3]
                print("需要补做")
            elif plan[i][3]>over:
                print("今日时间余额已耗尽")
        if plan[i][1]=="once":
            print(str(i - 1), plan[i][0], "\t一次\t未完成 ", end="")
            if plan[i][2]>over:
                print("今日时间余额已耗尽",end="")
            print("")
    print("")
def add_plans(plan,today):
    if plan==[]:
        print("Hi!看来你还没有计划。想要创建一个吗？\n1.Yes,我要好好学习\t2.No,我可以做到自我安排")
        if int(input("请输入:"))==1:
            print("期待你做完作业快乐的样子！来创建计划吧！")
            time.sleep(1)
            os.system("cls")
            print("首先，为你的计划取一个响亮的名字(如我的暑假计划等，别忘了最后有计划两个字哦！):", end="")
            plan.append(input(""))
            i,ii=input("请输入你到一天的什么时间就不继续完成项目了(比如18:30，请使用小写冒号，就是不要使用输入法的中文模式):").strip().split(':')
            plan.append(int(int(i)*60+int(ii)))
        else:
            print("期待你做自我管理大师！")
            return 0
    while True:
        i=int(input("选择项目类型:\n1.每天\n2.每周\n3.只要做一次\n4.退了退了不增加了\n(可能不能完全满足你的需求，比如一周要做4次同样的事情，但是你可以直接在名称里写“做4次XXX”，也可以重复创建4个相同的项目):"))
        plan1=[]
        if i==4:break
        plan1.append(input("请输入项目的名称（如写作业，做运动等）:"))
        if i==1:
            plan1.append("every day")
        elif i==2:
            plan1.append("every week")
        elif i==3:
            plan1.append("once")
        if i!=3:plan1.append(int(input("请输入这件事要做几天/几周:")))
        plan1.append(int(input("你觉得做一次这个项目会耗费你多久（分钟，不能输入xx:xx哦）？请输入:")))
        if i==1:
            plan1.append(datetime.date.today()-datetime.timedelta(days=1))
        if i==2:
            plan1.append(datetime.date.today().isocalendar()[1]-1)
        plan.append(plan1)
        print("添加完毕！接下来将显示完整的计划方便你参考：")
        time.sleep(2)
        see_plan(plan,today)
    return plan
def main():
    global plans
    print("假期规划助手\n\tby 吴宗权")
    print("使用方法：打开这个软件，按照提示输入信息，以后每天打开程序都会显示今天应该做什么~\n帮助你更充实地过假期！\n")
    if plans!=[False]:
        print("检测到当前已存在计划！\n请选择你现在要查看的计划:")
        for i in range(1,len(plans)):print(str(i)+":"+plans[i][0])
        print(str(len(plans))+" 非计划选项:新建计划")
        print(str(len(plans)+1) + " 非计划选项:退出")
        print(str(len(plans)+2)+" 非计划选项:删除计划")
        user_decide=-1
        user_decide=int(input("请输入选项编号:"))
        if user_decide==len(plans):
            add_plans([],datetime.date.today())
            fileapi(os.path.abspath(__file__), "plans=" + str(plans) + "\n", "plans=\[.", "write")
        elif user_decide==len(plans)+1:return 0
        elif user_decide==len(plans)+2:
            del plans[int(input("请输入计划编号:"))]
            if len(plans)==1:
                plans=[False]
            fileapi(os.path.abspath(__file__), "plans=" + str(plans) + "\n", "plans=\[.", "write")
        else:
            plans[user_decide]=显示与控制中心(plans[user_decide],datetime.date.today())
            fileapi(os.path.abspath(__file__), "plans=" + str(plans) + "\n", "plans=\[.", "write")
    else:
        plans=[True,add_plans([],datetime.date.today())]
        显示与控制中心(plans[len(plans)-1], datetime.date.today())
        fileapi(os.path.abspath(__file__), "plans=" + str(plans) + "\n", "plans=\[.", "write")
main()