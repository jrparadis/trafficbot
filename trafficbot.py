from PIL import Image
import autopy
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

'''
900,215 = i5 bridge
898,252 interstate / meadows
904,293 i5 near 30b
904,328 rosa parks
905,358 i5n at top of 405
|51 i5 south at i5/405 split
914,381 i5 below 405 north split
927,402 i5 n of 84
927,447 i5n to 84e

|52 4055 south at i5/405 split
900,390 405n to i5
890,414 405 n @ 26
895,470 405 n at bottom split

512|
913,507 s of 405 split
905,546 i5 at south waterfront
871,584 i5 at barber
797,637 99w at i5
786,683 above 217

i5 route ^

783,752 outside work n
770,781 outside work s - tulatlin

205 route v

777,830 205n at i5
842,829 stafford
916,852 before west lynn
966,888 west lynn hill
1025,855 abernathy
1089,781 n of gladstone
1097.5,715.5 clackamas
1106,649 sunnyside
1103,589 johnson creek /miles fiberglass
1111,551 lents
1112,469 divisionish
1112,471 205 n of 26/powell
1112,356 205 near killingsworth
1124,327 205 n of 30b
1146,298 airport way
1139,240 205 bridge

84|
941,425 84e @ i5
990,408 84e at sandy
1120,396 hell ramp 205 and 84

'''
i5bridgeroute = [(900,215),(898,252),(904,293),(904,328),(905,358),(914,381),(927,402),(927,447),(913,507),(905,546),(871,584),(797,637),(786,683),(783,752)]
i405route = [(900,215),(898,252),(904,293),(904,328),(905,358),(900,390),(890,414),(895,470),(913,507),(905,546),(871,584),(797,637),(786,683),(783,752)]
i205fullroute = [(770,781),(777,830),(842,829),(916,852),(966,888),(1025,855),(1089,781),(1097.5,715.5),(1106,649),(1103,589),(1111,551),(1112,469),(1112,471),(1112,356),(1124,327),(1146,298),(1139,240),(941,425),(990,408), (1120,396)]
i84to205route = [(1139,240),(1146,298),(1124,327),(1112,356),(1120,396),(990,408),(941,425),(927,447),(913,507),(905,546),(871,584),(797,637),(786,683),(783,752)]

newpoints = [i5bridgeroute,i405route,i205fullroute,i84to205route]
pointsonmap = [(900,215),(898,252), (904,293),(904,328),(905,358),(915,382),(927,402),(927,447),(900,390),(890,414),(895,470),(913,507),(905,546),(871,584),(797,637),(786,683),(783,752),
               (770,781),(777,830),(842,829),(916,852),(966,888),(1025,855),(1089,781),(1097.5,715.5),(1106,649),(1103,589),(1111,551),(1112,469),(1112,471),(1112,356),(1124,327),(1146,298),
               (1139,240),(941,425),(990,408), (1120,396)]
colors = {'green' : (132,202,80),'yellow' : (240, 125, 2),'red' : (230,0,0),'dark red' : (158,19,19)}
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--disable-infobars")
driver = webdriver.Chrome(chrome_options=options)

driver.get("https://www.google.com/maps/@45.4752613,-122.6474499,11z/data=!5m1!1e1")

time.sleep(5)

bitmap = autopy.bitmap.capture_screen()
bitmap.save('c:\\scripts\\traffic.png')
driver.quit()
im = Image.open('c:\\scripts\\traffic.png')
rgb_im = im.convert('RGB')
for route in newpoints:
    b = 0
    for points in route:
        trafficcolor = rgb_im.getpixel(points)
        if trafficcolor == colors['yellow']:
            b += 1
        elif trafficcolor == colors['red']:
            b += 2
        elif trafficcolor == colors['dark red']:
            b += 3
        elif trafficcolor == colors['green']:
            pass
        else:
            print 'something broke, probably broken coords'
            print points
            print trafficcolor
    if route == i5bridgeroute:
        print 'I5 bridge traffic score: ' + str(b)
    elif route == i405route:
        print 'i5 w/ 405 detour traffic score: ' + str(b)
    elif route == i205fullroute:
        print 'I205 full route traffic score: ' + str(b)
    elif route == i84to205route:
        print 'I5 -> 84 -> 205 traffic score: ' + str(b)
    else:
        print 'fail' 

