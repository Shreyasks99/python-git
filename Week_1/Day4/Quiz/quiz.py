from question import Question
class Quiz:

    questions = []#9845246666
    #8861036692
    #9739910668

    @classmethod
    def load_question(cls):
        with open("question.txt") as file:
            data = file.readlines()
            for line in data:
                q = line.split(",")
                cls.questions.append(Question(*q))

        print(cls.questions)

    

 
    @classmethod
    def begin_quiz(cls):
        cls.load_question()
        '''print(f"Total number of question:{len(cls.questions)}")
        num_correct = 0
        num_incorrect = 0
        for i, question in enumerate(cls.questions):
            print(f"{i+1}:{question}")
            ch = input("Enter the choice [A,B,C,D] only...")
            if ch == question.c_answer.strip():
                num_correct += 1
            else:
                num_incorrect += 1        
        #cls.show_result(num_correct, num_incorrect)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                0

    @classmethod
    def show_result(cls,num_correct,num_incorrect):
        total_q = len(cls.questions)
        print(f"Total number of questions:{total_q}")
        print(f"Correct Answers:{num_correct}")
        print(f"Incorrect Answers:{num_incorrect}")
        percentage = ((num_correct)/total_q)*100
        print(f"Percentage:{percentage}")
        if percentage >= 65:
            print("Congratulation...")
        else:
            print("Better luck next time")
'''