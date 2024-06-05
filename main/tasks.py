from config.celery import app

# @app.task(bind=True, ignore_result=True)
# def debug_task(self):
    # print(f'CELERY IS WORKING...')


@app.task()
def slow_func(a):
    for i in range(a):
        print(i, " ---> ", i * 2)
