import time

#프로그램 root 에서는 하위에 있는 모듈 (***.py파일)을 마음대로 가져다 쓸 수 있다.
from apps import appInit as init, appRun as hRun 

#어플리 케이션 초기화 
init.appInit();

time.sleep(3)

#어플리케이션 실행
hRun.appRun();
