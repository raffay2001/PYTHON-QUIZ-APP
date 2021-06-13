#--------------------------------------OOP QUIZ APPLICATION------------------------------------------------------#
import sys
import random
import datetime

# QUESTION_BANK CLASS


class Question_Bank:

    def __init__(self):
        self.creation_date = datetime.date.today()

    def take_question(self):
        self.question = input(f"\nEnter the question that you wanna add: ")
        self.opt_1 = input(f"Enter option 1: ")
        self.opt_2 = input(f"Enter option 2: ")
        self.opt_3 = input(f"Enter option 3: ")
        self.answer = int(input(f"Enter correct option number: "))

        return self.question, self.opt_1, self.opt_2, self.opt_3, self.answer

    def save_question(self):

        self.Record = list(self.take_question())

        self.file = open("studentDB.txt", "a")

        self.file.write(
            f"{self.Record[0]}, {self.Record[1]}, {self.Record[2]}, {self.Record[3]}, {self.Record[4]}, {self.creation_date}, \n")

        self.file.close()

    def read_file(self):

        self.Dict = {}

        self.file = open("studentDB.txt", "r")

        self.content = self.file.readlines()

        self.count = 1

        for record in self.content:

            temp = record.split(", ")

            temp.pop()

            self.Dict.update(
                {
                   self.count: temp
                }
            )

            self.count += 1

        return self.Dict

# QUIZ CLASS

class Quiz:

    def init(self):
        self.questions = Question_Bank()                # < / BY USING COMPOSITION MAKING AN INSTANCE VARIABLE WHICH IS EQUAL TO THE Question_Bank Type >
        

    def attempt_quiz(self):
        
        self.dict = Question_Bank().read_file()

        self.key = random.randint(1, len(self.dict))

        self.record = self.dict.get(self.key)

        print(f"\nThe Question was created on: {Question_Bank().creation_date}")

        print(f"Your Question is: {self.record[0]}\nOptions Are: \n1.{self.record[1]}\n2.{self.record[2]}\n3.{self.record[3]}")


        self.ans = int(input(f"Enter the correct option number: "))

        if 1 <= self.ans <= 3:

            if self.ans == int(self.record[4]):
                print(f"\n--------------------------------Hurrayyy!!!, Your Answer is Correct!!-----------------------------------------\n")

            else:
                print(f"\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!Incorrect Answer!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! :/\n")

        else:
            print(f"Please Enter a Valid Option!!")


# MENU CLASS

class Menu:

    def init(self):
        pass

    def display_menu(self):
        print(f"Welcome To The Quiz App!!\nOperations Menu:\n1.Add a Question To The Question Bank\n2.Take the Quiz\n3.Exit From The Application:((\n")

    def run(self):
        self.question_bank = Question_Bank()
        self.quiz = Quiz()

        while True:
            self.display_menu()

            self.choice = int(input(f"Enter your choice number: "))

            if 1 <= self.choice <= 3:

                if self.choice == 1:

                    self.question_bank.save_question()

                elif self.choice == 2:

                    self.d = self.question_bank.read_file()

                    if len(self.d) == 0:
                        print(f"Sorry, The Question Bank is Empty:((\nPlease Add Some Questions")
                        self.question_bank.save_question()

                    else:
                        self.quiz.attempt_quiz()

                elif self.choice == 3:

                    sys.exit(0)

            else:
                print(f"Please Enter a Valid Option!!")


if __name__ == "__main__":
    Menu().run()
