class Practice:
    def list_numbers(self):
        start = 1
        end = 8
        limit = 5

        numbers = list(range(start, end))
        for n in numbers:
            if n == limit:
                break
            print(n)


    def list_words(self):
        limit = 10
        words = [f"str{i}" for i in range(limit)]
        for word in words:
            print(word)


object_for_numbers = Practice()
print("lesson1")
object_for_numbers.list_numbers()

print("-"*200)

object_for_words = Practice()
print("lesson2")
object_for_words.list_words()