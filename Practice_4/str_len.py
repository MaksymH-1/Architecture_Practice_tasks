import subprocess

def main():

    str_input = input("Введіть рядок для визначення довжини: ")

    #запсук зовнішньої команди wc -c (word count --bytes)
    proc = subprocess.run(
        ["wc", "-c"],
        input = str_input,
        capture_output = True,
        text = True
    )

    #отримання результату (stdout)
    len = proc.stdout.strip()

    #вивід результату
    print(f"Довжина введеного рядка : {len}")

if __name__ == "__main__":
    main()