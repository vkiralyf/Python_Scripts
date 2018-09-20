#Import all the necessary libraries
from bs4 import BeautifulSoup
from requests import get
from time import sleep
from random import randint
from time import time
from IPython.core.display import clear_output
from warnings import warn
import os
######E-Mail Notificaiton Setup#############
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
##############################################

################Functions are defined##################
def deviationcalc(qw, qe, qr,invrt,prjtname,link):
    n1 = qw[0].strip('V')
    n2 =qw[1].strip('V')
    n3 = qw[2].strip('V')
    # print (n)
    deviation = float(n1) * 0.05
    newval = float(n1) + deviation
    # print(newval)
    newvalb = float(n1) - deviation
    # print(newvalb)
    # if the current value is greater than the newvalue send an email notifying the party in charge that there is a 5% deviation in the voltage
    if float(n2) >= newval or float(n2) < newvalb:
        m = 'if1-The current inverter {i} for project: {p} is  experiencing significant deviation in its voltage value. Please take a look {l} to see if any adjustments are needed.'.format(i=invrt, p=prjtname, l=link)
        cwd = os.path.dirname(os.path.realpath(__file__))
        filename = os.path.join(cwd, 'testmsg.txt')
        with open(filename, 'r+') as template_file:
            template_file.write(m)
            template_file.seek(0)
            template_file_content = template_file.read()
            template_file.close()
        ######E-Mail Notificaiton Setup############
        my_address = 'victor.kiralyfalvy@abundantsolarenergy.com'
        password = '8Abundant5'
        toaddr = 'victor.kiralyfalvy@abundantsolarenergy.com'
        msg = MIMEMultipart()
        msg['From'] = my_address
        msg['To'] = toaddr
        msg['Subject'] = "Inverter Alert"
        body = template_file_content
        msg.attach(MIMEText(body, 'plain'))
        server = smtplib.SMTP('smtp.office365.com', 587)
        server.starttls()
        server.login(my_address, password)
        text = msg.as_string()
        server.sendmail(my_address, toaddr, text)
        server.quit()
        ##############################################
    else:
        print("There is no significant deviation in the Voltage Value 2")
    if float(n3) >= newval or float(n3) < newvalb:
        m = 'if2-The current inverter {i} for project: {p} is  experiencing significant deviation in its voltage value. Please take a look {l} to see if any adjustments are needed.'.format(i=invrt, p=prjtname, l=link)
        cwd = os.path.dirname(os.path.realpath(__file__))
        filename = os.path.join(cwd, 'testmsg.txt')
        with open(filename, 'r+') as template_file:
            template_file.write(m)
            template_file.seek(0)
            template_file_content = template_file.read()
            template_file.close()
        ######E-Mail Notificaiton Setup############
        my_address = 'victor.kiralyfalvy@abundantsolarenergy.com'
        password = '8Abundant5'
        toaddr = 'victor.kiralyfalvy@abundantsolarenergy.com'
        msg = MIMEMultipart()
        msg['From'] = my_address
        msg['To'] = toaddr
        msg['Subject'] = "Inverter Alert"
        body = template_file_content
        msg.attach(MIMEText(body, 'plain'))
        server = smtplib.SMTP('smtp.office365.com', 587)
        server.starttls()
        server.login(my_address, password)
        text = msg.as_string()
        server.sendmail(my_address, toaddr, text)
        server.quit()
        ##############################################
    else:
        print("There is no significant deviation in the Voltage Value 3")
    u = qe[0].strip('A')
    u1 = qe[1].strip('A')
    u2 = qe[2].strip('A')
    dev = float(u) * 0.10
    newvala = float(u) + dev
    newvalc = float(u) - dev
    # if the current value is greater than the newvalue send an email notifying the party in charge that there is a 5% deviation in the voltage
    if float(u1) >= newvala or float(u1) < newvalc:
        m = 'if3-The current inverter {i} for project: {p} is  experiencing significant deviation in its amparage value. Please take a look {l} to see if any adjustments are needed.'.format(i=invrt, p=prjtname, l=link)
        cwd = os.path.dirname(os.path.realpath(__file__))
        filename = os.path.join(cwd, 'testmsg.txt')
        with open(filename, 'r+') as template_file:
            template_file.write(m)
            template_file.seek(0)
            template_file_content = template_file.read()
            template_file.close()
        ######E-Mail Notificaiton Setup############
        my_address = 'victor.kiralyfalvy@abundantsolarenergy.com'
        password = '8Abundant5'
        toaddr = 'victor.kiralyfalvy@abundantsolarenergy.com'
        msg = MIMEMultipart()
        msg['From'] = my_address
        msg['To'] = toaddr
        msg['Subject'] = "Inverter Alert"
        body = template_file_content
        msg.attach(MIMEText(body, 'plain'))
        server = smtplib.SMTP('smtp.office365.com', 587)
        server.starttls()
        server.login(my_address, password)
        text = msg.as_string()
        server.sendmail(my_address, toaddr, text)
        server.quit()
        ##############################################
    else :
        print("There is no significant deviation in the Amparage Value 2")
    if float(u2) >= newvala or float(u2) < newvalc:
        m = 'if4-The current inverter {i} for project: {p} is  experiencing significant deviation in its amparage value. Please take a look {l} to see if any adjustments are needed.'.format(
            i=invrt, p=prjtname, l=link)
        cwd = os.path.dirname(os.path.realpath(__file__))
        filename = os.path.join(cwd, 'testmsg.txt')
        with open(filename, 'r+') as template_file:
            template_file.write(m)
            template_file.seek(0)
            template_file_content = template_file.read()
            template_file.close()
        ######E-Mail Notificaiton Setup############
        my_address = 'victor.kiralyfalvy@abundantsolarenergy.com'
        password = '8Abundant5'
        toaddr = 'victor.kiralyfalvy@abundantsolarenergy.com'
        msg = MIMEMultipart()
        msg['From'] = my_address
        msg['To'] = toaddr
        msg['Subject'] = "Inverter Alert"
        body = template_file_content
        msg.attach(MIMEText(body, 'plain'))
        server = smtplib.SMTP('smtp.office365.com', 587)
        server.starttls()
        server.login(my_address, password)
        text = msg.as_string()
        server.sendmail(my_address, toaddr, text)
        server.quit()
        ##############################################
    else:
        print("There is no significant deviation in the Amparage Value 3")
    print("This is the current power list " + str(qr))
    if len(qr) <=1:
        cp=float(qr[0])
        deev=cp*0.05
        posdeev= cp+deev
        negdeev= cp-deev
        if cp >= posdeev or cp < negdeev:
            m = 'if5-The current inverter {i} for project: {p} is  experiencing significant deviation in its current power value. Please take a look {l} to see if any adjustments are needed.'.format(i=invrt, p=prjtname, l=link)
            cwd = os.path.dirname(os.path.realpath(__file__))
            filename = os.path.join(cwd, 'testmsg.txt')
            with open(filename, 'r+') as template_file:
                template_file.write(m)
                template_file.seek(0)
                template_file_content = template_file.read()
                template_file.close()
            ######E-Mail Notificaiton Setup############
            my_address = 'victor.kiralyfalvy@abundantsolarenergy.com'
            password = '8Abundant5'
            toaddr = 'victor.kiralyfalvy@abundantsolarenergy.com'
            msg = MIMEMultipart()
            msg['From'] = my_address
            msg['To'] = toaddr
            msg['Subject'] = "Inverter Alert"
            body = template_file_content
            msg.attach(MIMEText(body, 'plain'))
            server = smtplib.SMTP('smtp.office365.com', 587)
            server.starttls()
            server.login(my_address, password)
            text = msg.as_string()
            server.sendmail(my_address, toaddr, text)
            server.quit()
            ##############################################

        else:
            print("No Deviation Everything is Normal!")

    else:
        for p in pwrcomparison:
            devi = float(p) * 0.05
            newvald = float(p) + devi
            newvale = float(p) - devi
            if p >= newvald or p < newvale :
                m = 'else1-The current inverter {i} for project: {p} is  experiencing significant deviation in its current power value. Please take a look {l} to see if any adjustments are needed.'.format(i=invrt, p=prjtname, l=link)
                cwd = os.path.dirname(os.path.realpath(__file__))
                filename = os.path.join(cwd, 'testmsg.txt')
                with open(filename, 'r+') as template_file:
                    template_file.write(m)
                    template_file.seek(0)
                    template_file_content = template_file.read()
                    template_file.close()
                ######E-Mail Notificaiton Setup############
                my_address = 'victor.kiralyfalvy@abundantsolarenergy.com'
                password = '8Abundant5'
                toaddr = 'victor.kiralyfalvy@abundantsolarenergy.com'
                msg = MIMEMultipart()
                msg['From'] = my_address
                msg['To'] = toaddr
                msg['Subject'] = "Inverter Alert"
                body = template_file_content
                msg.attach(MIMEText(body, 'plain'))
                server = smtplib.SMTP('smtp.office365.com', 587)
                server.starttls()
                server.login(my_address, password)
                text = msg.as_string()
                server.sendmail(my_address, toaddr, text)
                server.quit()
                ##############################################
            else :
                print("There is no significant deviation in the Current Power")
def Fronius(p, sid, d, psa, psv):
    print (p + " Inverter: " + sid)
    ca = d[11]
    psa.append(ca)
    print (ca)
    cb = d[12]
    psa.append(cb)
    print (cb)
    cc = d[13]
    psa.append(cc)
    print (cc)
    va = d[14]
    psv.append(va)
    print (va)
    vb = d[15]
    psv.append(vb)
    print (vb)
    vc = d[16]
    psv.append(vc)
    print(vc)
def Sungrow(pn,shid,da,pasa,pasv):
    print (pn + " Inverter: " + shid)
    if shid=="7259":
        ca = da[18]
        pasa.append(ca)
        print (ca)
        cb = da[19]
        pasa.append(cb)
        print (cb)
        cc = da[20]
        pasa.append(cc)
        print (cc)
        va = da[15]
        pasv.append(va)
        print (va)
        vb = da[16]
        pasv.append(vb)
        print (vb)
        vc = da[17]
        pasv.append(vc)
        print(vc)
    else:
        ca = da[28]
        pasa.append(ca)
        print (ca)
        cb = da[29]
        pasa.append(cb)
        print (cb)
        cc = da[30]
        pasa.append(cc)
        print (cc)
        va = da[25]
        pasv.append(va)
        print (va)
        vb = da[26]
        pasv.append(vb)
        print (vb)
        vc = da[27]
        pasv.append(vc)
        print(vc)
def Huawei(pnn,shidd,daa,pasaa,pasvv):
    print (pnn + " Inverter: " + shidd)
    ca = daa[19]
    pasaa.append(ca)
    print (ca)
    cb = daa[20]
    pasaa.append(cb)
    print (cb)
    cc = daa[21]
    pasaa.append(cc)
    print (cc)
    va = daa[16]
    pasvv.append(va)
    print (va)
    vb = daa[17]
    pasvv.append(vb)
    print (vb)
    vc = daa[18]
    pasvv.append(vc)
    print(vc)
def Xantrex(prjn,sho,dat,passa,passv):
    print (prjn + " Inverter: " + sho)
    ca = dat[8]
    passa.append(ca)
    print (ca)
    cb = dat[9]
    passa.append(cb)
    print (cb)
    cc = dat[10]
    passa.append(cc)
    print (cc)
    va = dat[5]
    passv.append(va)
    print (va)
    vb = dat[6]
    passv.append(vb)
    print (vb)
    vc = dat[7]
    passv.append(vc)
    print(vc)
#Special container for weston3655 due to the fact that the font class changes and all the inverters are on one webpage
def Weston(wd,invd,westpower):
    #loops through each inverter on the page and scraps the voltage, amparage values
    # the deviation calculation function is called at the end of each if, elif or else statment depending on the current inverter
    #the voltage and amparage values are appended to the two global lists called passmorev and passmorea then are called in the deviation calculation function
    # the current power values are passed into the deviation calculation function as westpower which holds a list of all the power values for the 5 inverters
    for inverter in invd:
        if inverter=="Sungrow SG60KU-M #1":
            v1=wd[26].strip('V')
            passmorev.append(v1)
            v2=wd[27].strip('V')
            passmorev.append(v2)
            v3=wd[28].strip('V')
            passmorev.append(v3)
            a1=wd[29].strip('A')
            passmorea.append(a1)
            a2=wd[30].strip('A')
            passmorea.append(a2)
            a3=wd[31].strip('A')
            passmorea.append(a3)
            deviationcalc(passmorev, passmorea,westpower,inverter, pname, x)
        elif inverter=="Sungrow SG60KU-M #2":
            v1 =wd[56].strip('V')
            passmorev.append(v1)
            v2 =wd[57].strip('V')
            passmorev.append(v2)
            v3 =wd[58].strip('V')
            passmorev.append(v3)
            a1 =wd[59].strip('A')
            passmorea.append(a1)
            a2 =wd[60].strip('A')
            passmorea.append(a2)
            a3 =wd[61].strip('A')
            passmorea.append(a3)
            deviationcalc(passmorev, passmorea, westpower, inverter, pname, x)
        elif inverter== "Sungrow SG60KU-M #3":
            v1 =wd[126].strip('V')
            passmorev.append(v1)
            v2 =wd[127].strip('V')
            passmorev.append(v2)
            v3 =wd[128].strip('V')
            passmorev.append(v3)
            a1 =wd[129].strip('A')
            passmorea.append(a1)
            a2 =wd[130].strip('A')
            passmorea.append(a2)
            a3 =wd[131].strip('A')
            passmorea.append(a3)
            deviationcalc(passmorev, passmorea, westpower, inverter, pname, x)
        elif inverter == "Sungrow SG60KU-M #4":
            v1 =wd[156].strip('V')
            passmorev.append(v1)
            v2 =wd[157].strip('V')
            passmorev.append(v2)
            v3 =wd[158].strip('V')
            passmorev.append(v3)
            a1 =wd[159].strip('A')
            passmorea.append(a1)
            a2 =wd[160].strip('A')
            passmorea.append(a2)
            a3 =wd[161].strip('A')
            passmorea.append(a3)
            deviationcalc(passmorev, passmorea, westpower, inverter, pname, x)
        elif inverter == "Sungrow SG60KU-M #5":
            v1 =wd[226].strip('V')
            passmorev.append(v1)
            v2 =wd[227].strip('V')
            passmorev.append(v2)
            v3 =wd[228].strip('V')
            passmorev.append(v3)
            a1 =wd[229].strip('A')
            passmorea.append(a1)
            a2 =wd[230].strip('A')
            passmorea.append(a2)
            a3 =wd[231].strip('A')
            passmorea.append(a3)
            deviationcalc(passmorev, passmorea, westpower, inverter, pname, x)
##########################################
#List of inverters for each project
#"http://weston3655b.solarvu.net/green/solarvu/performSInverter.php?ac=101634"
mainls=["http://weston3655b.solarvu.net/green/solarvu/performSInverter.php?ac=101634","http://weston3655a.solarvu.net/green/solarvu/inverterLog.php?ac=101635&showtime=7251","http://weston3655a.solarvu.net/green/solarvu/inverterLog.php?ac=101635&showtime=7252",
                "http://weston3655a.solarvu.net/green/solarvu/inverterLog.php?ac=101635&showtime=7253","http://weston3655a.solarvu.net/green/solarvu/inverterLog.php?ac=101635&showtime=7254",
                "http://weston3655a.solarvu.net/green/solarvu/inverterLog.php?ac=101635&showtime=7255","http://weston3655a.solarvu.net/green/solarvu/inverterLog.php?ac=101635&showtime=7256",
                "http://weston3655a.solarvu.net/green/solarvu/inverterLog.php?ac=101635&showtime=7257","http://weston3655a.solarvu.net/green/solarvu/inverterLog.php?ac=101635&showtime=7258",
                "http://weston3655a.solarvu.net/green/solarvu/inverterLog.php?ac=101635&showtime=7259","http://scott21.solarvu.net/green/solarvu/inverterLog.php?ac=101633&showtime=7231","http://scott21.solarvu.net/green/solarvu/inverterLog.php?ac=101633&showtime=7220",
                "http://scott21.solarvu.net/green/solarvu/inverterLog.php?ac=101633&showtime=7221","http://scott21.solarvu.net/green/solarvu/inverterLog.php?ac=101633&showtime=7222",
                "http://scott21.solarvu.net/green/solarvu/inverterLog.php?ac=101633&showtime=7223","http://scott21.solarvu.net/green/solarvu/inverterLog.php?ac=101633&showtime=7224",
                "http://scott21.solarvu.net/green/solarvu/inverterLog.php?ac=101633&showtime=7225","http://scott21.solarvu.net/green/solarvu/inverterLog.php?ac=101633&showtime=7226",
                "http://scott21.solarvu.net/green/solarvu/inverterLog.php?ac=101633&showtime=7227","http://scott21.solarvu.net/green/solarvu/inverterLog.php?ac=101633&showtime=7228",
                "http://scott21.solarvu.net/green/solarvu/inverterLog.php?ac=101633&showtime=7229","http://scott21.solarvu.net/green/solarvu/inverterLog.php?ac=101633&showtime=7230",
                "http://scott21.solarvu.net/green/solarvu/inverterLog.php?ac=101633&showtime=7231","http://scott21.solarvu.net/green/solarvu/inverterLog.php?ac=101633&showtime=7232",
                "http://scott21.solarvu.net/green/solarvu/inverterLog.php?ac=101633&showtime=7233","http://scott21.solarvu.net/green/solarvu/inverterLog.php?ac=101633&showtime=7234",
                "http://scott21.solarvu.net/green/solarvu/inverterLog.php?ac=101633&showtime=7235","http://scott21.solarvu.net/green/solarvu/inverterLog.php?ac=101633&showtime=7236",
                "http://scott21.solarvu.net/green/solarvu/inverterLog.php?ac=101633&showtime=7237","http://scott21.solarvu.net/green/solarvu/inverterLog.php?ac=101633&showtime=7238",
                "http://scott21.solarvu.net/green/solarvu/inverterLog.php?ac=101633&showtime=7239","http://7090tranmere.solarvu.net/green/solarvu/inverterLog.php?ac=101375&showtime=4601","http://62selby.solarvu.net/green/solarvu/inverterLog.php?ac=101389&showtime=4770","http://equestrian931.solarvu.net/green/solarvu/inverterLog.php?ac=101428&showtime=5191","http://equestrian931.solarvu.net/green/solarvu/inverterLog.php?ac=101428&showtime=5192",
                "http://equestrian931.solarvu.net/green/solarvu/inverterLog.php?ac=101428&showtime=5193","http://equestrian931.solarvu.net/green/solarvu/inverterLog.php?ac=101428&showtime=5194",
                "http://equestrian931.solarvu.net/green/solarvu/inverterLog.php?ac=101428&showtime=5195","http://equestrian931.solarvu.net/green/solarvu/inverterLog.php?ac=101428&showtime=5196",
                "http://equestrian931.solarvu.net/green/solarvu/inverterLog.php?ac=101428&showtime=5197","http://equestrian931.solarvu.net/green/solarvu/inverterLog.php?ac=101428&showtime=5198",
                "http://equestrian931.solarvu.net/green/solarvu/inverterLog.php?ac=101428&showtime=5199","http://equestrian931.solarvu.net/green/solarvu/inverterLog.php?ac=101428&showtime=5200"]

#prj=['passmore328','craig39','corporate1205','stanfield2562','empey53','telson150','conlins541','vankirk120','berta160','equestrian931','62selby','emblem50','7090tranmere','westbeaver','Trowers164','Fima137','651Hardwood','Mccleary50','Passmore420','Rowntree640','Bowes211','Centennial10','Patteson246','Bowes311','Bakersfield49','DonHilock66','Fairgrounds2315','Frederick135','Industrial245','Middlefield61','Napier6','Norelco180','Parkside550b','Parkside550d','Parkside560','Pool2025','Scott41','Todd88','Weston3637','Weston3655a','Weston3655b']

#Define empty lists to hold values
prevobj=None
showtime=[]
prj = []
ac = []
passmorev=[]
passmorea=[]
inverters=["Fronius","Sungrow","Huawei","Xantrex"]
# Preparing the monitoring of the loop
start_time = time()
requests = 0
#A global list is created to premanantly hold the values scraped from the power now field in the table and then will be compared against each other in the deviation calculation
pwrcomparison = []
# For every url in mainls extract the project name and its showtime value. Then navigate to that page and scrap the required information
for x in mainls:
    #splits the url on the 7th charcter till the period to grab just the project name
    pname= x[7:].split('.')[0]
    prj.append(pname)
    #Grab the last 4 values of the url which is the the unique id for each inverter
    showid= x[-4:]
    showtime.append(showid)
    #acid=x[-20:-14]
    #ac.append(acid)
    #Create an empty list called data that will hold the scraped data
    data = []
    currentpower = []
    #Assign the value of x as the get request
    response= get(x)
    # # Pause the loop
    sleep(randint(1,3))

    # # Monitor the requests
    requests += 1
    elapsed_time = time() - start_time
    print('Request:{}; Frequency: {} requests/s'.format(requests, requests/elapsed_time))
    clear_output(wait = True)

    # # Throw a warning for non-200 status codes
    if response.status_code != 200:
        warn('Request: {}; Status code: {}'.format(requests, response.status_code))
    # # Break the loop if the number of requests is greater than expected
    ## The request value may have to be changed to reflect the amount of times you want to request a page
    if requests > 100:
        warn('Number of requests was greater than expected.')
        break
    # Parse the content of the request with BeautifulSoup
    page_html = BeautifulSoup(response.text, 'html.parser')
    #this is a designated check to see whether the site that has been passed in is equal to weston365b. If it is call the funcition that holds the special container for it to parse and scrap the information off it.
    if pname=="weston3655b":
        #create the necessary containers for current power, the main data on the page, inverter name and then appended the values to their designated lists
        #container for the current power values
        weston_power = []
        pwcontain = page_html.find_all('font', class_='blueXLarge')
        cnt=0
        for p in pwcontain:
            pwr = p.text
            pwr = pwr.strip().replace(",", "")
            if cnt % 2:
                weston_power.append(float(pwr))
                #print("Value added to list")
            else:
                print("This is the lifetime energy value " + pwr)
            cnt+=1
            #print("This is the count value " + str(cnt))
        print(weston_power)
        weston_data=[]
        #container for the inverter name
        invertmanu = page_html.find_all('td', class_='darklight')
        inverter_manu = []
        for i in invertmanu:
            inv=i.b.text
            inverter_manu.append(inv)
        weston_values = page_html.find_all('font', class_='blueFont')
        #container for the main data values on the page
        for v in weston_values:
            current_values=v.b.text
            weston_data.append(current_values)

        print(inverter_manu)
        #Calls the Weston function with the new created lists being passed in as parameters to scrap the specific volatage and amparage values for each inverter
        Weston(weston_data,inverter_manu,weston_power)


    else:
        invertmanu = page_html.find('td', class_='darklight').b.text
        print(invertmanu)
        # Select all the font tags that contain the class historyFont in them  from a single page
        mv_containers = page_html.find_all('font',class_ ='historyFont')
        # Create a new container to select all the font tags that contain the class historyXLarge in them  from a single page
        containerb = page_html.find_all('font',class_ ='historyXLarge')
        for contain in containerb:
            cp=contain.text
            currentpower.append(cp)

        #print(pwrcomparison)
        # strip the the tabs and new line tags from containerb in order to have just the value
        # for pw in currentpower[0]:
        #     y = pw.strip()
        #     print("This the value of: "+y)
        # #append the value from y and store in a list called current power
        #     if "," in y:
        #         t=y.replace(",","")
        #         print (t)
        #         pwrcomparison.append(float(t))
        #     else:
        #         pwrcomparison.append(float(y))
        #print (pwrcomparison)
        # For the current container grab the value between the bold tag convert to a text and appended it to a list called data
        for container in mv_containers:
            #print (container)
            #Scrape the bold tag to retrieve the values in the table
            current = container.b.text
            #print (current)
            data.append(current)
    #Grab the values for amparage and voltage from the data list and assign them to a variable
        if inverters[0] in invertmanu:
            cpwr=currentpower[0].strip().replace(",","")
            if float(cpwr) > 10000:
                pwrcomparison.append(cpwr)
            else:
                wats_kw = float(cpwr)/1000
                pwrcomparison.append(wats_kw)
            Fronius(pname,showid,data,passmorea,passmorev)
        elif inverters[1] in invertmanu:
            # strip the the tabs and new line tags from containerb in order to have just the value
            for pw in currentpower[1:]:
                y = pw.strip()
                # append the value from y and store in a list called pwrcomparison
                if "," in y:
                    t = y.replace(",", "")
                    print (t)
                    if float(t)>10000:
                        pwrcomparison.append(t)
                    else:
                        wats_kw = float(t) / 1000
                        pwrcomparison.append(wats_kw)
                else:
                    pwrcomparison.append(float(y))
            # print (pwrcomparison)
            Sungrow(pname,showid,data,passmorea,passmorev)

        elif inverters[2] in invertmanu:
            cpwr = currentpower[0].strip().replace(",","")
            if float(cpwr) > 10000:
                pwrcomparison.append(cpwr)
            else:
                wats_kw=float(cpwr) / 1000
                pwrcomparison.append(wats_kw)
            Huawei(pname, showid, data, passmorea, passmorev)
        elif inverters[3] in invertmanu:
            cpwr = currentpower[0].strip().replace(",","")
            if float(cpwr) > 10000:
                pwrcomparison.append(cpwr)
            else:
                wats_kw = float(cpwr) / 1000
                pwrcomparison.append(wats_kw)
            Xantrex(pname, showid, data, passmorea, passmorev)
        else:
            cpwr = currentpower[0].strip().replace(",","")
            if float(cpwr) > 10000:
                pwrcomparison.append(cpwr)
            else:
                wats_kw = float(cpwr)/1000
                pwrcomparison.append(wats_kw)
            print (pname+" Inverter: "+showid)
            ca=data[12]
            passmorea.append(ca)
            print (ca)
            cb=data[13]
            passmorea.append(cb)
            print (cb)
            cc=data[14]
            passmorea.append(cc)
            print (cc)
            va=data[9]
            passmorev.append(va)
            print (va)
            vb=data[10]
            passmorev.append(vb)
            print (vb)
            vc=data[11]
            passmorev.append(vc)
            print(vc)
            print (currentpower)
    # for the voltage values in passmore multiple each value by 5%
    # You would have to run a loop for each list that has been created. One for the voltage, amparage and current power. Then for each value in that list find its 5% deviation and compare it to the orginale value to see if there have been any significant changes.

        # if the projectname changes clear the current lists and start appending the new projects values to the definded lists
        if prevobj is not None and pname==prevobj:
            #cnt == 0
            deviationcalc(passmorev,passmorea,pwrcomparison,invertmanu,pname,x)
            passmorev.clear()
            passmorea.clear()
            currentpower.clear()
        elif prevobj is None:
            deviationcalc(passmorev, passmorea, pwrcomparison, invertmanu, pname, x)
            passmorev.clear()
            passmorea.clear()
            currentpower.clear()
            prevobj = pname
        elif prevobj != pname:
            pwrcomparison.clear()
            cpwr = currentpower[0].strip().replace(",", "")
            if float(cpwr) > 10000:
                pwrcomparison.append(cpwr)
            else:
                wats_kw = float(cpwr)/1000
                pwrcomparison.append(wats_kw)
            deviationcalc(passmorev, passmorea, pwrcomparison, invertmanu, pname, x)
            passmorev.clear()
            passmorea.clear()
            currentpower.clear()
            prevobj = pname
        else:
            pwrcomparison.clear()
