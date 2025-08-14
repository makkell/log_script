Небольшая демонстрация кода

## Запуск с одним отчетом
```
python main.py --files "example1.log" --report "average" 
```
Вывод в консоли: 

<img width="655" height="397" alt="image" src="https://github.com/user-attachments/assets/4bf3b923-429a-4bc2-8d54-a5288776f048" />


## Передача нескольких отчетов

```
python main.py --files "example1.log example2.log " --report "average" 
```
Вывод в консоли:

<img width="691" height="395" alt="image" src="https://github.com/user-attachments/assets/dcd32173-e5cb-4a3f-a914-4410862198a6" />

## Выбор неверного отчета 

```
python main.py --files "example1.log example2.log " --report "sum" 
```
Вывод в консоли:
<img width="935" height="41" alt="image" src="https://github.com/user-attachments/assets/fe3895f1-8f22-458a-9a01-75144420822f" />

## Фильтрация по датам 
### Формат даты
Дата пердается в следующем формате: dd.mm либо промежуток dd.mm-dd.mm

### Фильтрация по одному дню

```
python main.py --files "example1.log example2.log" --date "22.06" --report "average"
```
Вывод в консоли:

<img width="617" height="407" alt="image" src="https://github.com/user-attachments/assets/ccea67a6-67b1-4bb9-9c81-a9778e5f01a7" />


### Фильтрация по промежутку

```
python main.py --files "example1.log example2.log" --date "22.06-25.06" --report "average"
```

Вывод в консоли:

<img width="628" height="397" alt="image" src="https://github.com/user-attachments/assets/807d38fa-e8d5-48ce-a094-eb71133333f3" />

