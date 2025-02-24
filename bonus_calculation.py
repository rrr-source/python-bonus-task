from datetime import datetime, timedelta

# Пример данных пользователей (даты сразу преобразуем)
users = {
    1: {"inviter": None, "package": 1500, "purchase_date": datetime(2024, 2, 1)},
    2: {"inviter": 1, "package": 1500, "purchase_date": datetime(2024, 2, 5)},
    3: {"inviter": 1, "package": 1500, "purchase_date": datetime(2024, 2, 10)},
    4: {"inviter": 2, "package": 1500, "purchase_date": datetime(2024, 2, 15)},
    5: {"inviter": 2, "package": 1500, "purchase_date": datetime(2024, 2, 20)},
    6: {"inviter": 3, "package": 1500, "purchase_date": datetime(2024, 2, 25)},
    7: {"inviter": 3, "package": 1500, "purchase_date": datetime(2024, 2, 13)},
}

# Функция проверки выполнения условий бонуса
def calculate_bonus(users):
    bonus_recipients = {}

    for inviter_id, inviter_data in users.items():
        if inviter_data["package"] < 1500:
            continue

        start_date, end_date = inviter_data["purchase_date"], inviter_data["purchase_date"] + timedelta(days=30)

        referrals = {
            uid for uid, udata in users.items()
            if udata["inviter"] == inviter_id and start_date <= udata["purchase_date"] <= end_date and udata["package"] >= 1500
        }

        if len(referrals) >= 2:
            bonus_recipients[inviter_id] = list(referrals)

    return bonus_recipients

# Вывод результатов
for user, referrals in calculate_bonus(users).items():
    print(f"{user}: {referrals}")
