## Al 1

# num_list = []

# for i in range(1000):
# 	if i % 3 == 0 or i % 5 == 0:
# 		num_list.append(i)

# All = sum(num_list)


# print All


# # ## Al 2
# fib_list =[1 ,1]
# f = 1
# even_list = []

# while f <= 4000000:
# 	f= fib_list[-1] + fib_list[-2]
# 	fib_list.append(f)

# del fib_list[-1]

# for i in fib_list:
# 		if i % 2 == 0:
# 			even_list.append(i)

# answer = sum(even_list)

# print answer



## Al 3

def prime_factors(n):
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n = n/d
        d = d + 1

    print max(factors)

prime_factors(600851475143)




