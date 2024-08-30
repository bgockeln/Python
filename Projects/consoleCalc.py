#Console Calculator

mainloop = 1

while mainloop == 1:
      print("""
      Dikt sein Kalkulator
            1. Addition
            2. Subtraktion
            3. Multiplikation
            4. Division
            5. Exit
            """)
      def addit():
            numA = int(input("Zahl 1: "))
            numB = int(input("Zahl 2: "))
            numC = numA + numB
            print(numA, "+", numB, "=", numC )
            input("Weiter mit Enter")
      def sub():
            numA = int(input("Zahl 1: "))
            numB = int(input("Zahl 2: "))
            numC = numA - numB
            print(numA, "-", numB, "=", numC)
            input("Weiter mit Enter")
      def multip():
            numA = int(input("Zahl 1: "))
            numB = int(input("Zahl 2: "))
            numC = numA + numB
            print(numA, "*", numB, "=", numC)
            input("Weiter mit Enter")
      def divis():
            numA = int(input("Zahl 1: "))
            numB = int(input("Zahl 2: "))
            numC = numA / numB
            print(numA, "/", numB, "=", numC)
            input("Weiter mit Enter")

      choice = int(input("Auswahl 1-5: "))
      if choice == 1:
            addit()
      elif choice == 2:
            sub()
      elif choice == 3:
            multip()
      elif choice == 4:
            divis()
      elif choice == 5:
            mainloop = 0
      


           