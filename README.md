# quiz_arm_history

### A compeptitive quiz game for checking students' homework

## Gameplay

```shell
*********** ՀԱՅՈՑ ՊԱՏՄՈՒԹՅՈՒՆ ***********
               Հարցախաղ
*****************************************

- Խաղում ընդգրկվում են 2 թիմեր։
- Ընդհանուր կա 20 հարց։
- Յուրաքանչյուր թիմին տրվում է 10-ական հարց։
Սեղմեք Enter սկսելու համար։

Գնացինք․․․
Խաղացող 1-ի անունը: team1
Խաղացող 2-ի անունը: team2

1. Հարց
Who is the first president of Armenia?
1. tigran mets
2. vazgen sargsyan
3. levon ter-petrosyan
4. serzh sargsyan
Պատասխանը գրեք թվով: 3
Ճիշտ է։

Խաղը ավարտվեց։
team1-ի հաշիվը: 10
team2-ի հաշիվը: 0
Հաղթեց։ team1-ը

Շնորհակալություն խաղում մասնակցողներին։
```

## Custom Questions Lists

You can add your custom questions in your <questions_name>.json file in this format

```json
[
  {
    "question": "Who is the first president of Armenia?",
    "correct_answer": 2,
    "answers": [
      "tigran mets",
      "vazgen sargsyan",
      "levon ter-petrosyan",
      "serzh sargsyan"
    ]
  }
]
```
