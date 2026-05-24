import random
import time

class Practice:
    def rostics_monitoring(self):
        limit = 10
        alert = 85
        pause = 0.2

        i = 0
        while i < limit:
            current_load = random.randint(0, 100)

            print(f"Текущая нагрузка: {current_load}%")

            if current_load > alert:
                print(f"🚨 WARNING! Превышен порог нагрузки в {alert}%!")

            time.sleep(pause)
            i += 1

object_for_rostics = Practice()
object_for_rostics.rostics_monitoring()