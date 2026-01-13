def show_welcome():
    print("""
                                                                    ..;===+.
                                                                .:=iiiiii=+=
                                                             .=i))=;::+)i=+,
                                                          ,=i);)I)))I):=i=;
                                                       .=i==))))ii)))I:i++
                                                     +)+))iiiiiiii))I=i+:'
                                .,:;;++++++;:,.       )iii+:::;iii))+i='
                             .:;++=iiiiiiiiii=++;.    =::,,,:::=i));=+'
                           ,;+==ii)))))))))))ii==+;,      ,,,:=i))+=:
                         ,;+=ii))))))IIIIII))))ii===;.    ,,:=i)=i+
                        ;+=ii)))IIIIITIIIIII))))iiii=+,   ,:=));=,
                      ,+=i))IIIIIITTTTTITIIIIII)))I)i=+,,:+i)=i+
                     ,+i))IIIIIITTTTTTTTTTTTI))IIII))i=::i))i='
                    ,=i))IIIIITLLTTTTTTTTTTIITTTTIII)+;+i)+i`
                    =i))IIITTLTLTTTTTTTTTIITTLLTTTII+:i)ii:'
                   +i))IITTTLLLTTTTTTTTTTTTLLLTTTT+:i)))=,
                   =))ITTTTTTTTTTTLTTTTTTLLLLLLTi:=)IIiii;
                  .i)IIITTTTTTTTLTTTITLLLLLLLT);=)I)))))i;
                  :))IIITTTTTLTTTTTTLLHLLLLL);=)II)IIIIi=:
                  :i)IIITTTTTTTTTLLLHLLHLL)+=)II)ITTTI)i=
                  .i)IIITTTTITTLLLHHLLLL);=)II)ITTTTII)i+
                  =i)IIIIIITTLLLLLLHLL=:i)II)TTTTTTIII)i'
                +i)i)))IITTLLLLLLLLT=:i)II)TTTTLTTIII)i;
              +ii)i:)IITTLLTLLLLT=;+i)I)ITTTTLTTTII))i;
             =;)i=:,=)ITTTTLTTI=:i))I)TTTLLLTTTTTII)i;
           +i)ii::,  +)IIITI+:+i)I))TTTTLLTTTTTII))=,
         :=;)i=:,,    ,i++::i))I)ITTTTTTTTTTIIII)=+'
       .+ii)i=::,,   ,,::=i)))iIITTTTTTTTIIIII)=+
      ,==)ii=;:,,,,:::=ii)i)iIIIITIIITIIII))i+:'
     +=:))i==;:::;=iii)+)=  `:i)))IIIII)ii+'
   .+=:))iiiiiiii)))+ii;
  .+=;))iiiiii)));ii+
 .+=i:)))))))=+ii+
.;==i+::::=)i=;
,+==iiiiii+,
`+=+++;`
           """)
    print("კოსმოსური Quiz თამაშში მოგესალმებით!\n")

def ask_question(question, options, correct_answer):
    print(question)
    for key, value in options.items():
        print(f"{key}: {value}")
    answer = input("თქვენი პასუხი: ").upper()
    if answer == correct_answer:
        print("სწორია!\n")
        return 1
    else:
        print(f"არასწორია! სწორი პასუხი: {correct_answer}\n")
        return 0

def start_quiz():
    questions = [
        {
            "question": "რა პლანეტა ცნობილია წითელი პლანეტად?",
            "options": {"A": "ზენიტი", "B": "მარსი", "C": "სატურნი", "D": "ვენერა"},
            "answer": "B"
        },
        {
            "question": "რა არის კოსმოსში ვარსკვლავების მთავარი შემადგენელი ნაწილი?",
            "options": {"A": "ჰელიუმი", "B": "მჟავა", "C": "წყალი", "D": "ნახშირი"},
            "answer": "A"
        },
        {
            "question": "რამდენი პლანეტა აქვს მზის სისტემას?",
            "options": {"A": "8", "B": "9", "C": "7", "D": "10"},
            "answer": "A"
        },
        {
            "question": "რა პლანეტა ყველაზე დიდი ზომისაა?",
            "options": {"A": "იუპიტერი", "B": "მარსი", "C": "ვენერა", "D": "სატურნი"},
            "answer": "A"
        },
        {
            "question": "რა ეწოდება მთვარეს დედამიწის გარშემო?",
            "options": {"A": "სამყარო", "B": "სპუტნიკი", "C": "მთვარე", "D": "კოსმოსური ლაბორატორია"},
            "answer": "C"
        },
    ]

    score = 0
    for q in questions:
        score += ask_question(q["question"], q["options"], q["answer"])
    print(f"თქვენი ქულა: {score}/{len(questions)}\n")
    print("თამაში დასრულებულია. მადლობა თამაშისთვის!\n")

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