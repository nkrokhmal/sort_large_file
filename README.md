# Сортировка строк в больших файлах.

Для решения задачи я использовал следующий подход. 

Делим файл на k маленьких файликов и применяем для них сортировку.

Затем берем k отсортированных маленьких файлов, выбираем из них первые элементы, создаем кучу и по сути применяем HeapSort. 
Чтобы протестировать локально - требуется запустить команду 

  ```
    python3 main.py --mem 1g --row 1000 --length 200 --newdata True
  ```
  
  
