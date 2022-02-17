import threading
import time
import inspect
import ctypes


def _async_raise(tid, exctype):
    """raises the exception, performs cleanup if needed"""
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")


def stop_thread(thread):
    _async_raise(thread.ident, SystemExit)


# class TestThread(threading.Thread):
#
#     def run(self):
#         print("begin")
#         while True:
#             time.sleep(0.1)
#         print("end")


def test():
    print('sleep ing')
    # time.sleep(5)
    while True:
        pass
    print('finished sleep')


if __name__ == "__main__":
    for i in range(3):
        a = threading.Thread(target=test)
        a.start()
        print(threading.enumerate())
        stop_thread(a)
        time.sleep(1)
        print(threading.enumerate())
    print(threading.enumerate())