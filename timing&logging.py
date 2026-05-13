import random
#Genearate 1000 random intergers between 1 and 1000
random_nums = [random.randint(1,1000)for _ in range(1000)]
def is_prime(n):
    if n<2 :return False
    for i in range(2, int(n**0.5)+1):
        if n %i ==0:
            return False
    return True
#filter for primes and Map to suare them
# we cast to list ot evaluate the lazy iterators
processed_nums = list(map(lambda x:x**2, filter(is_prime, random_nums)))
print(f"Found {len(processed_nums)} primes. First 5 squared results: {processed_nums[:5]}")