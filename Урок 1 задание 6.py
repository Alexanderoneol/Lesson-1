while True:
    days = 1
    first_day_km = float(inpet("езультат первого дня тренировок: "))
    end_day_km = float(input("Результат достигнутый по окончании тренировок: "))
    if first_day_km <= 0 or end_day_km < 0:
        print("Вы должны пробежать некоторое расстояние, Расстояние != 0.")
    else:
        while first_day_km < end_day_km:
            first_day_km += first_day_km * 0.1
            days += 1

        print(f"ы достигнете желаемого результата за {days} дней")
        break