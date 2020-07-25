from time import sleep, time


class TrafficLight:
    __color1 = "\033[31m {}".format('red')
    __color2 = "\033[33m {}".format('yellow')
    __color3 = "\033[32m {}".format('green')

    def running(self):
        time_end = float(input('На сколько секунд включить светофор?: '))
        t_end = time() + time_end
        while True:
            print(TrafficLight.__color1)
            sleep(7)
            if time() > t_end:
                break
            print(TrafficLight.__color2)
            sleep(2)
            if time() > t_end:
                break
            print(TrafficLight.__color3)
            sleep(7)
            if time() > t_end:
                break
            print(TrafficLight.__color2)
            sleep(2)
            if time() > t_end:
                break

        return "\033[30m {}".format('Светофор выключен')


obj = TrafficLight()
print(obj.running())
