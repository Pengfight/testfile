import json
import os

def load_city_data():
    time_sum=0.0
    rid1=0
    rid2=0
    rid3=0
    rid4=0
    rid5=0
    citys_arry=[]
    with open('path_json_with_time1.json',encoding='utf-8') as fd:
        loaded = json.load(fd)
    outfile1=open('cityHours_doc_train_dis_4_new.txt','w',encoding='utf-8')
    outfile2=open('cityHours_doc_train_dis_4-5_new.txt','w',encoding='utf-8')
    outfile3=open('cityHours_doc_train_dis_6-7_new.txt','w',encoding='utf-8')
    outfile4=open('cityHours_doc_train_dis_8-10_new.txt','w',encoding='utf-8')
    outfile5=open('cityHours_doc_train_dis_10_new.txt','w',encoding='utf-8')
    for path in loaded:
        '''rid+=1
        tid+=1
        outfile1.write(str(rid)+' '+str(tid)+' ')'''
        citys_arry=[]
        citylist=''
        #citys=[]
        for place in path:
            time_sum=0.0
            if place.get(u'type') == 'place':
                place_name = place.get(u'name')
                trip_id=place.get(u'plan_id')
                if place_name not in citys_arry:
                    citys_arry.append(place_name)
                trave_time=place.get(u'travel_times')
                for i in range(len(trave_time)):
                    time_sum+=float(trave_time[i])
                #print(time_sum)
                if int(time_sum) == 0:
                    time_sum=4
                #citys.append((str(place_name)+' ')*int((time_sum/4)))
                citylist+=(str(place_name)+' ')*int((time_sum/4))
                #outfile.write(citys)
                #city_timeDic.setdefault(place_name,[]).append(time_sum)
                #citylist.append(str(place_name))
                #citylist+=(str(place_name)+' ')*days
                #print(place_name)
        if len(citys_arry)<4:
            rid1+=1
            outfile1.write(str(rid1)+' '+str(trip_id)+' ')
            outfile1.write(citylist)
            outfile1.write('\n')
        elif len(citys_arry)<=5:
            rid2+=1
            outfile2.write(str(rid2)+' '+str(trip_id)+' ')
            outfile2.write(citylist)
            outfile2.write('\n')
        elif len(citys_arry)<=7:
            rid3+=1
            outfile3.write(str(rid3)+' '+str(trip_id)+' ')
            outfile3.write(citylist)
            outfile3.write('\n')
        elif len(citys_arry)<=10:
            rid4+=1
            outfile4.write(str(rid4)+' '+str(trip_id)+' ')
            outfile4.write(citylist)
            outfile4.write('\n')
        else:
            rid5+=1
            outfile5.write(str(rid5)+' '+str(trip_id)+' ')
            outfile5.write(citylist)
            outfile5.write('\n')
        #outfile.write('\n')
        #print(len(citys_arry))
    fd.close()
    outfile1.close()
    outfile2.close()
    outfile3.close()
    outfile4.close()
    outfile5.close()
    #print(timeDic)
    #return timeDic
load_city_data()
#write_citylist(city)
