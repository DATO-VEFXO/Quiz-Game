def main():
    show_welcome()
    while True:
        choice = input("გსურთ თამაში დაიწყოთ? (KI/ARA): ").upper()
        if choice == "KI":
            start_quiz()
        elif choice == "ARA":
            print("თამაში დასრულდა. ნახვამდის!")
            break
        else:
            print("გთხოვთ შეიყვანოთ მხოლოდ KI ან ARA.\n")
if __name__ == "__main__":
    main()
