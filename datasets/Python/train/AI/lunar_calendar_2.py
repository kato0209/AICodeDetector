import datetime
import calendar

def gregorian_to_islamic(year, month, day):
    """グレゴリオ暦からイスラム暦への変換（近似）"""
    # この変換は非常に近似的で、正確なイスラム暦の計算には適していません。
    jd = sum(calendar.monthrange(year, m)[1] for m in range(1, month)) + day
    islamic_year = int((jd - 227015) / 354.367)
    islamic_month = 1  # この実装では、月の計算は行われません。
    islamic_day = 1    # この実装では、日の計算は行われません。
    return islamic_year, islamic_month, islamic_day


greg_to_islamic = gregorian_to_islamic(2023, 4, 1)