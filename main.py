import time
import json

with open('/home/mika/quiz_arm_history/questions_elen.json', 'r', encoding='utf-8') as file:
    questions = json.load(file)

print("""
*********** ՀԱՅՈՑ ՊԱՏՄՈՒԹՅՈՒՆ ***********
               Հարցախաղ
*****************************************
""")
time.sleep(1)
print("- Խաղում ընդգրկվում են 2 թիմեր։")
time.sleep(1)
print("- Ընդհանուր կա 20 հարց։")
time.sleep(1)
print("- Յուրաքանչյուր թիմին տրվում է 10-ական հարց։")
time.sleep(1)
print("Սեղմեք Enter սկսելու համար։")
input()
print("Գնացինք․․․")

team1 = input("Խաղացող 1-ի անունը: ")
team2 = input("Խաղացող 2-ի անունը: ")

team1_score = 0
team2_score = 0

for i in range(len(questions)):
    print(f"\n{i+1}. Հարց")
    print(questions[i]["question"])

    for ans_i in range(len(questions[i]["answers"])):
        print(f"{ans_i+1}. {questions[i]['answers'][ans_i]}")

    answer = int(input("Պատասխանը գրեք թվով: ")) - 1

    if answer == questions[i]["correct_answer"]:
        print("Ճիշտ է։")
        if i % 2 == 0:
            team1_score += 10
        else:
            team2_score += 10
    else:
        print("Սխալ է։")

time.sleep(1)
print("\nԽաղը ավարտվեց։")
time.sleep(1)
print(f"{team1}-ի հաշիվը: {team1_score}")
print(f"{team2}-ի հաշիվը: {team2_score}")
time.sleep(1)
if team1_score > team2_score:
    print(f"Հաղթեց։ {team1}-ը")
elif team1_score < team2_score:
    print(f"Հաղթեց։ {team2}-ը")

print("\nՇնորհակալություն խաղում մասնակցողներին։")