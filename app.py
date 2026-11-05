import sys
import time

def main():
    print(f"Sikeres futás a konténerből! Python verzió: {sys.version}")
    for i in range(1, 4):
        print(f"Feldolgozás... {i}/3")
        time.sleep(1)
    print("Kész!")

if __name__ == "__main__":
    main()