from project.hero import Hero

from unittest import TestCase, main


class HeroTests(TestCase):
    def setUp(self) -> None:
        self.hero = Hero("hero", 1, 100, 10)
        self.enemy = Hero("enemy", 1, 100, 10)

    def test_constructor(self):
        self.assertEqual("hero", self.hero.username)
        self.assertEqual(1, self.hero.level)
        self.assertEqual(100, self.hero.health)
        self.assertEqual(10, self.hero.damage)

    def test_battle_between_same_heroes(self):
        self.enemy.username = self.hero.username
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy)
        expected = "You cannot fight yourself"
        self.assertEqual(expected, str(ex.exception))

    def test_battle_if_hero_health_is_less_or_equal_to_zero(self):
        self.hero.health = 0
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)
        expected = "Your health is lower than or equal to 0. You need to rest"
        self.assertEqual(expected, str(ve.exception))

    def test_battle_if_enemy_health_is_less_or_equal_to_zero(self):
        self.enemy.health = 0
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)
        expected = "You cannot fight enemy. He needs to rest"
        self.assertEqual(expected, str(ve.exception))

    def test_battle_is_draw(self):
        self.hero.damage = 100
        self.enemy.damage = 100
        result = self.hero.battle(self.enemy)
        self.assertEqual("Draw", result)

    def test_battle_if_hero_wins(self):
        self.hero.damage = 100
        self.enemy.damage = 10
        result = self.hero.battle(self.enemy)

        self.assertEqual("You win", result)
        self.assertEqual(2, self.hero.level)
        self.assertEqual(95, self.hero.health)
        self.assertEqual(105, self.hero.damage)

    def test_battle_if_hero_looses(self):
        self.hero.damage = 10
        self.enemy.damage = 100
        result = self.hero.battle(self.enemy)

        self.assertEqual("You lose", result)
        self.assertEqual(2, self.enemy.level)
        self.assertEqual(95, self.enemy.health)
        self.assertEqual(105, self.enemy.damage)

    def test_str_representation(self):
        expected = f"Hero hero: 1 lvl\nHealth: 100\nDamage: 10\n"
        self.assertEqual(expected, str(self.hero))


if __name__ == "__main__":
    main()
