from PyQt5 import uic,QtWidgets,QtGui
import os
import sys
import random
import pandas as pd
from PyQt5.QtCore import QAbstractTableModel,Qt
import sys
import sqlite3
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
db=sqlite3.connect('lgn.db')
mycurser=db.cursor()
mycurser.execute("create table if not exists userc(username varchar(20),password varchar(20))")
mycurser=db.cursor()
data=pd.read_csv('final_data.csv',encoding='latin1')
data.drop(['comb','actor_1_name', 'actor_2_name', 'actor_3_name'],axis=1,inplace=True)
r=[]
for i in range(0,len(data)):
    r.append(i)
data['index']=r
cb=data['genres']
vec = TfidfVectorizer()
fv=vec.fit_transform(cb)
sim=cosine_similarity(fv)
ml=data['movie_title'].tolist()

def hel():
    image.close()
    pro.show()  

def ret():
    pro.er.clear()
    pro.close()
    image.show()

def udt1():
    uidf=pro.un.text().lower()
    pwdn=pro.pw.text().lower()
    if len(uidf)==0:
        pro.un.clear()
        pro.pw.clear()
        pro.er.setText('Update not possible for blank username')
    else:
        mycurser.execute(f"select username from userc where username='{uidf}'")
        res5=mycurser.fetchall()
        if len(res5)==0:
            pro.er.setText('Incorrect Username!!!')
        elif len(pwdn)<8:
            pro.un.clear()
            pro.pw.clear()
            pro.er.setText('update not possible.Password must be 8 characters Long')
        else:
            mycurser.execute(f"update userc set password='{pwdn}' where username='{uidf}';")
            db.commit()
            pro.un.clear()
            pro.pw.clear()
            pro.er.setText('Password changed successfully')

def msg(uidf):
    lp.er.setText('User deleted successfully')
    # lp.er.clear()

def dlt():
    uidf=pro.un.text().lower()
    if len(uidf)==0:
        pro.er.setText('Delete cant be possible for blank Username')
        pro.un.clear()
    else:
        mycurser.execute(f"select username from userc where username='{uidf}'")
        res5=mycurser.fetchall()
        if len(res5)==0:
            pro.er.setText('Username not found!!!')
            pro.un.clear()
        else:
            mycurser.execute(f"delete from userc where username='{uidf}'")
            db.commit()
            pro.un.clear()
            pro.er.clear()
            pro.close()
            lp.show()
            msg(uidf)

def lbt():
    pro.un.clear()
    pro.er.clear()
    pro.close()
    print('User logout successfully')
    lp.show()

def prc():
    sup.er.clear()
    uid=sup.un.text().lower()
    pwd=sup.pw.text().lower()
    if len(uid)==0:
        sup.er.setText('Username cant be blank')
        sup.un.clear()
        sup.pw.clear()
    elif len(pwd)==0:
        sup.er.setText('Password cant be blank')
        sup.un.clear()
        sup.pw.clear()
    elif uid=='admin':
        sup.er.setText('Username cant be admin')
        sup.un.clear()
        sup.pw.clear()
    else:
        mycurser.execute(f"select username from userc where username='{uid}'")
        res3=mycurser.fetchall()
        if len(res3)==0:
            if(len(pwd)>=8):
                mycurser.execute(f"insert into userc values('{uid}','{pwd}')")
                db.commit()
                sup.er.clear()
                sup.close()
                lp.show()
                lp.er.setText('User cretaed successfully')
            else:
                sup.er.setText('Password is too short. It must be 8 characters Long')
                sup.pw.clear()
        else:
            for x in res3:
                print(x)
                if x.count(uid)==1:
                    sup.un.clear()
                    sup.pw.clear()
                    sup.er.setText('username exist change it')
                    print('username exist change it')
            
def prc2():
    sup.close()
    lp.show()

def sp():
    lp.un.clear()
    lp.pw.clear()
    lp.er.clear()
    lp.close()
    sup.show()
    sup.un.clear()
    sup.pw.clear()

def prc3(uid):
    lp.un.clear()
    lp.pw.clear()
    lp.er.clear()
    image.pp.setText(f"User: {uid.upper()}")
    genr()

def mye():
    lp.er.clear()
    uid=lp.un.text().lower()
    pwd=lp.pw.text().lower()
    if len(uid)==0:
        lp.er.setText('Username cant be blank')
    elif len(pwd)==0:
        lp.er.setText('Password cant be blank')
    else:
        mycurser.execute(f"select username from userc where username='{uid}'")
        res1=mycurser.fetchall()
        if len(res1)==0:
            lp.er.setText('Invalid creds')
            lp.un.clear()
            lp.pw.clear()
        mycurser.execute(f"select password from userc where username='{uid}'")
        res2=mycurser.fetchall()
        for x in res1:
            if uid in x:
                if uid=='admin':
                    if len(pwd)>0:
                        for y in res2:
                            if pwd in y:
                                print("Admin is logged in")
                                lp.un.clear()
                                lp.un.clear()
                                lp.pw.clear()
                                lp.close()
                                ad.show()
                            else:
                                lp.un.clear()
                                lp.pw.clear()
                                lp.er.setText('Invalid creds')
                else:
                    if len(pwd)>0:
                        for y in res2:
                            if pwd in y and uid in x:
                                print(f"User {uid.upper()} login succesful")
                                lp.un.clear()
                                lp.pw.clear()
                                lp.close()
                                image.show()
                                prc3(uid)
                            else:
                                lp.un.clear()
                                lp.pw.clear()
                                lp.er.setText('Invalid creds')
            else:
                print('invalid creds')
                lp.er.setText('Invalid creds')

def ptt():
    image.close()
    t2.show()

def prt(q1,o1):
    row1=0
    row2=0
    t2.dmn.setColumnCount(1)
    t2.dmn.setRowCount(len(q1))
    t2.dmn.setColumnWidth(0,500)
    t2.gnr2.setColumnCount(1)
    t2.gnr2.setRowCount(len(o1))
    t2.gnr2.setColumnWidth(0,500)
    for i in q1:
        t2.mn_2.setText(f"Movies you might also like by {hel1[len(hel1)-1].upper()}")
        t2.dmn.setItem(row1,0,QtWidgets.QTableWidgetItem(i.upper()))
        row1=row1+1
    for j in o1:
        t2.gnr2.setItem(row2,0,QtWidgets.QTableWidgetItem(j.upper()))
        row2=row2+1
    image.tw.clearSelection()
    q1.clear()
    o1.clear()
    ptt()

global hel1
hel1=[]
def prr3(z):
    hel2=[]
    q1=[]
    q2=[]
    o1=[]
    mn=data[data['movie_title']==z]['director_name']
    fc=difflib.get_close_matches(z,ml)
    cm=fc[0]
    im=data[data.movie_title==cm]['index'].values[0]
    simscr=list(enumerate(sim[im]))
    ssm=sorted(simscr,key=lambda x:x[1],reverse=True)
    u=1
    for movie in ssm:
        index=movie[0]
        title=data[data.index==index]['movie_title'].values[0]
        if u<=30:
            q2.append(title)
            u+=1
    for n in q2:
        if n not in m:
            o1.append(n)
    for i in mn:
        hel1.append(i)
        p1=data[data['director_name']==hel1[len(hel1)-1]]['movie_title']
    for i in range(0,len(p1)):
            q1.append(p1.values[i])
    prt(q1,o1)

global ty
ty=[]
global wlo
wlo=[]
def prr():
    for i in rw:
        t2.mn.setText(m[i].upper())
        wlo.append(m[i])
        for root, dirs, files in os.walk("projimages"):
             for subdir in dirs:
                for file in os.listdir(os.path.join(root, subdir)):
                    h=f"{m[i]}.jpg"
                    j=f"{m[i]}.jpeg"
                    k=f"{m[i]}.png"
                    if (file == h) |(file==j)|(file==k):
                        kkk=os.path.join(root,subdir,m[i])
                        np= kkk.replace(os.path.sep, "/")
                        t2.img.setPixmap(QtGui.QPixmap(f"{np}"))
                        break
        prr3(m[i])

def prr2():
    rw.clear()
    for hh in image.tw.selectedIndexes():
        rw.clear()
        rw.append(hh.row())
    prr()

def ptr4():
    t2.close()
    image.show()

global rw
rw=[]
def dspl(res1):
    if res1['genres'].value_counts().sum()==0:
        genr()
    else:
        l=[]
        global m
        m=[]
        for i in range(0,len(res1)):
            p=res1['genres'].values[i]
            q=res1['movie_title'].values[i]
            l.append(p)
            m.append(q)
        row=0
        image.tw.setRowCount(len(res1))
        for res1 in res1:
            for i in range(0,len(l)):
                image.tw.setItem(row,0,QtWidgets.QTableWidgetItem(m[i].upper()))
                row=row+1
        prr2()

def genr():
    image.tw.clearSelection()
    t2.mn.clear()
    t2.close()
    ger=['Action', 'Adventure', 'Animation', 'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Family', 'Fantasy', 
    'Fiction Film-Noir', 'Game-Show', 'History', 'Horror', 'Movie', 'Music','Musical', 'Mystery', 'News', 'Reality-TV', 
    'Romance', 'Sci-Fi', 'Science', 'Short', 'Sport', 'TV', 'Thriller', 'War', 'Western', 'Romance']
    l = list(range(len(ger)))
    out=[]
    for _ in range(4):
        x = random.choice(ger)
        if x not in out:
            out.append(x)
    out.sort()
    res=' '.join(out)
    p=res
    res1=data[data['genres']==res]
    if res1['genres'].value_counts().sum()==1:
        genr()
    else:
        image.tw.setColumnCount(1)
        image.tw.setColumnWidth(0,500)
        image.tw.setColumnWidth(1,510)
        image.pp_3.setText('Genres:')
        image.pp_2.setText(f" {p.upper()}")
        dspl(res1)

def lt2():
    ad.close()
    print('admin logout successfully')
    ad.uls.setRowCount(0)
    lp.show()

def fh2():
    global ul
    ul=[]
    ad.uls.setColumnCount(1)
    ad.uls.setColumnWidth(0,500)
    mycurser.execute("select username from userc where username!='admin'")
    lst=mycurser.fetchall()
    ad.uls.setRowCount(len(lst))
    rw3=0
    for x in lst:
        for uif in x:
            ul.append(uif)
    for y in range(0,len(lst)):
        ad.uls.setItem(rw3,0,QtWidgets.QTableWidgetItem(ul[y].upper()))
        rw3+=1

def ds1():
    for t in lo:
        du=ul[t]
        eq=mycurser.execute(f"delete from userc where username='{du}'")
        db.commit()
        ad.pgb.setText(f'User: {du} is deleted successfully')
        ad.uls.clearSelection()
        fh2()

global lo
lo=[]
def dd2():
    for j in ad.uls.selectedIndexes():
        lo.clear()
        lo.append(j.row())
    ds1()

def wlt():
    
    t3.ml.setColumnCount(1)
    t3.ml.setColumnWidth(0,500)
    t3.ml.setRowCount(len(wlo))
    rw4=0
    for i in wlo:
        for y in range(0,len(wlo)):
            t3.ml.setItem(rw4,0,QtWidgets.QTableWidgetItem(wlo[y].upper()))
            rw4=rw4+1
    image.close()
    t3.show()

def oo():
    t3.close()
    image.show()

j=QtWidgets.QApplication([])
lp=uic.loadUi('lp.ui')
image=uic.loadUi('2nd.ui')
ad=uic.loadUi('admin.ui')
t2=uic.loadUi('mpfl.ui')
sup=uic.loadUi('sup.ui')
pro=uic.loadUi('prfl.ui')
t3=uic.loadUi('wl.ui')
t3.setFixedSize(1123, 830)
image.setFixedSize(1123, 830)
pro.setFixedSize(1123, 830)
lp.setFixedSize(1123, 830)
t2.setFixedSize(1123, 830)
ad.setFixedSize(1123, 830)
t2.setFixedSize(1123, 830)
sup.setFixedSize(1123, 830)
t3.setWindowIcon(QtGui.QIcon('pjkt.jpg'))
t3.setStyleSheet("#centralwidget{background-image:url(image.jpg);}")
image.setStyleSheet("#centralwidget{background-image:url(image.jpg);}")
lp.setStyleSheet("#centralwidget{background-image:url(image.jpg);}")
ad.setStyleSheet("#centralwidget{background-image:url(image.jpg);}")
t2.setStyleSheet("#centralwidget{background-image:url(image.jpg);}")
sup.setStyleSheet("#centralwidget{background-image:url(image.jpg);}")
pro.setStyleSheet("#centralwidget{background-image:url(image.jpg);}")
# image.setFixedSize(1200, 1400)
lp.setWindowIcon(QtGui.QIcon('pjkt.jpg'))
sup.setWindowIcon(QtGui.QIcon('pjkt.jpg'))
pro.setWindowIcon(QtGui.QIcon('pjkt.jpg'))
t2.setWindowIcon(QtGui.QIcon('pjkt.jpg'))
image.setWindowIcon(QtGui.QIcon('pjkt.jpg'))
ad.setWindowIcon(QtGui.QIcon('pjkt.jpg'))
ad.setWindowTitle('Admin Panel')
lp.setWindowTitle('Login')
sup.setWindowTitle('SignUp')
pro.setWindowTitle('Settings')
t2.setWindowTitle('Info')
image.setWindowTitle('Home')
t3.setWindowTitle('Profile')
lp.show()
t2.gn_3.clicked.connect(ptr4)
lp.lg.clicked.connect(mye)
lp.su.clicked.connect(sp)
sup.su.clicked.connect(prc)
sup.lg.clicked.connect(prc2)
image.hh.clicked.connect(hel)
pro.lgt.clicked.connect(lbt)
image.gn.clicked.connect(genr)
pro.upp.clicked.connect(udt1)
image.gn_2.clicked.connect(prr2)
ad.lot.clicked.connect(lt2)
ad.fh.clicked.connect(fh2)
ad.d2.clicked.connect(dd2)
pro.hm.clicked.connect(ret)
pro.da.clicked.connect(dlt)
t3.hm.clicked.connect(oo)
image.wll.clicked.connect(wlt)
sys.exit(j.exec_())