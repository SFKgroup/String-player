import cv2


cap = cv2.VideoCapture('.\\schoolday.mp4')
grand = open('drawing.cpp','w',encoding='utf-8')
#grand.write('#include <stdio.h>\n#include <stdlib.h>\n#include<windows.h>\nint main()\n{\n')
grand.write('#include <stdio.h>\n#include<windows.h>\nvoid gotoxy(int posX, int posY)\n{\nCOORD pos;\npos.X = posX;\npos.Y = posY;\nHANDLE hOut = GetStdHandle(STD_OUTPUT_HANDLE);\nSetConsoleCursorPosition(hOut, pos);\n}\nint main()\n{\nchar a[200];\nprintf("Plaese watch it with full screen.\\nEnter any character to continue.");\nscanf("%d",a);\n')

while True:
    #os.system('cls')
    damn,img = cap.read()
    if not damn:break
    frame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    shit,show=cv2.threshold(frame,150,255,cv2.THRESH_BINARY)
        #way,fuck = cv2.findContours(show,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    #show = cv2.drawContours(show,way,-1,255,2,cv2.LINE_AA)
    show = cv2.resize(show,(133,37),interpolation=cv2.INTER_AREA)
    #cv2.imshow('test',show)
    #print(way)
    cv2.waitKey(1)
    x,y = show.shape
    #print(x,y)
    all_word = ''
    for a in range(x):
        words = ''
        for b in range(y):
            if show[a,b] == 0:
                #print("\033[40m \033[0m", end="")
                words = words + "@"
            else:
                #print("\033[47m \033[0m")
                words = words + "."
        all_word = all_word + words + '\\n'

    #grand.write('system("cls");\nprintf("'+all_word+'");\nSleep(33);\n')
    grand.write('gotoxy(0, 0);\nprintf("'+all_word+'");\nSleep(21);\n')

grand.write('scanf("%d",a);\nreturn 0;\n}')
grand.close()