# 1. A list contains the denominations as follows :
# D = [2000, 500, 200, 100 , 50, 20, 10, 5]
# Accept an amount from user and calculate how many
# minimum number of notes will be needed for that
# amount.



D = [2000,500,200,100,50,20,10,5]

amount = int(input('Enter amount :'))
note_count = {}

for note in D :
    if (amount >= note):
        count = amount // note
        amount = amount % note 
        note_count[note] = count

print('Minimum number of note required :')
total_notes =  0

for note,count in note_count.items():
    print(f'{note} : {count}')
    total_notes += count

print('total note = ', total_notes)