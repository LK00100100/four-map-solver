from datetime import datetime


class Stopwatch:
    def __enter__(self):
        print("Start:", datetime.now())
        return None

    def __exit__(self, type, value, traceback):
        print("End  :", datetime.now())
        return None
