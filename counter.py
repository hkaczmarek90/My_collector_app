import math


class MySolution:
    def __init__(self, smallbox, mediumbox, largebox, collectcount):
        self.smallBox = smallbox
        self.mediumBox = mediumbox
        self.largeBox = largebox
        self.collectcount = collectcount

    def without_collect_box(self, quantity):
        if quantity <= self.smallBox:
            result = 'Only 1 small box'
        elif quantity <= self.mediumBox:
            result = 'Only 1 medium box'
        elif quantity <= self.largeBox:
            result = "Only 1 large box"
        return result

    def check_collect_box(self, c):
        return math.ceil(c / self.collectcount)

    def check_box(self, quantity):
        largeboxquan = quantity // self.largeBox
        rest = quantity - (largeboxquan * self.largeBox)
        if rest == 0:
            result = f"{largeboxquan} large box"
        else:
            if rest <= self.smallBox:
                result = f"{largeboxquan} large box and 1 small box"
            elif rest <= self.mediumBox:
                result = f"{largeboxquan} large box and 1 medium box"
            else:
                result = f"{largeboxquan + 1} large box"
        return result + '. This boxes in ' + str(self.check_collect_box(largeboxquan + 1)) + ' collecting box'

    def medium_box(self):
        return "2 medium boxes in 1 collecting box"

    def count(self, quantity):
        quan = quantity / 3
        if quan <= 3:
            result = self.without_collect_box(quantity)
        elif quan <= 4:
            result = self.medium_box()
        elif quan > 4:
            if 4 < quan < 6:
                quantity = 18
            result = self.check_box(quantity)
        return result