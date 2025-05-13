# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

    def test_standard_item_before_sell_date(self):
        items = [Item("Normal Item", 10, 20)]
        GildedRose(items).update_quality()
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(19, items[0].quality)

    def test_standard_item_after_sell_date(self):
        items = [Item("Normal Item", 0, 20)]
        GildedRose(items).update_quality()
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(18, items[0].quality)

    def test_standard_item_quality_never_negative(self):
        items = [Item("Normal Item", 5, 0)]
        GildedRose(items).update_quality()
        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(0, items[0].quality)

    def test_aged_brie_before_sell_date(self):
        items = [Item("Aged Brie", 2, 0)]
        GildedRose(items).update_quality()
        self.assertEqual(1, items[0].sell_in)
        self.assertEqual(1, items[0].quality)

    def test_aged_brie_after_sell_date(self):
        items = [Item("Aged Brie", -1, 0)]
        GildedRose(items).update_quality()
        self.assertEqual(-2, items[0].sell_in)
        self.assertEqual(2, items[0].quality)

    def test_aged_brie_quality_never_above_50(self):
        items = [Item("Aged Brie", 5, 50)]
        GildedRose(items).update_quality()
        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(50, items[0].quality)

    def test_sulfuras_never_changes(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 0, 80)]
        GildedRose(items).update_quality()
        self.assertEqual(0, items[0].sell_in)
        self.assertEqual(80, items[0].quality)

    def test_backstage_pass_long_before_concert(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 15, 20)]
        GildedRose(items).update_quality()
        self.assertEqual(14, items[0].sell_in)
        self.assertEqual(21, items[0].quality)

    def test_backstage_pass_close_to_concert_10_days(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 25)]
        GildedRose(items).update_quality()
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(27, items[0].quality)

    def test_backstage_pass_close_to_concert_5_days(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 45)]
        GildedRose(items).update_quality()
        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(48, items[0].quality)

    def test_backstage_pass_after_concert(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 40)]
        GildedRose(items).update_quality()
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(0, items[0].quality)

    def test_conjured_item_before_sell_date(self):
        items = [Item("Conjured Mana Cake", 3, 6)]
        GildedRose(items).update_quality()
        self.assertEqual(2, items[0].sell_in)
        self.assertEqual(4, items[0].quality)

    def test_conjured_item_after_sell_date(self):
        items = [Item("Conjured Mana Cake", 0, 6)]
        GildedRose(items).update_quality()
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(2, items[0].quality)

    def test_conjured_item_quality_never_negative(self):
        items = [Item("Conjured Mana Cake", 0, 1)]
        GildedRose(items).update_quality()
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(0, items[0].quality)


if __name__ == '__main__':
    unittest.main()


        
if __name__ == '__main__':
    unittest.main()
