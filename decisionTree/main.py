from DecisionQuery import DecisionQuery
from DecisionResult import DecisionResult
from Node import Node



def main_decision_tree(questions):
    log_reg = DecisionResult("Логистическая Регрессия")
    lin_reg = DecisionResult("Линейная Регрессия")
    anova = DecisionResult("Дисперсионный Анализ")
    chi_square = DecisionResult("Хи-квадрат Пирсона")
    t_student = DecisionResult("Т-критерий Стъюдента")

    sixth = DecisionQuery(questions[5],
                          positive=t_student,
                          negative=log_reg)
    fifth = DecisionQuery(questions[4],
                          positive=chi_square,
                          negative=sixth)
    fourth = DecisionQuery(questions[3],
                           positive=lin_reg,
                           negative=fifth)
    third = DecisionQuery(questions[2],
                          positive=anova,
                          negative=lin_reg)
    second = DecisionQuery(questions[1],
                           positive=third,
                           negative=log_reg)
    first = DecisionQuery(questions[0],
                          positive=second,
                          negative=fourth)

    return first


if __name__ == '__main__':
    questions = ["Переменных больше двух?", "Зависимая переменная количественная?", "Сравнение групп?",
                 "Обе переменные количественные?", "Обе переменные номинативные?", "Сравнить переменные?"]
    main_decision_tree(questions).evaluate(Node())