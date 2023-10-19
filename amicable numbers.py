M = int(input("Enter the first number (M): "))
N = int(input("Enter the second number (N): "))
sum_M = sum(i for i in range(2, M) if M % i == 0)
sum_N = sum(i for i in range(2, N) if N % i == 0)
if sum_M == N and sum_N == M:
    print(f"{M} and {N} are amicable numbers.")
else:
    print(f"{M} and {N} are not amicable numbers.")
