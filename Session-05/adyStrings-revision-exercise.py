# ---------------------------------------------------------------------
# Revision Exercise for Strings
#
# Filename: strings-revision-exercise.py
# Location: Session-05
#
# URI:      https://github.com/AdyGCode/ICTPRG302-Classwork-2025-S1/blob/main/Session-05/strings-revision-exercise.py
# Author:   Rafael Avigad <rafael.avigad@nmtafe.wa.edu.au>
#
# Instructions:
# - Copy the file from GitHub
# - Save to the Session-05 folder
# - Read through the exercise
# - Solve each problem in turn
# ---------------------------------------------------------------------

# Define variables
tic_tac = ("- X O\n" +
           "X - X\n" +
           "O - O\n")
# helpful reference
#012345678912345678
'- X OnX - XnO - On'

# ---------------------------------------------------------------------
# Exercise 1: what is the length of the string?
# insert code here
print(len(tic_tac))
print(tic_tac[1:2])

# ---------------------------------------------------------------------
# Exercise 2: make the following print True by substituting
# each `?` with a **different** value
#      print(tic_tac[0] ==
#      tic_tac[?] ==
#      tic_tac[?]) # True

# clue: Here is an example that prints True:
print(bool(tic_tac[0] == tic_tac[8] == tic_tac[14]))
# but remember you must use different integer values!
# notice that line breaks don't matter inside brackets

# ---------------------------------------------------------------------
# Exercise 3: make the following print True by substituting
# each `?` with a **different** value
#print(tic_tac[2] ==
#      tic_tac[?] ==
#      tic_tac[?]) # True

print(bool(tic_tac[2] == tic_tac[6] == tic_tac[10]))
# ---------------------------------------------------------------------
# Exercise 4: make the following print True by substituting
# each `?` with a **different** value
#print(tic_tac[5] ==
#      tic_tac[?] ==
#      tic_tac[?]) # True
print(bool(tic_tac[5] == tic_tac[11] == tic_tac[-1]))
# ---------------------------------------------------------------------
# Exercise 5: combine two slices of the original string
# for X to win the game:
print(tic_tac[0:1] + 'X' + tic_tac[0:1])
# should print:
# - X O
# X X X
# O - O
'- X OnX - XnO - On'
# ---------------------------------------------------------------------
# Exercise 6: combine two slices of the original string
# for O to win the game:
#print(tic_tac[?:?] + 'O' + tic_tac[?:?])
# should print:
# - X O
# X - X
# O O O

# ---------------------------------------------------------------------
# Exercise 7: Bonus question!
# Complete the following to print 'XXX'
#print(tic_tac[?:?:?])
