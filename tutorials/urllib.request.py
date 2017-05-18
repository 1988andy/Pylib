import os
import re
import urllib.request
from datetime import *

pattern = re.compile(r'<LI><A\shref=".*?"\starget=_blank>(?P<no>\d{11})</A>\s</LI>')
for i in range(1,14916):
    url = "http://dingwei.hiphop8.com/more.php?page=" + str(i)
    with open(os.getcwd() + "/xiaochao.csv", "a") as f:
        f.write(",".join(("Phone Number", "Province", "City", "Area Code", "Operator")))
        f.write("\n")
        try:
            print(datetime.today().strftime("%Y-%m-%d %H:%M:%S %p"), "Request", url)
            with urllib.request.urlopen(url) as request:
                content = request.read().decode("gbk")
                #print(content)
                for m in pattern.finditer(content):
                    #print(m.group("no"))
                    no = m.group("no")
                    prov = ""
                    city = ""
                    areacode = ""
                    operator = ""
                    url = "http://dingwei.hiphop8.com/nub/" + no + ".html"
                    try:
                        print(datetime.today().strftime("%Y-%m-%d %H:%M:%S %p"), "Request", url)
                        with urllib.request.urlopen(url) as rdetail:
                            cdetail = rdetail.read().decode("gbk")
                            mdetail = re.search("卡号归属地：</SPAN><SPAN class=T>(?P<prov>[^\s]+?)\s(?P<city>.*?)</SPAN></DIV>", cdetail)
                            if mdetail:
                                prov = mdetail.group("prov")
                                city = mdetail.group("city")
                            mdetail = re.search("归属地区号：</SPAN><SPAN class=T>(?P<val>\d+?)</SPAN></DIV>", cdetail)
                            if mdetail:
                                areacode = mdetail.group("val")
                            mdetail = re.search("卡号类型：</SPAN><SPAN\s*class=T>(?P<operator>.*?)</SPAN></DIV></DIV>", cdetail)
                            if mdetail:
                                operator = mdetail.group("operator")
                    except:
                        print("!Err", url)
                    f.write(",".join((no, prov, city, areacode, operator)))
                    f.write("\n")
                    f.flush()
                    print("  >>>", no, prov, city, areacode, operator)
                break
        except:
            print("!Err", url)
        f.close()
        break

