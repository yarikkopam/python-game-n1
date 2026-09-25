# ================================================
# ИГРА «ЗАБРОШЕННАЯ КУЗНИЦА»
# Автор: Александров Ярослав
# Дата: сентябрь 2026
#
# Пункт 4 - «потрогать наковальню»: герой проверяет,
# тёплая ли она ещё.
# Пункт 5 - «осмотреть полки»: герой ищет полезные вещи.
# Пункт 6 - «тренировка»: герой бьёт старое чучело.
# ================================================

# --- Заголовок ------------------------------------
title = "ЗАБРОШЕННАЯ КУЗНИЦА"
frame = "=" * 22
print(frame)
print(f" {title} ")
print(frame)
print()

# --- Знакомство с героем --------------------------
print("Как зовут героя?")
hero_name = input()
print(f"Добро пожаловать, {hero_name}!")
print("Ты входишь в старую кузницу. Здесь пахнет железом и золой, "
      "а в углу тлеет уголёк.")
print()

# --- Настройка героя -------------------------------
print("Настройка героя.")
print("Здоровье, сила, ловкость, воля — по одному числу в строке:")
health = int(input())
strength = int(input())
agility = int(input())
will = int(input())

# --- Расчёт урона ----------------------------------
base_attack = 10
damage = base_attack + strength * 1.5
crit_damage = damage * 2
stamina = (health + will) // 5
max_stamina = stamina

# --- Формуляр героя --------------------------------
print("Характеристики героя:")
print(f"Здоровье:   {health}")
print(f"Сила:       {strength}")
print(f"Ловкость:   {agility}")
print(f"Воля:       {will}")
print()
print(f"Урон героя:        {damage:.1f}")
print(f"Критический урон:  {crit_damage:.1f}")
print(f"Запас сил:         {stamina}")
print()

# --- Главный цикл игры ---------------------------
running = True
actions = 0

while running:
    print("Что делаешь?")
    print("1 - осмотреться")
    print("2 - идти вперёд")
    print("3 - отдохнуть")
    print("4 - потрогать наковальню")
    print("5 - осмотреть полки")
    print("6 - тренировка")
    print("0 - выйти из кузницы")

    # --- Защита от неверного ввода ----------------
    valid = ("0", "1", "2", "3", "4", "5", "6")
    choice = input()
    while choice not in valid:
        print("Такого пункта нет. Введи номер пункта из меню.")
        choice = input()

    if choice == "1":
        print("Вы внимательно осматриваетесь. В кузнице тихо, "
              "только изредка потрескивает уголёк.")

    elif choice == "2":
        cost = 3
        if stamina >= cost:
            stamina -= cost
            print("Вы осторожно идёте вперёд. Пол скрипит под ногами.")
        else:
            health -= cost - stamina
            stamina = 0
            print("Сил больше нет — вы идёте на одном упорстве.")

    elif choice == "3":
        stamina += 1
        if stamina > max_stamina:
            stamina = max_stamina
        print("Вы присаживаетесь на край скамьи и переводите дух. "
              "Силы понемногу возвращаются.")

    elif choice == "4":
        stamina -= 1
        print("Вы осторожно касаетесь наковальни. Металл ещё хранит "
              "слабое тепло — кузница заброшена не так давно.")

    elif choice == "5":
        will += 1
        stamina -= 2
        print("На пыльной полке вы находите старую эмблему "
              "кузнечного цеха. Что-то внутри вас крепнет.")

    elif choice == "6":
        # --- Тренировочный бой ----------------------
        strikes = 6
        total_damage = 0
        crit_count = 0

        print("Вы подходите к старому чучелу, сколоченному из брёвен "
              "и обтянутому ржавыми листами железа.")
        print("Его оставил прошлый кузнец — тренировался, когда заказов "
              "не было.")
        print()
        print(f"Наносите {strikes} ударов.")

        for i in range(1, strikes + 1):
            if i % 3 == 0:
                hit_damage = crit_damage
                crit_count += 1
                print(f"Удар {i}: {hit_damage:.1f} — критический!")
            else:
                hit_damage = damage
                print(f"Удар {i}: {hit_damage:.1f}")

            total_damage += hit_damage

        print()
        print(f"Итог: {strikes} ударов, критических ударов: {crit_count}")
        print(f"Общий урон: {total_damage:.1f}")
        print(f"Средний урон: {total_damage / strikes:.1f}")

        stamina -= 4

    elif choice == "0":
        print("Вы выходите из кузницы на свежий воздух. "
              "Дверь со скрипом закрывается позади.")
        running = False

    else:
        print("Такого действия нет. Выберите номер из списка.")

    # --- Счётчик и строка состояния ------------------
    if running:
        actions += 1
        print()
        print(f"Здоровье: {health:5d} Запас сил: {stamina:5d}")

        # --- Проверка гибели ------------------------
        if health <= 0:
            print(f"{hero_name} падает без сил. Кузница забирает ещё одного гостя.")
            running = False

# --- Прощание --------------------------------------
print()
print(frame)
if health <= 0:
    print(f"Ты не дошёл, {hero_name}. Действий совершено: {actions}.")
else:
    print(f"Забег окончен, {hero_name}. Действий совершено: {actions}.")
print(frame)
