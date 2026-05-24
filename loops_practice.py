class Practice:

    def list_words(self):
        limit = 10
        words = [f"str{i}" for i in range(limit)]
        for word in words:
            print(word)

object_for_words = Practice()
print("lesson2")
object_for_words.list_words()