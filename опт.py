import random

# Задание 1: Инспекция объекта
iface = {
    "m1": lambda x: [x],
    "m2": lambda x, y: [x, y],
    "m3": lambda x, y, z: [x, y, z]
}

# Инспекция: ключи и количество аргументов
inspection_result = [[key, func.__code__.co_argcount] for key, func in iface.items()]
print("Inspection Result:", inspection_result)
# Ожидаемый вывод: [['m1', 1], ['m2', 2], ['m3', 3]]

# Задание 2: Генерация случайных чисел
def random_min_max(min_value=0, max_value=10):
    return random.randint(min_value, max_value)

print("Random Number (5-15):", random_min_max(5, 15))

# Задание 3: Генерация ключа
def generate_key(length, characters):
    return ''.join(random.choice(characters) for _ in range(length))

characters = 'abcdefghijklmnopqrstuvwxyz0123456789'
key = generate_key(16, characters)
print("Generated Key:", key)

# Задание 4: Преобразование IP в число
def ip_to_number(ip):
    parts = list(map(int, ip.split('.')))
    shifts = [24, 16, 8, 0]
    return sum(part << shift for part, shift in zip(parts, shifts))

ip = "127.0.0.1"
ip_number = ip_to_number(ip)
print(f"IP {ip} as Number:", ip_number)

# Дополнительный вывод
ips = ["127.0.0.1", "10.0.0.1", "192.168.1.10", "165.225.133.150", "0.0.0.0", "8.8.8.8"]
for ip in ips:
    print(f"{ip} -> {ip_to_number(ip)}")
