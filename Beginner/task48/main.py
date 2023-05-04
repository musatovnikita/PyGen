a, b, c = int(input()), int(input()), int(input())
if a == b != c:
    print("Равнобедренный")
elif a != b == c:
    print("Равнобедренный")
elif a == c != b:
    print("Равнобедренный")
elif a == b ==c:
    print("Равносторонний")
elif a != b != c:
    print("Разносторонний")