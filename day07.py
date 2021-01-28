"""
進程
"""

"""

# 未使用 多進程代碼
from random import randint
from time import time, sleep

def download_task(filename):
    print('start download %s' % filename)
    time_to_download = randint(5,10)
    sleep(time_to_download)
    print('%s download finish ! cost %d second' % (filename,time_to_download))

def main():
    start = time()
    download_task('Python Book.pdf')
    download_task('Java Book.pdf')
    end = time()
    print('all time cost %.2f second .' % (end-start))

if __name__ == '__main__':
    main()

"""

# 使用 多進程代碼
from multiprocessing import Process
from os import getpid
from random import randint
from time import time, sleep

def download_task(filename):
    print('start download process , pid = [%d].' % getpid())
    print('start download %s ...' % filename)
    time_to_download = randint(5,10)
    sleep(time_to_download)
    print('%s download finish ! cost %d seconds' % (filename , time_to_download))

def main():
    start = time()
    # target = 函數名 ，代表進程啟動後，要運行的代碼
    # args = 元組 ，代表函數執行時，傳入的參數
    p1 = Process(target=download_task, args=('Python Book.pdf', ))

    # Process對象的 start 方法用來啟動進程
    p1.start()
    p2 = Process(target=download_task, args=('Java Book.pdf', ))
    p2.start()
    # join 方法 代表 等待進程結束，如果沒有使用這個，在這個情境中，是會直接運行完main方法，導致其他進程還沒結束程式就結束了。
    p1.join()
    p2.join()
    end = time()
    print('all time cost %.2f seconds .' % (end - start))

if __name__ == '__main__':
    main()