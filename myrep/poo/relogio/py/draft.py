import sys

class Watch:
    
    def __init__(self, hour, minute, second):
        self._hour = 0
        self._minute = 0
        self._second = 0 

        self.set_hour(hour)
        self.set_minute(minute)
        self.set_second(second)

    def get_hour(self):
        return self._hour

    def get_minute(self):
        return self._minute

    def get_second(self):
        return self._second

    def set_hour(self, hour):
        if 0 <= hour <= 23:
            self._hour = hour

    def set_minute(self, minute):
        if 0 <= minute <= 59:
            self._minute = minute

    def set_second(self, second):
        if 0 <= second <= 59:
            self._second = second

    def nextSecond(self):
        if self._second == 59:
            self._second = 0
            if self._minute == 59:
                self._minute = 0 
                if self._hour == 23:
                    self._hour = 0
                else:
                    self._hour += 1
            else:
                self._minute += 1
        else:
            self._second += 1

    def toString(self):
        return f"{self._hour:02d}:{self._minute:02d}:{self._second:02d}"
        
    def __str__(self):
        return self.toString()
    
if __name__ == "__main__":
    
    my_watch = Watch(0, 0, 0)

    while True:
        try:
            line = input().strip()
            if not line:
                continue

            print(f"${line}")
            
            parts = line.split()
            command = parts[0]
    
            if command == "show":
                print(my_watch.toString())

            elif command == "next":
                my_watch.nextSecond()

            elif command == "set":
                if len(parts) != 4:
                    print("(fail: formato invalido)")
                else:
                    h = int(parts[1])
                    m = int(parts[2])
                    s = int(parts[3])

                    valid_h = (0 <= h <= 23)
                    valid_m = (0 <= m <= 59)
                    valid_s = (0 <= s <= 59)

                    if not valid_h:
                        print("(fail: hora errada)")
                    elif not valid_m:
                        print("(fail: minuto invalido)")
                    elif not valid_s:
                        print("(fail: segundo invalido)")
                    
                    if valid_h:
                        my_watch.set_hour(h)
                    if valid_m:
                        my_watch.set_minute(m)
                    if valid_s:
                        my_watch.set_second(s)
            
            elif command == "end":
                break

        except EOFError:
            break
        except ValueError:
            print("(fail: formato invalido)")
        except IndexError:
            print("(fail: formato invalido)")