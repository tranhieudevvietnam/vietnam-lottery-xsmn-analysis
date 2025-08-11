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


from datetime import datetime, time, timedelta
from zoneinfo import ZoneInfo
import os
import sys
from lottery import Lottery


if __name__ == '__main__':
    lottery = Lottery()
    lottery.load()

    # ✅ Lấy ngày cần fetch từ biến môi trường hoặc tham số CLI
    target_date_str = os.getenv("FETCH_DATE") or (sys.argv[1] if len(sys.argv) > 1 else None)

    tz = ZoneInfo('Asia/Ho_Chi_Minh')
    now = datetime.now(tz)

    if target_date_str:
        # Nếu truyền ngày, parse về kiểu date
        last_date = datetime.strptime(target_date_str, "%Y-%m-%d").date()
        begin_date = last_date - timedelta(days=1)  # Lùi 1 ngày để vòng lặp fetch đúng ngày
    else:
        # Logic cũ
        begin_date = lottery.get_last_date()
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
