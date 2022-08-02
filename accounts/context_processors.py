from datetime import datetime

def our_time(request):
    now = datetime.now()
    current_time = now.strftime('%H:%M:%S')
    return {"our_current_time": current_time}