import cv2

#strlist = ['@','Q','*','o',':','`',' ']
strlist = [' ','`',':','o','*','Q','@']
#strlist = ['⬜','◻️','◼','◽','▪️',' ']
cap = cv2.VideoCapture('.\\rickroll.mp4')#input
grand = open('drawing.html','w',encoding='utf-8')#output
lheight = 3
#grand.write('#include <stdio.h>\n#include <stdlib.h>\n#include<windows.h>\nint main()\n{\n')
grand.write('<!DOCTYPE html>\n<html lang="en" style="width: 100%;height: 100%;font-style: sans-serif;">\n<head>  \n    <meta charset="UTF-8">  \n    <title>Video Play</title>\n</head>\n<body style="width: 100%;height: 100%;font-family: \'Open Sans\',sans-serif;overflow-y:hidden;overflow-x:hidden;background-color: #000000;">\n <table id="out" style="color: #fff;text-shadow:0 0 1px;letter-spacing: 1px;font-size:1px;text-align:left;white-space:pre; line-height:'+str(lheight)+'px;"></table>\n<script type="text/javascript">\n')
time = 0
while True:
    #os.system('cls')
    damn,img = cap.read()
    if not damn:break
    frame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #shit,show=cv2.threshold(frame,150,255,cv2.THRESH_BINARY)
        #way,fuck = cv2.findContours(show,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    #show = cv2.drawContours(show,way,-1,255,2,cv2.LINE_AA)
    show = cv2.resize(frame,(93,50),interpolation=cv2.INTER_AREA)
    #185,85
    cv2.waitKey(1)
    x,y = show.shape
    #print(x,y)
    all_word = ''
    for a in range(x):
        words = ''
        for b in range(y):
            words = words + strlist[round(show[a,b]//round(255//len(strlist)+1))]
        all_word = all_word + '<tr><th><code>' + words + '</code></th></tr>'

    #grand.write('system("cls");\nprintf("'+all_word+'");\nSleep(33);\n')
    grand.write("setTimeout(function () {document.getElementById('out').innerHTML='"+all_word+"'}, "+str(time)+");\n")
    time += 41

grand.write('</script>\n</body>\n</html>\n')
grand.close()