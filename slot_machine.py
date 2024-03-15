#slot_machine.py
import random
symbols = ['🍒',' 🍇', '🍉', '7️⃣']
results = random.choices(symbols, k=3)
print('  | '.join(results), end = '\n\n')
if results == '7️⃣':
  print('Jackpot! 💰')
else:
  print('Thanks for playing!')

#lot_machyne.py
import random

def play():
  symbols = ['🍒',' 🍇', '🍉', '7️⃣']
  results = random.choices(symbols, k=3)
  print('  | '.join(results), end = '\n\n')

  #if all(symbols == '🍒' or symbols == '🍇' or symbols == '🍉' or symbols == '7️⃣' for symbols in results):
  if len(set(results)) == 1:
    print('Jackpot! 💰')
  else:
    print('Thanks for playing!')

play()