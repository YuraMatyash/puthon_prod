  #аргументы с ключевыми словами делают код более читаемым
def get_info(name, qty):
    info = f"{name} wrote {qty} posts"
    return info

print(get_info(name='Yura', qty=22))  # аргументы с ключевыми словами