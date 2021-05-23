from django.db.models.fields import DateField
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, View
from pandas.core.frame import DataFrame
from .models import Oneteam_model
from django.urls import reverse_lazy
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 
import json, io, copy, csv, japanize_matplotlib
from operator import itemgetter 

class Oneteam_Delete(DeleteView):
    template_name = 'delete.html'
    model = Oneteam_model
    success_url = reverse_lazy('list')

class Oneteam_Update(UpdateView):
    template_name = 'update.html'
    model = Oneteam_model
    fields = ('お名前', '所属部署',
              '日曜日の予定', '月曜日の予定', '火曜日の予定', '水曜日の予定', '木曜日の予定', '金曜日の予定', '土曜日の予定', 
              
              'task1', 
              'urgency_weight1', 
              'importance_weight1', 
              'motivation_weight1', 
              'difficult_weight1',

              'task2', 
              'urgency_weight2', 
              'importance_weight2', 
              'motivation_weight2', 
              'difficult_weight2',

              'task3', 
              'urgency_weight3', 
              'importance_weight3', 
              'motivation_weight3', 
              'difficult_weight3',     

              'task4', 
              'urgency_weight4', 
              'importance_weight4', 
              'motivation_weight4', 
              'difficult_weight4',  

              'task5', 
              'urgency_weight5', 
              'importance_weight5', 
              'motivation_weight5', 
              'difficult_weight5',

              'task6', 
              'urgency_weight6', 
              'importance_weight6', 
              'motivation_weight6', 
              'difficult_weight6',     

              'task7', 
              'urgency_weight7', 
              'importance_weight7', 
              'motivation_weight7', 
              'difficult_weight7',   

              'task8', 
              'urgency_weight8', 
              'importance_weight8', 
              'motivation_weight8', 
              'difficult_weight8',

              'task9', 
              'urgency_weight9', 
              'importance_weight9', 
              'motivation_weight9', 
              'difficult_weight9',     

              'task10', 
              'urgency_weight10', 
              'importance_weight10', 
              'motivation_weight10', 
              'difficult_weight10'           
              )
    success_url = reverse_lazy('list')

class Oneteam_List(ListView):
    template_name = 'list.html'
    model = Oneteam_model

class Oneteam_Create(CreateView):
    template_name = 'create.html'
    model = Oneteam_model
    fields = ('お名前', '所属部署',
              '日曜日の予定', '月曜日の予定', '火曜日の予定', '水曜日の予定', '木曜日の予定', '金曜日の予定', '土曜日の予定', 

              'task1', 
              'urgency_weight1', 
              'importance_weight1', 
              'motivation_weight1', 
              'difficult_weight1',

              'task2', 
              'urgency_weight2', 
              'importance_weight2', 
              'motivation_weight2', 
              'difficult_weight2',

              'task3', 
              'urgency_weight3', 
              'importance_weight3', 
              'motivation_weight3', 
              'difficult_weight3',     

              'task4', 
              'urgency_weight4', 
              'importance_weight4', 
              'motivation_weight4', 
              'difficult_weight4',  

              'task5', 
              'urgency_weight5', 
              'importance_weight5', 
              'motivation_weight5', 
              'difficult_weight5',

              'task6', 
              'urgency_weight6', 
              'importance_weight6', 
              'motivation_weight6', 
              'difficult_weight6',     

              'task7', 
              'urgency_weight7', 
              'importance_weight7', 
              'motivation_weight7', 
              'difficult_weight7',   

              'task8', 
              'urgency_weight8', 
              'importance_weight8', 
              'motivation_weight8', 
              'difficult_weight8',

              'task9', 
              'urgency_weight9', 
              'importance_weight9', 
              'motivation_weight9', 
              'difficult_weight9',     

              'task10', 
              'urgency_weight10', 
              'importance_weight10', 
              'motivation_weight10', 
              'difficult_weight10'           
              )

    success_url = reverse_lazy('list')

class Oneteam_Detail(DetailView):
    template_name = 'detail.html'
    model = Oneteam_model

# SVG化
def plt2svg():
    buf = io.BytesIO()
    plt.savefig(buf, format='svg', bbox_inches='tight')
    s = buf.getvalue()
    buf.close()
    return s

def matrixfunk(request, pk):
    template_name = 'detail.html'
    object = Oneteam_model.objects.get(pk=pk)

    task1 = object.task1
    task2 = object.task2
    task3 = object.task3
    task4 = object.task4
    task5 = object.task5
    task6 = object.task6
    task7 = object.task7
    task8 = object.task8
    task9 = object.task9
    task10 = object.task10

    task_l = [task1, task2, task3, task4, task5, task6, task7, task8, task9, task10]

    urgency_d = {}
    importance_d = {}
    motivation_d = {}
    difficult_d = {}    

    urgency_d[task1] = object.urgency_weight1
    importance_d[task1] = object.importance_weight1
    motivation_d[task1] = object.motivation_weight1
    difficult_d[task1] = object.difficult_weight1

    urgency_d[task2] = object.urgency_weight2
    importance_d[task2] = object.importance_weight2
    motivation_d[task2] = object.motivation_weight2
    difficult_d[task2] = object.difficult_weight2

    urgency_d[task3] = object.urgency_weight3
    importance_d[task3] = object.importance_weight3
    motivation_d[task3] = object.motivation_weight3
    difficult_d[task3] = object.difficult_weight3

    urgency_d[task4] = object.urgency_weight4
    importance_d[task4] = object.importance_weight4
    motivation_d[task4] = object.motivation_weight4
    difficult_d[task4] = object.difficult_weight4

    urgency_d[task5] = object.urgency_weight5
    importance_d[task5] = object.importance_weight5
    motivation_d[task5] = object.motivation_weight5
    difficult_d[task5] = object.difficult_weight5

    urgency_d[task6] = object.urgency_weight6
    importance_d[task6] = object.importance_weight6
    motivation_d[task6] = object.motivation_weight6
    difficult_d[task6] = object.difficult_weight6

    urgency_d[task7] = object.urgency_weight7
    importance_d[task7] = object.importance_weight7
    motivation_d[task7] = object.motivation_weight7
    difficult_d[task7] = object.difficult_weight7

    urgency_d[task8] = object.urgency_weight8
    importance_d[task8] = object.importance_weight8
    motivation_d[task8] = object.motivation_weight8
    difficult_d[task8] = object.difficult_weight8

    urgency_d[task9] = object.urgency_weight9
    importance_d[task9] = object.importance_weight9
    motivation_d[task9] = object.motivation_weight9
    difficult_d[task9] = object.difficult_weight9

    urgency_d[task10] = object.urgency_weight10
    importance_d[task10] = object.importance_weight10
    motivation_d[task10] = object.motivation_weight10
    difficult_d[task10] = object.difficult_weight10
    
    # 以下ステータス作成
    labels = ['緊急度', '重要度', 'モチベーション', '難易度']
    # for文で平均を出す
    task_task_l = []
    for task in task_l:
        if task != '':
            task_task_l.append([urgency_d.get(task), importance_d.get(task), motivation_d.get(task), difficult_d.get(task)])
        else:
            pass
    score_df = DataFrame(task_task_l)
    urgency_mean = score_df[0].mean()
    importance_mean = score_df[1].mean()
    motivation_mean = score_df[2].mean()
    difficult_mean = score_df[3].mean()

    values = [urgency_mean, importance_mean, motivation_mean, difficult_mean]
    angles = np.linspace(0, 2 * np.pi, len(labels) + 1, endpoint=True)
    values = np.concatenate((values, [values[0]]))  # 閉じた多角形にする

    fig = plt.figure(figsize=(14, 5), dpi=150)
    fig.subplots_adjust(hspace=0.5)
    ax1 = fig.add_subplot(121, polar=True)
    ax1.plot(angles, values, 'o-', color='#651818')  # 外枠
    ax1.fill(angles, values, alpha=0.25, color='#edcece')  # 塗りつぶし
    ax1.set_thetagrids(angles[:-1] * 180 / np.pi, labels)  # 軸ラベル
    ax1.set_rlim(0 ,6)
    ax1.set_title('〜今週のタスク〜'.format(task1), size=25)

    #　以下マトリクス作成
    color_d = {1:'#54B5FF', 2:'#c2afff', 3:'#7fff5f', 4:'#FFC55F', 5:'#ff0000', 6:'a31010'} 

    ax2 = fig.add_subplot(122)
    ax2.plot([0, 6.5], [3.5, 3.5], color='black', linewidth=7, alpha=0.3)
    ax2.plot([3.5, 3.5], [0, 6.5], color='black', linewidth=7, alpha=0.3)

    for task in task_l:
        if task != '':
            ax2.text(urgency_d.get(task), 
                    importance_d.get(task), 
                    task, 
                    va='center', 
                    ha='center', 
                    fontsize=difficult_d.get(task)*3, 
                    color=color_d.get(motivation_d.get(task)))
        else:
            pass
                
    ax2.axvspan(3.5, 6.5, 0.5, 1, color = "red", alpha=0.3) #第1象限 最優先①
    ax2.axvspan(0, 3.5, 0.5, 1, color = "orange", alpha=0.3) #第2象限 本当はやるべき②
    ax2.axvspan(0, 3.5, 0, 0.5, color = "green", alpha=0.1) #第3象限 放置ちされがち④
    ax2.axvspan(3.5, 6.5, 0, 0.5, color = "yellow", alpha=0.3) #第4象限 優先されがち③

    ax2.set_title('〜緊急・重要マトリックス〜', size=25)
    ax2.set_xlabel('緊急度')
    ax2.set_ylabel('重要度')
    ax2.set_xlim(0.5, 6.5)
    ax2.set_ylim(0.5, 6.5)
    ax2.grid(True)

    svg = plt2svg()  #SVG化
    plt.cla()  # グラフをリセット
    response = HttpResponse(svg, content_type='image/svg+xml')
    return response




def barfunk(request):    

    object_all = Oneteam_model.objects.all()
    data_len = len(object_all)
    bar_l = list(range(1, data_len+1))

    busyness_l = []
    for index, i in enumerate(object_all):
        name = i.お名前
        schedule_len = len(i.日曜日の予定.splitlines()) + len(i.月曜日の予定.splitlines()) + len(i.火曜日の予定.splitlines()) + len(i.水曜日の予定.splitlines()) + len(i.木曜日の予定.splitlines()) + len(i.金曜日の予定.splitlines()) + len(i.土曜日の予定.splitlines())
        print(schedule_len)
        count = 0
        for j in [i.task1, i.task2, i.task3, i.task4, i.task5, i.task6, i.task7, i.task8, i.task9, i.task10]:
            if j != '':
                count += 1
        busyness_len = schedule_len + count
        busyness_l.append([name, busyness_len])

    busyness_l = sorted(busyness_l, key=itemgetter(1), reverse=True)

    name_l = [set[0] for set in busyness_l]
    busy_l = [set[1] for set in busyness_l]

    fig, ax = plt.subplots(figsize=(12, 9), dpi=150)
 
    for index, i in enumerate(busyness_l):
        ax.text(index+1, i[1], i[1], ha='center', va='bottom', fontsize=20)

    ax.bar(bar_l, busy_l, tick_label=name_l, color='gray')
    ax.set_title('Busyness', fontsize=30, fontname='IPAexGothic')
    ax.set_xticklabels(name_l, rotation=45, fontsize=20)
    ax.grid(True)
    ax.set_axisbelow(True)

    svg = plt2svg()  #SVG化
    plt.cla()  # グラフをリセット
    response = HttpResponse(svg, content_type='image/svg+xml')
    return response


class UserCsvDownloadView(View):
    def get(self, request, *args, **kwargs):
        object = Oneteam_model.objects.get(pk=self.kwargs['pk'])

        sun_schedule_l = object.日曜日の予定.splitlines()
        mon_schedule_l = object.月曜日の予定.splitlines()
        tue_schedule_l = object.火曜日の予定.splitlines()
        wed_schedule_l = object.水曜日の予定.splitlines()
        thu_schedule_l = object.木曜日の予定.splitlines()
        fri_schedule_l = object.金曜日の予定.splitlines()
        sat_schedule_l = object.土曜日の予定.splitlines()

        task1 = object.task1
        task2 = object.task2
        task3 = object.task3
        task4 = object.task4
        task5 = object.task5
        task6 = object.task6
        task7 = object.task7
        task8 = object.task8
        task9 = object.task9
        task10 = object.task10

        schedule_d = {'日曜日':sun_schedule_l, 
                    '月曜日':mon_schedule_l,
                    '火曜日':tue_schedule_l,
                    '水曜日':wed_schedule_l,
                    '木曜日':thu_schedule_l,
                    '金曜日':fri_schedule_l,
                    '土曜日':sat_schedule_l,}

        week = ['日曜日', '月曜日', '火曜日', '水曜日', '木曜日', '金曜日', '土曜日']

        task_set = [task1, task2, task3, task4, task5, task6, task7, task8, task9, task10]
        task_l = [i for i in task_set if i != '']
        urgency_d = {}
        importance_d = {}
        motivation_d = {}
        difficult_d = {}    

        urgency_d[task1] = object.urgency_weight1
        importance_d[task1] = object.importance_weight1
        motivation_d[task1] = object.motivation_weight1
        difficult_d[task1] = object.difficult_weight1

        urgency_d[task2] = object.urgency_weight2
        importance_d[task2] = object.importance_weight2
        motivation_d[task2] = object.motivation_weight2
        difficult_d[task2] = object.difficult_weight2

        urgency_d[task3] = object.urgency_weight3
        importance_d[task3] = object.importance_weight3
        motivation_d[task3] = object.motivation_weight3
        difficult_d[task3] = object.difficult_weight3

        urgency_d[task4] = object.urgency_weight4
        importance_d[task4] = object.importance_weight4
        motivation_d[task4] = object.motivation_weight4
        difficult_d[task4] = object.difficult_weight4

        urgency_d[task5] = object.urgency_weight5
        importance_d[task5] = object.importance_weight5
        motivation_d[task5] = object.motivation_weight5
        difficult_d[task5] = object.difficult_weight5

        urgency_d[task6] = object.urgency_weight6
        importance_d[task6] = object.importance_weight6
        motivation_d[task6] = object.motivation_weight6
        difficult_d[task6] = object.difficult_weight6

        urgency_d[task7] = object.urgency_weight7
        importance_d[task7] = object.importance_weight7
        motivation_d[task7] = object.motivation_weight7
        difficult_d[task7] = object.difficult_weight7

        urgency_d[task8] = object.urgency_weight8
        importance_d[task8] = object.importance_weight8
        motivation_d[task8] = object.motivation_weight8
        difficult_d[task8] = object.difficult_weight8

        urgency_d[task9] = object.urgency_weight9
        importance_d[task9] = object.importance_weight9
        motivation_d[task9] = object.motivation_weight9
        difficult_d[task9] = object.difficult_weight9

        urgency_d[task10] = object.urgency_weight10
        importance_d[task10] = object.importance_weight10
        motivation_d[task10] = object.motivation_weight10
        difficult_d[task10] = object.difficult_weight10

        schedule_count = 0
        schedule_l = []
        for day in week:
            schedule_len = len(schedule_d.get(day))
            schedule_count += schedule_len
            schedule_l.append(schedule_len)
        task_len = len(task_l)
        todo_len_l = copy.copy(schedule_l)
        # ①minを取る、②minの中でも先頭を見つける、③入れ替える、④task_lenを-1
        while task_len > 0:
            min_sc = min(todo_len_l) 
            for index, i in enumerate(todo_len_l):
                if i == min_sc:
                    todo_len_l[index] = min_sc + 1
                    task_len -=1
                    break
                    
        capacity_l = [x - y for (x, y) in zip(todo_len_l, schedule_l)]

        quadrant1_l = []
        quadrant2_l = []
        quadrant3_l = []
        quadrant4_l = []

        for task in task_l: 
            urg_score = urgency_d.get(task)
            imp_score = importance_d.get(task)
            mot_score = motivation_d.get(task)
            dif_score = difficult_d.get(task)
            
            # 最優先案件(第1象限)
            if 4<=urg_score and 4<=imp_score:  
                quadrant1_l.append((task, urg_score, imp_score, mot_score, dif_score))
                quadrant1_l.sort(key=lambda x: x[1], reverse=True)
            # 優先案件(第2象限)
            elif urg_score<=3 and 4<=imp_score: 
                quadrant2_l.append((task, urg_score, imp_score, mot_score, dif_score))
                quadrant2_l.sort(key=lambda x: x[1], reverse=True)
            # 後回し案件(第3象限)
            elif urg_score<=3 and imp_score<=3: 
                quadrant3_l.append((task, urg_score, imp_score, mot_score, dif_score))
                quadrant3_l.sort(key=lambda x: x[1], reverse=True)
            # デッドライン案件(第4象限)
            else:
                quadrant4_l.append((task, urg_score, imp_score, mot_score, dif_score))
                quadrant4_l.sort(key=lambda x: x[1], reverse=True)

        total_quadrant_l = quadrant1_l + quadrant2_l + quadrant3_l + quadrant4_l

        # 上から順に振り分ける
        # capacityが0になったら次の日に移行する
        week_d = {}
        for index, capacity in enumerate(capacity_l):
            day_task_l = []
            while True:
                if capacity==0:
                    week_d[week[index]] = day_task_l
                    break
                else:
                    capacity -= 1
                    day_task_l.append(total_quadrant_l.pop(0))
                    week_d[week[index]] = day_task_l
                    
                    
        # 1日のスケジュールを難易度で最適化
        task_d = {}
        for day in week:
            task_order = []
            tasks = week_d.get(day)
            tasks.sort(key=lambda x: x[4], reverse=True) #難易度で降順ソート
            if len(tasks) != 0:
                task_order.append(tasks.pop(-1)) #最初は簡単な案件→難しい、、、、簡単な案件の順に並び替え
            task_order = [i[0] for i in task_order + tasks]
            
            task_d[day] = task_order
            
        # scheduleとtaskの組み合わせで日程
        your_action_plan = DataFrame()
        for day in week:
            sum_l = schedule_d.get(day) + task_d.get(day)
            max_todo = max(todo_len_l)
            gap = max_todo - len(sum_l)
            for _ in range(gap):
                sum_l.append('')
            your_action_plan[day] = sum_l
        your_action_plan = your_action_plan.T

        len_task = len(your_action_plan.T.index)
        d = {}
        for i in range(len_task):
            d[i] = str(i+1) + '番目にやること'
        your_action_plan = your_action_plan.rename(columns=d)
        column = list(your_action_plan.columns)
        your_action_plan['曜日'] = ['日', '月', '火', '水', '木', '金', '土']
        your_action_plan = your_action_plan.reindex(columns=['曜日']+column)

        # 作ったdfをhtmlに変換
        response = HttpResponse(content_type='text/csv; charset=utf8')
        response['Content-Disposition'] = 'attachment; filename=ActionPlan.csv'
        your_action_plan.to_csv(path_or_buf=response, encoding='utf_8_sig', index=None)
        return response  




class Oneteam_Table(DetailView):
    template_name = 'table.html'
    model = Oneteam_model


def analysis(request, pk):
    template_name = 'detail.html'
    object = Oneteam_model.objects.get(pk=pk)
    sun_schedule_l = object.日曜日の予定.splitlines()
    mon_schedule_l = object.月曜日の予定.splitlines()
    tue_schedule_l = object.火曜日の予定.splitlines()
    wed_schedule_l = object.水曜日の予定.splitlines()
    thu_schedule_l = object.木曜日の予定.splitlines()
    fri_schedule_l = object.金曜日の予定.splitlines()
    sat_schedule_l = object.土曜日の予定.splitlines()

    task1 = object.task1
    task2 = object.task2
    task3 = object.task3
    task4 = object.task4
    task5 = object.task5
    task6 = object.task6
    task7 = object.task7
    task8 = object.task8
    task9 = object.task9
    task10 = object.task10

    schedule_d = {'日曜日':sun_schedule_l, 
                  '月曜日':mon_schedule_l,
                  '火曜日':tue_schedule_l,
                  '水曜日':wed_schedule_l,
                  '木曜日':thu_schedule_l,
                  '金曜日':fri_schedule_l,
                  '土曜日':sat_schedule_l,}

    week = ['日曜日', '月曜日', '火曜日', '水曜日', '木曜日', '金曜日', '土曜日']

    task_set = [task1, task2, task3, task4, task5, task6, task7, task8, task9, task10]
    task_l = [i for i in task_set if i != '']
    urgency_d = {}
    importance_d = {}
    motivation_d = {}
    difficult_d = {}    

    urgency_d[task1] = object.urgency_weight1
    importance_d[task1] = object.importance_weight1
    motivation_d[task1] = object.motivation_weight1
    difficult_d[task1] = object.difficult_weight1

    urgency_d[task2] = object.urgency_weight2
    importance_d[task2] = object.importance_weight2
    motivation_d[task2] = object.motivation_weight2
    difficult_d[task2] = object.difficult_weight2

    urgency_d[task3] = object.urgency_weight3
    importance_d[task3] = object.importance_weight3
    motivation_d[task3] = object.motivation_weight3
    difficult_d[task3] = object.difficult_weight3

    urgency_d[task4] = object.urgency_weight4
    importance_d[task4] = object.importance_weight4
    motivation_d[task4] = object.motivation_weight4
    difficult_d[task4] = object.difficult_weight4

    urgency_d[task5] = object.urgency_weight5
    importance_d[task5] = object.importance_weight5
    motivation_d[task5] = object.motivation_weight5
    difficult_d[task5] = object.difficult_weight5

    urgency_d[task6] = object.urgency_weight6
    importance_d[task6] = object.importance_weight6
    motivation_d[task6] = object.motivation_weight6
    difficult_d[task6] = object.difficult_weight6

    urgency_d[task7] = object.urgency_weight7
    importance_d[task7] = object.importance_weight7
    motivation_d[task7] = object.motivation_weight7
    difficult_d[task7] = object.difficult_weight7

    urgency_d[task8] = object.urgency_weight8
    importance_d[task8] = object.importance_weight8
    motivation_d[task8] = object.motivation_weight8
    difficult_d[task8] = object.difficult_weight8

    urgency_d[task9] = object.urgency_weight9
    importance_d[task9] = object.importance_weight9
    motivation_d[task9] = object.motivation_weight9
    difficult_d[task9] = object.difficult_weight9

    urgency_d[task10] = object.urgency_weight10
    importance_d[task10] = object.importance_weight10
    motivation_d[task10] = object.motivation_weight10
    difficult_d[task10] = object.difficult_weight10

    schedule_count = 0
    schedule_l = []
    for day in week:
        schedule_len = len(schedule_d.get(day))
        schedule_count += schedule_len
        schedule_l.append(schedule_len)
    task_len = len(task_l)
    todo_len_l = copy.copy(schedule_l)
    # ①minを取る、②minの中でも先頭を見つける、③入れ替える、④task_lenを-1
    while task_len > 0:
        min_sc = min(todo_len_l) 
        for index, i in enumerate(todo_len_l):
            if i == min_sc:
                todo_len_l[index] = min_sc + 1
                task_len -=1
                break
                
    capacity_l = [x - y for (x, y) in zip(todo_len_l, schedule_l)]

    quadrant1_l = []
    quadrant2_l = []
    quadrant3_l = []
    quadrant4_l = []

    for task in task_l: 
        urg_score = urgency_d.get(task)
        imp_score = importance_d.get(task)
        mot_score = motivation_d.get(task)
        dif_score = difficult_d.get(task)
        
        # 最優先案件(第1象限)
        if 4<=urg_score and 4<=imp_score:  
            quadrant1_l.append((task, urg_score, imp_score, mot_score, dif_score))
            quadrant1_l.sort(key=lambda x: x[1], reverse=True)
        # 優先案件(第2象限)
        elif urg_score<=3 and 4<=imp_score: 
            quadrant2_l.append((task, urg_score, imp_score, mot_score, dif_score))
            quadrant2_l.sort(key=lambda x: x[1], reverse=True)
        # 後回し案件(第3象限)
        elif urg_score<=3 and imp_score<=3: 
            quadrant3_l.append((task, urg_score, imp_score, mot_score, dif_score))
            quadrant3_l.sort(key=lambda x: x[1], reverse=True)
        # デッドライン案件(第4象限)
        else:
            quadrant4_l.append((task, urg_score, imp_score, mot_score, dif_score))
            quadrant4_l.sort(key=lambda x: x[1], reverse=True)

    total_quadrant_l = quadrant1_l + quadrant2_l + quadrant3_l + quadrant4_l

    # 上から順に振り分ける
    # capacityが0になったら次の日に移行する
    week_d = {}
    for index, capacity in enumerate(capacity_l):
        day_task_l = []
        while True:
            if capacity==0:
                week_d[week[index]] = day_task_l
                break
            else:
                capacity -= 1
                day_task_l.append(total_quadrant_l.pop(0))
                week_d[week[index]] = day_task_l
                
                
    # 1日のスケジュールを難易度で最適化
    task_d = {}
    for day in week:
        task_order = []
        tasks = week_d.get(day)
        tasks.sort(key=lambda x: x[4], reverse=True) #難易度で降順ソート
        if len(tasks) != 0:
            task_order.append(tasks.pop(-1)) #最初は簡単な案件→難しい、、、、簡単な案件の順に並び替え
        task_order = [i[0] for i in task_order + tasks]
        
        task_d[day] = task_order
        
    # scheduleとtaskの組み合わせで日程
    your_action_plan = DataFrame()
    for day in week:
        sum_l = schedule_d.get(day) + task_d.get(day)
        max_todo = max(todo_len_l)
        gap = max_todo - len(sum_l)
        for _ in range(gap):
            sum_l.append('')
        your_action_plan[day] = sum_l
    your_action_plan = your_action_plan.T

    len_task = len(your_action_plan.T.index)
    d = {}
    for i in range(len_task):
        d[i] = str(i+1) + '番目にやること'
    your_action_plan = your_action_plan.rename(columns=d)

    # 作ったdfをhtmlに変換
    table = your_action_plan.to_html()
    return render(request, 'table.html', {'table': table})