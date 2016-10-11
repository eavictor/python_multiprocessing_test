from multiprocessing import Pool
import time


result_list = []


def my_print(n):
    time.sleep(1)
    print(n)
    return n


def result(n):
    global result_list
    result_list.append(n)


if __name__ == '__main__':
    pool = Pool(10)
    # remove for loop in worker, it's only for testing the multiprocessing pool
    for i in range(1000):
        # if multiprocessing pool has space, the function will run immediately, otherwise will block and wait for space
        # can use callback function send result back to response MQ
        pool.apply_async(func=my_print, args=(i, ), callback=result)
    # I don't need this in MQ-RPC worker and will automatically be called when the connection is garbage collected.
    pool.close()
    # I don't need this in MQ-RPC worker
    pool.join()
    print(result_list)
