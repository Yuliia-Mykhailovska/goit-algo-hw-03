import random
def get_numbers_ticket(min, max, quantity):
    try:
        if min >= 1 and max <= 1000:
            lottery_numbers = set()
            while len(lottery_numbers) < quantity:
                lottery_numbers.add(random.randint(min, max))
        return sorted(list(lottery_numbers))
    except:
        return []
     
        
lottery_numbers = get_numbers_ticket(1, 1000, 6)
print("Your numbers:", lottery_numbers)
    

   
      
