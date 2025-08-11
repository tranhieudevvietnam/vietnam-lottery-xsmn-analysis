# __author__ = 'Khiem Doan'
# __github__ = 'https://github.com/khiemdoan'
# __email__ = 'doankhiem.crazy@gmail.com'

# from datetime import datetime, time, timedelta
# from zoneinfo import ZoneInfo
# from lottery import Lottery



# if __name__ == '__main__':
#     lottery = Lottery()
#     lottery.load()

#     # Download new data

#     begin_date = lottery.get_last_date()
#     tz = ZoneInfo('Asia/Ho_Chi_Minh')
#     now = datetime.now(tz)
#     last_date = now.date()
#     if now.time() < time(18, 35):
#         last_date -= timedelta(days=1)

#     delta = (last_date - begin_date).days + 1
#     for i in range(1, delta):
#         selected_date = begin_date + timedelta(days=i)
#         print(f'Fetching: {selected_date}')
#         lottery.fetch(selected_date)

#     lottery.generate_dataframes()
#     lottery.dump()


import os
from datetime import datetime, time, timedelta
from zoneinfo import ZoneInfo
from lottery import Lottery

if __name__ == '__main__':
    lottery = Lottery()
    lottery.load()

    # ✅ Lấy ngày từ biến môi trường FETCH_DATE nếu có
    fetch_date_str = os.getenv("FETCH_DATE")
    tz = ZoneInfo('Asia/Ho_Chi_Minh')

    if fetch_date_str:
        # Nếu truyền ngày, parse thành datetime.date
        last_date = datetime.strptime(fetch_date_str, "%Y-%m-%d").date()
        begin_date = last_date - timedelta(days=1)  # để vòng for chạy đúng ngày
    else:
        # Logic cũ
        begin_date = lottery.get_last_date()
        now = datetime.now(tz)
        last_date = now.date()
        if now.time() < time(18, 35):
            last_date -= timedelta(days=1)

    delta = (last_date - begin_date).days + 1
    for i in range(1, delta):
        selected_date = begin_date + timedelta(days=i)
        print(f'Fetching: {selected_date}')
        lottery.fetch(selected_date)

    lottery.generate_dataframes()
    lottery.dump()
