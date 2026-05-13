# def get_fib_list(n):
#     a, b = 0, 1
#     fibs = []
#     for _ in range(n):
#         fibs.append(a)
#         a, b = b, a + b
#     return fibs

# numbers = get_fib_list(10)
# print(numbers)
# even_fibs = list(filter(lambda x :x %2 ==0, numbers))
# print(even_fibs)
# squared_fibs = list(map(lambda x : x**2, numbers))
# print(squared_fibs)


# command = ""
# while command.lower() != "quit":
#     command = input("enter the command(type quit toexit: ")
#     print(f"excuting:{command}")


# while True :
#     name = input("enter your name: ")
#     if name.isalpha():
#         break
#     print("Invalid name Please use letters only")
# print(f"Hello, {name}")




# attempts = 3
# while attempts > 0:
#     password = input("enter password")
#     if password == "secret123":
#         print("access granted")
#         break
#     attempts -=1
#     print(f"wrong !{attempts} left")
# else:
    
#     print("Accout locked")



# # tasks = ["Email Boss", "Fix Bug", "Refactor Code"]
# tasks = [1,2,3,4,5,6,6,7,8,9,0,6,4,3,2,2]
# while tasks:
#     current_task = tasks.pop()
#     print(f"currently working on:{current_task}")
#     print(f"remaining task:{len(tasks)}")
# print("all work finished!")