# Returns a list of prime numbers from 1–50
def prime_numbers(end):
    for num in range(1, end):    
        status = True

        for i in range(2, num):
            if num%i==0:
                status = False
                break

        if status:
            print(num,end="\t")

prime_numbers(50)
    