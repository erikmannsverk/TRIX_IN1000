"""
07.04: Studenter og quiz-score
"""

class Student:

    def __init__(self, navn, quizScore, antQuiz):
        self._navn = navn
        self._quizScore = quizScore
        self._antQuiz = antQuiz

    def leggTilQuizScore(self, quizScore):
        self._quizScore += quizScore
        self._antQuiz += 1

    def gjennomsnittligScore(self):
        return self._quizScore / self._antQuiz

    def skrivUtInfo(self):
        print(f"Navn: {self._navn}. Total score: {self._quizScore}. Antall Quizer: {self._antQuiz}. Gjennomsnittscore: {self.gjennomsnittligScore()}")

# Oppretter tre student objekter
s1 = Student("Joakim", 20, 2)
s2 = Student("Kristin", 40, 4)
s3 = Student("Dag", 35, 4)

# Legg til quiz score 1. gang
s1.leggTilQuizScore(10)
s2.leggTilQuizScore(7)
s3.leggTilQuizScore(8)

# Legg til quiz score 2. gang
s1.leggTilQuizScore(6)
s2.leggTilQuizScore(10)
s3.leggTilQuizScore(8)

# Gjennomsnitt og totale
print()
s1.skrivUtInfo()
print()
s2.skrivUtInfo()
print()
s3.skrivUtInfo()
print()
