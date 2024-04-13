import os 
import sys

sys.path.append("./config")
import time
import schedule 
import funcoes

schedule.every(10).minutes.do(funcoes.run)

while True:
    schedule.run_pending()
    time.sleep(55)
    