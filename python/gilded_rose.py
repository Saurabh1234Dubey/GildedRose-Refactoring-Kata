# -*- coding: utf-8 -*-

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return f"{self.name}, {self.sell_in}, {self.quality}"


class GildedRose:
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == "Sulfuras, Hand of Ragnaros":
                continue  # Legendary item, no change

            self._update_sell_in(item)

            if item.name == "Aged Brie":
                self._update_aged_brie(item)
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                self._update_backstage_passes(item)
            elif item.name.lower().startswith("conjured"):
                self._update_conjured_item(item)
            else:
                self._update_standard_item(item)

    def _update_sell_in(self, item):
        item.sell_in -= 1

    def _increase_quality(self, item, amount=1):
        item.quality = min(50, item.quality + amount)

    def _decrease_quality(self, item, amount=1):
        item.quality = max(0, item.quality - amount)

    def _update_aged_brie(self, item):
        self._increase_quality(item, 2 if item.sell_in < 0 else 1)

    def _update_backstage_passes(self, item):
        if item.sell_in < 0:
            item.quality = 0
        elif item.sell_in < 5:
            self._increase_quality(item, 3)
        elif item.sell_in < 10:
            self._increase_quality(item, 2)
        else:
            self._increase_quality(item, 1)

    def _update_conjured_item(self, item):
        degradation = 4 if item.sell_in < 0 else 2
        self._decrease_quality(item, degradation)

    def _update_standard_item(self, item):
        degradation = 2 if item.sell_in < 0 else 1
        self._decrease_quality(item, degradation)
