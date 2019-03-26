import os
from multiprocessing import cpu_count

bind=["localhost:portnumber"]     #配置nginx时，将此地址写入nginx配置文件
daemon = True #守护进程
workers = cpu_count()*2
forworded_allow_ips = '*'

# gunicorn配置参数
keepalive = 6
timeout = 65
graceful_timeout = 10
worker_connections = 65535
