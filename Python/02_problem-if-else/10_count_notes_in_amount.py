amount = int(input(("Enter amount: ")))


notes_2000 = amount // 2000
print("2000- ", notes_2000)
amount = amount % 2000

notes_500 = amount // 500
print("500- ", notes_500)
amount = amount % 500


notes_200 = amount // 200
print("200- ", notes_200)
amount = amount % 200

notes_100 = amount // 100
print("100- ", notes_100)
amount = amount % 100

notes_50 = amount // 50
print("50- ", notes_50)
amount = amount % 50

notes_20 = amount // 20
print("20- ", notes_20)
amount = amount % 20

notes_10 = amount // 10
print("10- ", notes_10)
amount = amount % 10

total_notes = notes_2000 + notes_500 + notes_200+ notes_100+ notes_50+ notes_20  + notes_10

print("TOtal notes-", total_notes)