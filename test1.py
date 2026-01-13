from ascii_art import show_welcome
from quiz_logic import start_quiz

def main():
    show_welcome()
    while True:
        choice = input("გსურთ თამაში დაიწყოთ? (Y/N): ").upper()
        if choice == "Y":
            start_quiz()
        elif choice == "N":
            print("თამაში დასრულდა. ნახვამდის!")
            break
        else:
            print("გთხოვთ შეიყვანოთ მხოლოდ Y ან N.\n")

if __name__ == "__main__":
    main()