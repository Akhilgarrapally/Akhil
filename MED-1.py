from csv import reader
from csv import writer
import requests
from bs4 import BeautifulSoup
import re


with open('C:\Akhil\ylink.csv','r') as read_obj :
    csv_reader=reader(read_obj)


    for row in csv_reader :



            try:
                final_list = []

                url = row[0]
                res = requests.get(url).content
                soup = BeautifulSoup(res, "html.parser")
                try:

                    name = soup.find('h1', attrs={'class': 'ooufh'})
                    medicinename=(name.text)
                    final_list.append(medicinename)

                except Exception as e :
                    print(e)
                    final_list.append("none")

                try:

                    manu = soup.find('div', attrs={'class': '_3JVGI'})
                    manufatcure=(manu.text[3:])
                    final_list.append(manufatcure)


                except Exception as e:
                    print(e)
                    final_list.append("None")


                try:

                    size = soup.find('div', attrs={'class': '_36aef'})
                    size1=(size.text)
                    final_list.append(size1)

                except Exception as e:
                    print(e)
                    final_list.append("None")

                try:

                    price = soup.find('span', attrs={'class': '_31Agc'})
                    price1=(price.text[1:])
                    final_list.append(price1)

                except Exception as e:
                    print(e)
                    final_list.append("None")



                try:

                    therapy = soup.find('td', attrs={'class': '_3C_XR'})
                    therapy1=(therapy.text)
                    final_list.append(therapy1)

                except Exception as e:
                    print(e)
                    final_list.append("None")


                #print(final_list)

                with open ('C:/Akhil/Yletter.csv','a', encoding="utf-8", newline='') as f_obj:
                    writer_obj = writer(f_obj)
                    writer_obj.writerow(final_list)
                    f_obj.close()

            except Exception as e:
                print(e)
