choices = {
    "ชอบเล่นเกม" : None,
    "ชอบดูหนัง" : None,
    "ชอบฟังเพลง" : None,
    "ชอบหลับในคาบ" : None,
}




choices["ชอบเล่นเกม"] = "IntVar()"
choices["ชอบดูหนัง"] = "IntString()"

print(choices.keys())
print(choices.items())
print(choices.values())