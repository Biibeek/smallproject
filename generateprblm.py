import random
import time
OPERATORS=["+","-" ,"*"]
MAX_OPERAND=12
MIN_OPERAND=3
TOTAL_PRBLM=10
def generate_prblm():
    left=random.randint(MIN_OPERAND,MAX_OPERAND)
    right=random.randint(MIN_OPERAND,MAX_OPERAND)
    operator=random.choice(OPERATORS)

    expr=str(left)+" "+operator+" "+str(right)
    ans=eval(expr)
    return expr,ans

wrong=0
input("press enter to start!!")
print("-----------------------------")
start_time=time.time()
for i in range(TOTAL_PRBLM):
    expr,ans=generate_prblm()
    while True:
        guess=int(input("problem #" + str(i+1) + ": " + expr +"="))
        if guess==ans:
            break
        wrong +=1
end_time=time.time()
total_time=round(end_time-start_time)

print(f"Nice work!!! you finished in {total_time} seconds")