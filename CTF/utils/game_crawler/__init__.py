from .game import *
# 引入所有的类和函数

import sched
import time

# 用于启动定时任务

scheduler = sched.scheduler(time.time, time.sleep)
scheduler.enter(3600, 1, get_inf, ())
scheduler.run()
