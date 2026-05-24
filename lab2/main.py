import math
import base64
from datetime import datetime, timedelta

BUS_SPEED = 3


class Position:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def calc_distance(self, target):
        return math.sqrt((self.x - target.x) ** 2 + (self.y - target.y) ** 2)


class Stop:
    def __init__(self, title="", pos=None, travel_time=0):
        self.title = title
        self.pos = pos if pos else Position()
        self.travel_time = travel_time


class ListNode:
    def __init__(self, stop=None):
        self.stop = stop
        self.nxt = None
        self.prv = None


class RouteList:
    def __init__(self):
        self.start = None
        self.end = None
        self.count = 0

    def _get_travel_time(self, p1, p2):
        dist = p1.calc_distance(p2)
        return round(dist / BUS_SPEED)

    def add_stop(self, stop):
        node = ListNode(stop)

        if self.count == 0:
            stop.travel_time = 0
            self.start = self.end = node
            self.count += 1
            return

        if self.count == 1:
            t = self._get_travel_time(self.start.stop.pos, stop.pos)
            self.start.stop.travel_time = t
            stop.travel_time = 0

            self.start.nxt = node
            node.prv = self.start
            self.end = node
            self.count += 1
            return

        nearest = self.start
        min_dist = float("inf")
        cur = self.start
        while cur:
            d = stop.pos.calc_distance(cur.stop.pos)
            if d < min_dist:
                min_dist = d
                nearest = cur
            cur = cur.nxt

        if nearest == self.start:
            t = self._get_travel_time(stop.pos, self.start.stop.pos)
            stop.travel_time = t

            node.nxt = self.start
            self.start.prv = node
            self.start = node
            self.count += 1
            return

        if nearest == self.end:
            t = self._get_travel_time(self.end.stop.pos, stop.pos)
            self.end.stop.travel_time = t
            stop.travel_time = 0

            self.end.nxt = node
            node.prv = self.end
            self.end = node
            self.count += 1
            return

        d_prv = stop.pos.calc_distance(nearest.prv.stop.pos)
        d_nxt = stop.pos.calc_distance(nearest.nxt.stop.pos)

        if d_prv < d_nxt:
            t1 = self._get_travel_time(nearest.prv.stop.pos, stop.pos)
            t2 = self._get_travel_time(stop.pos, nearest.stop.pos)

            nearest.prv.stop.travel_time = t1
            stop.travel_time = t2

            node.prv = nearest.prv
            node.nxt = nearest
            nearest.prv.nxt = node
            nearest.prv = node
        else:
            t1 = self._get_travel_time(nearest.stop.pos, stop.pos)
            t2 = self._get_travel_time(stop.pos, nearest.nxt.stop.pos)

            nearest.stop.travel_time = t1
            stop.travel_time = t2

            node.prv = nearest
            node.nxt = nearest.nxt
            nearest.nxt.prv = node
            nearest.nxt = node

        self.count += 1

    def get_total_time(self):
        total = 0
        cur = self.start
        while cur:
            total += cur.stop.travel_time
            cur = cur.nxt
        return total

    def find_stop_after_n(self, from_title, n, depart_time=None):
        cur = self.start
        while cur and cur.stop.title != from_title:
            cur = cur.nxt

        if not cur:
            print(f"Остановка '{from_title}' не найдена")
            return

        mins = 0
        for _ in range(n):
            mins += cur.stop.travel_time
            cur = cur.nxt
            if not cur:
                print(f"Маршрут закончился раньше чем через {n} остановок")
                return

        s = cur.stop
        print(f"  Через {n} остановок: {s.title} ({s.pos.x}, {s.pos.y})")
        print(f"  Время в пути: {mins} мин")

        if depart_time:
            arrival = depart_time + timedelta(minutes=mins)
            print(f"  Время прибытия: {arrival.strftime('%H:%M')}")

    def show(self):
        if not self.start:
            print("  Маршрут пуст")
            return

        print("Маршрут:")
        cur = self.start
        idx = 1
        while cur:
            s = cur.stop
            line = f"  {idx:>2}. {s.title:<20} ({s.pos.x:>5}, {s.pos.y:>5})"
            if cur.nxt:
                line += f"  →  [{s.travel_time} мин]"
            else:
                line += "  (конечная)"
            print(line)
            cur = cur.nxt
            idx += 1

        print(f"\n  Общее время маршрута: {self.get_total_time()} мин")

    def reverse(self):
        if self.count < 2:
            return

        saved_time = 0
        cur = self.start

        while cur:
            cur_time = cur.stop.travel_time
            tmp = cur.nxt

            cur.nxt = cur.prv
            cur.prv = tmp

            cur.stop.travel_time = saved_time
            saved_time = cur_time

            cur = tmp

        self.start, self.end = self.end, self.start

    def save_to_file(self, filename="route.txt"):
        if not self.start:
            print("  Маршрут пуст, файл не создан")
            return

        with open(filename, "w", encoding="utf-8") as f:
            cur = self.start
            while cur:
                s = cur.stop
                raw = f"{s.title}|{s.pos.x}|{s.pos.y}|{s.travel_time}"
                encoded = base64.b64encode(raw.encode("utf-8")).decode("utf-8")
                f.write(encoded + "\n")
                cur = cur.nxt

        print(f"  Маршрут сохранён в файл: {filename}")

    def load_from_file(self, filename="route.txt"):
        self.start = None
        self.end = None
        self.count = 0

        with open(filename, "r", encoding="utf-8") as f:
            lines = f.readlines()

        for line in lines:
            line = line.strip()
            if not line:
                continue

            decoded = base64.b64decode(line).decode("utf-8")
            parts = decoded.split("|")
            title = parts[0]
            x = float(parts[1])
            y = float(parts[2])
            travel_time = int(parts[3])

            s = Stop(title, Position(x, y), travel_time)
            node = ListNode(s)

            if not self.start:
                self.start = self.end = node
            else:
                node.prv = self.end
                self.end.nxt = node
                self.end = node

            self.count += 1

        print(f"  Маршрут загружен из файла: {filename} ({self.count} остановок)")


if __name__ == "__main__":

    route = RouteList()

    route.add_stop(Stop("Вокзал", Position(0, 0)))
    route.add_stop(Stop("Центр", Position(10, 0)))
    route.add_stop(Stop("Парк", Position(20, 0)))
    route.add_stop(Stop("Школа", Position(30, 0)))
    route.add_stop(Stop("Больница", Position(40, 0)))
    route.add_stop(Stop("Рынок", Position(3, 2)))
    route.add_stop(Stop("Библиотека", Position(12, 3)))
    route.add_stop(Stop("Памятник", Position(30, 5)))

    route.show()

    print("Где будет автобус через 3 остановки от Вокзала?")
    print()
    depart = datetime(2025, 1, 1, 8, 0)
    route.find_stop_after_n("Вокзал", n=3, depart_time=depart)

    print()
    print("Через 5 остановок от Рынка (без времени отправления):")
    print()
    route.find_stop_after_n("Рынок", n=5)

    print("\n" + "─" * 55)
    print("Разворачиваем маршрут:")
    print()
    route.reverse()
    route.show()

    print("\n" + "─" * 55)
    print("Сохраняем маршрут в файл (Base64):")
    print()
    route.save_to_file("route.txt")

    print("\n" + "─" * 55)
    print("Загружаем маршрут обратно из файла:")
    print()
    route2 = RouteList()
    route2.load_from_file("route.txt")
    route2.show()
