# Лабораторная работа №4
Косенок Иван БСТ2201

## Задание 1
Реализовать методы поиска в соответствии с заданием.
Организовать генерацию начального набора случайных данных.
Для всех вариантов добавить реализацию добавления, поиска и удаления элементов
Оценить время работы каждого алгоритма поиска и сравнить его со временем работы стандартной функции поиска

| Метод поиска           | 100000 | 400000 | 2000000 |
|------------------------|--------|--------|---------|
| Бинарный поиск         | 0 ms   | 0 ms   | 0 ms    |
| Бинарное дерево        | 0 ms   | 1 ms   | 0 ms    |
| Поиск Фибоначчи        | 0 ms   | 152 ms | 447 ms  |
| Интерполяционный поиск | 0 ms   | 0 ms   | 0 ms    |
| Стандартная функция    | 4 ms   | 58 ms  | 224 ms  |

## Задание 2

| Метод рехеширования | 100 | 400 | 2000 | 4000 |
| ------------------- | --- | --- | ---- | ---- |
| Простое рехеширование | 0 ms | 4 ms | 115 ms | 475 ms |
| Рехеширование ГСЧ | 2 ms | 22 ms | 599 ms | 2705 ms |
| Метод цепочек | 0 ms | 1 ms | 1 ms | 2 ms |

## Задание 3
Расставить на стандартной 64-клеточной шахматной доске
8 ферзей так, чтобы ни один из них не находился под боем другого.

Решение задачи, предложенное программой:

**A1 B5 C8 D6 E3 F7 G2 H4**
