'''

finder is a interface for finding the Latitude and Logitude coordinates given the address information.

Using Google and Here Geocoding API. 

03/22/2018
Xudong Liu

'''
import sys
import requests
from PyQt4 import QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import argparse

parser =argparse.ArgumentParser()

parser.add_argument('--google_api_key', type=str, help='https://developers.google.com/console')
parser.add_argument('--here_app_id', type=str, help='https://developer.here.com/documentation/geocoder/topics/quick-start.html')
parser.add_argument('--here_app_code', type=str, help='https://developer.here.com/documentation/geocoder/topics/quick-start.html')

args = parser.parse_args()

class Lat_Lng_finder(QtGui.QWidget):

    def __init__(self):
        super(Lat_Lng_finder, self).__init__()

        self.initUI()

    def initUI(self):

        self.add = QtGui.QLabel('Address:')
        self.city= QtGui.QLabel('City:')
        self.state = QtGui.QLabel('State:')

        self.lat = QtGui.QLabel('Lat:')
        # self.lat.setVisible(False)
        self.lng = QtGui.QLabel('Lng:')
        # self.lat.setVisible(False)
        self.addEdit = QtGui.QLineEdit()
        self.cityEdit = QtGui.QLineEdit()
        # self.stateEdit = QtGui.QLineEdit()

        self.stateCombo = QtGui.QComboBox(self)
        self.stateCombo.addItem("")
        self.stateCombo.addItem("AL")
        self.stateCombo.addItem("AK")
        self.stateCombo.addItem("AK")
        self.stateCombo.addItem("AR")
        self.stateCombo.addItem("CA")
        self.stateCombo.addItem("CO")
        self.stateCombo.addItem("CT")
        self.stateCombo.addItem("DE")
        self.stateCombo.addItem("FL")
        self.stateCombo.addItem("GA")
        self.stateCombo.addItem("HI")
        self.stateCombo.addItem("ID")
        self.stateCombo.addItem("IL")
        self.stateCombo.addItem("IN")
        self.stateCombo.addItem("IA")
        self.stateCombo.addItem("KS")
        self.stateCombo.addItem("KY")
        self.stateCombo.addItem("LA")
        self.stateCombo.addItem("ME")
        self.stateCombo.addItem("MD")
        self.stateCombo.addItem("MA")
        self.stateCombo.addItem("MI")
        self.stateCombo.addItem("MN")
        self.stateCombo.addItem("MS")
        self.stateCombo.addItem("MO")
        self.stateCombo.addItem("MT")
        self.stateCombo.addItem("NE")
        self.stateCombo.addItem("NV")
        self.stateCombo.addItem("NH")
        self.stateCombo.addItem("NJ")
        self.stateCombo.addItem("NM")
        self.stateCombo.addItem("KY")
        self.stateCombo.addItem("NY")
        self.stateCombo.addItem("NC")
        self.stateCombo.addItem("ND")
        self.stateCombo.addItem("OH")
        self.stateCombo.addItem("OK")
        self.stateCombo.addItem("OR")
        self.stateCombo.addItem("PA")
        self.stateCombo.addItem("RI")

        self.stateCombo.addItem("SC")
        self.stateCombo.addItem("SD")
        self.stateCombo.addItem("TN")
        self.stateCombo.addItem("TX")
        self.stateCombo.addItem("UT")
        self.stateCombo.addItem("VT")
        self.stateCombo.addItem("VA")
        self.stateCombo.addItem("WA")
        self.stateCombo.addItem("WV")
        self.stateCombo.addItem("WI")
        self.stateCombo.addItem("WY")
        self.stateCombo.addItem("DC")



        # self.latEdit = QtGui.QLineEdit()
        # self.lngEdit = QtGui.QLineEdit()
        # self.lat.setVisible(False)
        # self.lngEdit.setVisible(False)

        self.cancelButton = QtGui.QPushButton("clear",self)

        self.okButton = QtGui.QPushButton("Get Coordinates",self)


        self.grid = QtGui.QGridLayout()
        self.grid.setSpacing(10)

        self.grid.addWidget(self.add, 1, 0)
        self.grid.addWidget(self.addEdit, 1, 1)

        self.grid.addWidget(self.city, 2, 0)
        self.grid.addWidget(self.cityEdit, 2, 1)

        self.grid.addWidget(self.state, 3, 0)
        self.grid.addWidget(self.stateCombo, 3, 1)

        self.grid.addWidget(self.cancelButton, 4, 0)

        self.okButton.setShortcut('Return')
        self.grid.addWidget(self.okButton, 4, 1)

        self.cancelButton.setShortcut('Delete')
        # self.grid.addWidget(self.lat,4,1)
        # self.grid.addWidget(self.latEdit, 4, 2)
        # self.grid.addWidget(self.lng, 5, 1)
        # self.grid.addWidget(self.lngEdit, 5, 2)

        self.setLayout(self.grid)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('interface')
        self.show()

        self.okButton.clicked.connect(self.okbuttonClicked)
        self.cancelButton.clicked.connect(self.cancelbuttonClicked)


    def okbuttonClicked(self):

        lat,lng,details= self.locating()
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("lat and lng")
        if lat and lng:

            msg.setText("Latitude:"+str(lat))
            msg.setInformativeText("Longitude:"+str(lng))
            # msg.setWindowTitle("lat and lng")
            msg.setDetailedText("The location details:\n"+ str(details))

        else:
            msg.setText("NA, Please make sure the address is correct!")

        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.exec_()
        # print "value of pressed message box button:", retval

        # out = self.addEdit.text()
        # print out

    # def msgbtn(self,i):
    #     print "Button pressed is:", i.text()


    def cancelbuttonClicked(self):

        self.addEdit.clear()
        self.cityEdit.clear()
        self.stateCombo.setCurrentIndex(0)
        # self.stateEdit.clear()

    def locating(self):

        s1 = str(self.addEdit.text())
        s2 = str(self.cityEdit.text())
        s3 = str(self.stateCombo.currentText())
        # s3 = str(self.stateEdit.text())

        goolge_map = 'https://maps.googleapis.com/maps/api/geocode/json'
        here_map = 'https://geocoder.cit.api.here.com/6.2/geocode.json'
        here_app_id = args.here_app_code
        here_app_code = args.here_app_code
        google_api_key = args.google_api_key



        value = s1.replace(' ', '+') + '+' + s2 + '+' + s3
        goole_payload = {'address': value, 'key': google_api_key}
        s = requests.Session()
        r = s.get(goolge_map, params=goole_payload)

        # t =0
        if r.status_code == requests.codes.ok:
        # if t:
            res = r.json()
            if res[u'results']:
                lat = res[u'results'][0][u'geometry'][u'location'][u'lat']
                lng = res[u'results'][0][u'geometry'][u'location'][u'lng']
                details= res[u'results'][0][u'formatted_address']
            else:
                lat , lng, details = None,None,None

            return lat,lng,details

        else:
            here_payload = {'app_id': here_app_id, 'app_code': here_app_code, 'searchtext': value}

            rr = s.get(here_map, params=here_payload)

            res = rr.json()
            if res[u'Response'][u'View']:
                lat = res[u'Response'][u'View'][0][u'Result'][0][u'Location'][u'DisplayPosition'][u'Latitude']
                lng = res[u'Response'][u'View'][0][u'Result'][0][u'Location'][u'DisplayPosition'][u'Longitude']
                details = res[u'Response'][u'View'][0][u'Result'][0][u'Location'][u'Address'][u'Label']
            else:
                lat,lng,details = None,None,None
            return lat,lng,details
            # res[u'Response'][u'View'][0][u'Result'][0][u'Location'][u'DisplayPosition'][u'Latitude'][u'Longitude']


def main():

    app = QtGui.QApplication(sys.argv)
    finder = Lat_Lng_finder()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
