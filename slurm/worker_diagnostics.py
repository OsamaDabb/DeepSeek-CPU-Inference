# worker_diagnostics.py
import psutil
import time
import datetime
import socket

hostname = socket.gethostname()
log_file = f"worker_diagnostics_{hostname}.log"

while True:
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cpu = psutil.cpu_percent(interval=1)
    mem = psutil.virtual_memory()
    net = psutil.net_io_counters()
    
    with open(log_file, "a") as f:
        f.write(f"[{now}] CPU: {cpu}% | Mem: {mem.percent}% | Net Sent: {net.bytes_sent} B | Net Recv: {net.bytes_recv} B\n")
    
    time.sleep(5)  # adjust frequency here

