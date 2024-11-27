import time
import json
import sys

questions_filename = 'questions.json'

if len(sys.argv) == 2:
    questions_filename = sys.argv[1]

try:
    with open(f"./{questions_filename}", 'r', encoding='utf-8') as file:
        questions = json.load(file)
except FileNotFoundError:
    print("Չհաջողվեց բեռնել հարցերը։")
    sys.exit(1)

print("""
*********** ՀԱՅՈՑ ՊԱՏՄՈՒԹՅՈՒՆ ***********
               Հարցախաղ
*****************************************
""")
time.sleep(1)
print("- Խաղում ընդգրկվում են 2 թիմեր։")
time.sleep(1)
print(f"- Ընդհանուր կա {len(questions)} հարց։")
time.sleep(1)
print(f"- Յուրաքանչյուր թիմին տրվում է {len(questions)/2}-ական հարց։")
time.sleep(1)
print("- Ճիշտ պատասխանի համար թիմը ստանում է 10 միավոր։")
time.sleep(1)
print("- Կհաղթի այն թիմը, որը կունենա ավելի շատ միավոր։")
time.sleep(1)
input("\nՍեղմեք Enter սկսելու համար։")
print("\nԳնացինք․․․\n")
time.sleep(1)

team1 = input("Խաղացող 1-ի անունը: ")
team2 = input("Խաղացող 2-ի անունը: ")

team1_score = 0
team2_score = 0

for i in range(len(questions)):
    curr_team = team2 if (i % 2) else team1;
    print(f"\n{i+1}. Հարց -> {curr_team}")
    print(questions[i]["question"])

    for ans_i in range(len(questions[i]["answers"])):
        print(f"({ans_i+1}) {questions[i]['answers'][ans_i]}")

    while True:
        try:
            answer = int(input("Պատասխանը(ներմուծված համարով): ")) - 1
            if answer < 0 or answer > len(questions[i]["answers"]):
                raise ValueError
            break
        except ValueError:
            print("Սխալ ներմուծում։")

    if answer == questions[i]["correct_answer"]:
        print("Ճիշտ է։")
        if i % 2 == 0:
            team1_score += 10
        else:
            team2_score += 10
    else:
        print("Սխալ է։")

time.sleep(1)
print("\nԽաղն ավարտվեց։")
time.sleep(1)
print(f"{team1}-ի հաշիվը: {team1_score}")
print(f"{team2}-ի հաշիվը: {team2_score}")
time.sleep(1)
if team1_score > team2_score:
    print(f"Հաղթեց։ {team1}-ը")
elif team1_score < team2_score:
    print(f"Հաղթեց։ {team2}-ը")

print("\nՇնորհակալություն խաղի մասնակիցներին։")
