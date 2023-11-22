# StatusTermoFurnace
## Статус электропечей

Бэкенд часть сервиса по получению данных по проктоколу modbus.
Отображение статуса электропечей закалки, текущее время работы, температуру.

### Используемые библиотeки:
>pyserial==3.5  
>Flask==3.0.0  


Для тестирования была добавлена возможность симуляции
получаемых данных от электропечи.
В файле /server/app.py: 
```python
data_dict = get_data_from_sp(test=True)
```
>test=True - симуляция включена
>test=False - симуляция выключена

Демо версия с выводом в html файл.
http://45.132.1.65:5333/



# StatusTermoFurnace
## Status of Heat Treatment Furnaces

This is the backend component of a service designed to retrieve data using the Modbus protocol. 
It provides information on the status of tempering electric furnaces, current operating time, and temperature.

### Used Libraries:
>pyserial==3.5  
>Flask==3.0.0  

### Testing and Simulation:
For testing purposes, a data simulation feature has been implemented. In the file `/server/app.py`:

```python
data_dict = get_data_from_sp(test=True)
```
>test=True enables simulation mode.
>test=False disables simulation mode.


Demo version with output to an html file.
http://45.132.1.65:5333/
