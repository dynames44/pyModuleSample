import sys
import os

# 패키지(디렉토리) 이름으로 모듈(***.py 파일)을 임포트 할수 있는 전역 설정
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__)))
sys.path.append(BASE_DIR)