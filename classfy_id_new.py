import json
import os
class lda_learning():
    def classfy_city_data(self):
        '''
           Divide the data set according to the number of days of trip,
           divided into 4 days, 4-5 days, 6-7 days, 8-10 days,
           10 days and above,five kinds of situations.
           the format of each line:id trip-id word word word...
           The length of word is 4 hours, rounding up.
        '''
        time_sum=0.0
        rid1=0
        rid2=0
        rid3=0
        rid4=0
        rid5=0
        citys_arry=[]
        with open('../data/path_json_with_time1.json',encoding='utf-8') as fd:
            loaded = json.load(fd)
        outfile1=open('../data/cityHours_doc_train_dis_4.txt','w',encoding='utf-8')
        outfile2=open('../data/cityHours_doc_train_dis_4-5.txt','w',encoding='utf-8')
        outfile3=open('../data/cityHours_doc_train_dis_6-7.txt','w',encoding='utf-8')
        outfile4=open('../data/cityHours_doc_train_dis_8-10.txt','w',encoding='utf-8')
        outfile5=open('../data/cityHours_doc_train_dis_10.txt','w',encoding='utf-8')
        for path in loaded:
            citys_arry=[]
            citylist=''
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
                    if int(time_sum) == 0:
                        time_sum=4
                    citylist+=(str(place_name)+' ')*int((time_sum/4))
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
        fd.close()
        outfile1.close()
        outfile2.close()
        outfile3.close()
        outfile4.close()
        outfile5.close()
    def data_format(self):
        '''
           format training data sets
        '''
        #copy data file
        os.system("cp ../data/cityHours_doc_train_dis_4.txt ../../../tools/warplda/data")
        os.system("cp ../data/cityHours_doc_train_dis_4-5.txt ../../../tools/warplda/data")
        os.system("cp ../data/cityHours_doc_train_dis_6-7.txt ../../../tools/warplda/data")
        os.system("cp ../data/cityHours_doc_train_dis_8-10.txt ../../../tools/warplda/data")
        os.system("cp ../data/cityHours_doc_train_dis_10.txt ../../../tools/warplda/data")
        #format data sets
        os.system("cd ../data;../../../tools/warplda/release/src/format -input ./warplda/data/cityHours_doc_train_dis_4.txt -prefix train4")
        os.system("cd ../data;../../../tools/warplda/release/src/format -input ./warplda/data/cityHours_doc_train_dis_4-5.txt -prefix train4_5")
        os.system("cd ../data;../../../tools/warplda/release/src/format -input ./warplda/data/cityHours_doc_train_dis_6-7.txt -prefix train6_7")
        os.system("cd ../data;../../../tools/warplda/release/src/format -input ./warplda/data/cityHours_doc_train_dis_8-10.txt -prefix train8_10")
        os.system("cd ../data;../../../tools/warplda/release/src/format -input ./warplda/data/cityHours_doc_train_dis_10.txt -prefix train10")
    def training(self,days,k,niter):
        '''
           train data sets and get topic model
           :param days: the kind of data set
           (e.g. 4:4 days, 4_5:4-5 days, 6_7:6-7 days, 8_10:8-10 days, 10:10 days)
           :param k: the number of topics
           :param niter: the number of iterations
        '''
        os.system("cd ../data;../../../tools/warplda/release/src/warplda --prefix train"+days+" --k "+k+" --niter "+niter)
        #os.system("mv ../tools/warplda/release/src/train"+days+".info.full.txt train6_7.info11.full.txt")
