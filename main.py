"""Willpower corretctor.

I hope that no one else need this.
"""

import os
import subprocess
import signal
from dotenv import load_dotenv
import datetime
import time
import sys

load_dotenv()
param = ""

if len(sys.argv) > 1:
  param = sys.argv[1]

# Getting values from ENV file
apps = tuple(map(str, os.getenv('APPS').split(',')))
apps_work_time = tuple(map(int, os.getenv('APP_WT').split(',')))
tts = os.getenv('USE_TTS')
tts_str = os.getenv('TTS_STRING')

load_dotenv(override=True)

# main cycle
while True:
    gulty = False
    now = datetime.datetime.now()
    for indx, app in enumerate(apps):
        if (now.hour < int(apps_work_time[indx*2]) or
                now.hour >= int(apps_work_time[2*indx+1])):
            p = subprocess.Popen(['ps', '-A'], stdout=subprocess.PIPE)
            out, err = p.communicate()
            ou = out.decode("utf-8")
            for line in ou.splitlines():
                if app in line:
                    pid = int(line.split(None, 1)[0])
                    os.kill(pid, signal.SIGKILL)
                    print("i killed "+app+" "+str(pid))
                    gulty = True
    if tts and gulty:
        os.system('echo %s | festival --tts --language russian' % tts_str)
    time.sleep(1)
