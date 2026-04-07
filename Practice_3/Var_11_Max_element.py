import threading
import time
import random

local_maxes = []

lock = threading.Lock()

def find_max(chunk, thread_name):
    chunk_max = chunk[0]

    for num in chunk:
        if num > chunk_max:
            chunk_max = num

    print(f"{thread_name} знайшов максимум: {chunk_max}")

    #Безпечне додавання з lock
    with lock:
        local_maxes.append(chunk_max)
        
    time.sleep(1)

def main():
    data_list = [random.randint(1,1000) for i in range(80)] #створення списку з 80 елементів, згенерованих рандомно від 1 до 1000

    threads_num = 4
    chunk_size = len(data_list) // threads_num
    threads = []

    for i in range(threads_num):
        start_index = i * chunk_size

        thread_name = f"Потік {i + 1}"

        chunk = data_list[start_index:start_index + chunk_size] #Ділимо список на частини для обробки кожним потоком

        t = threading.Thread(target=find_max, args=(chunk, thread_name)) 
        threads.append(t)
        t.start()

    #Очікування завершення потоків
    for t in threads:
        t.join()
    
    result = local_maxes[0]
    for num in local_maxes:
        if num > result:
            result = num

    print("\nУсі потоки завершили роботу.")
    print(f"\nЛокальні максимуми потоків: {local_maxes}")
    print(f"Загальний знайдений максимум: {result}")
    
    # Перевірка вбудованою функцією Python для підтвердження
    print(f"Фактичний максимум (перевірка max()): {max(data_list)}")

if __name__ == "__main__":
    main()