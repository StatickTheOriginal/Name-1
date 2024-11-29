# Протокол обмена данными с контроллером

Данное описание содержит информацию для работы с контроллером шлифовального станка.
Версия протокол: 1.0

Обмен данных с контроллером осуществляется по COM-порту.

## Команды

При получении ожидаемого ответа или ошибки, контроллер в конце сообщения ставит знак "!", который служит для обозначения конца передачи сообщения.


Параметризованные команды передаются в виде:
```
<команда>.<параметр>
```

Пример:
```
move.7777
```


### Управление питанием

#### Проверка активности

Данная команда служит для проверки активности контроллера после подключения к COM порту

<table>
    <tbody>
        <tr>
            <td>Команда</td>
            <td>set_idle</td>
        </tr>
        <tr>
            <td>Ожидаемый ответ</td>
            <td>idle</td>
        </tr>
        <tr>
            <td>Ожидаемая ошибка</td>
            <td>i cant stop!!</td>
        </tr>
        <tr>
            <td>Максимальное время ожидания</td>
            <td>1000</td>
        </tr>
        <tr>
            <td>Пример</td>
            <td>1000</td>
        </tr>
    </tbody>
</table>

#### Включить питание

<table>
    <tbody>
        <tr>
            <td>Команда</td>
            <td>switch_on</td>
        </tr>
        <tr>
            <td>Ожидаемый ответ</td>
            <td>on</td>
        </tr>
        <tr>
            <td>Ожидаемая ошибка</td>
            <td>Power fault</td>
        </tr>
        <tr>
            <td>Максимальное время ожидания</td>
            <td>15000</td>
        </tr>
    </tbody>
</table>


#### Выключение питания
<table>
    <tbody>
        <tr>
            <td>Команда</td>
            <td>set_idle</td>
        </tr>
        <tr>
            <td>Ожидаемый ответ</td>
            <td>idle</td>
        </tr>
        <tr>
            <td>Ожидаемая ошибка</td>
            <td>i cant stop!!</td>
        </tr>
        <tr>
            <td>Максимальное время ожидания</td>
            <td>1000</td>
        </tr>
    </tbody>
</table>


### Управление подачей

#### Подача материала

В качестве параметра принимает количество шагов двигателя на мм

<table>
    <tbody>
        <tr>
            <td>Команда</td>
            <td>move</td>
        </tr>
        <tr>
            <td>Тип параметра</td>
            <td>Целочисленный</td>
        </tr>
        <tr>
            <td>Ожидаемый ответ</td>
            <td>moved</td>
        </tr>
        <tr>
            <td>Ожидаемая ошибка</td>
            <td>Move Crush</td>
        </tr>
        <tr>
            <td>Максимальное время ожидания</td>
            <td>30000</td>
        </tr>
    </tbody>
</table>

#### Подача материала (быстрая)

В качестве параметра принимает количество шагов двигателя на мм

<table>
    <tbody>
        <tr>
            <td>Команда</td>
            <td>fastmove</td>
        </tr>
        <tr>
            <td>Тип параметра</td>
            <td>Целочисленный</td>
        </tr>
        <tr>
            <td>Ожидаемый ответ</td>
            <td>moved</td>
        </tr>
        <tr>
            <td>Ожидаемая ошибка</td>
            <td>Move Crush</td>
        </tr>
        <tr>
            <td>Максимальное время ожидания</td>
            <td>30000</td>
        </tr>
    </tbody>
</table>

#### Обнуление положения
<table>
    <tbody>
        <tr>
            <td>Команда</td>
            <td>set_zero_point</td>
        </tr>
        <tr>
            <td>Ожидаемый ответ</td>
            <td>zero_point</td>
        </tr>
        <tr>
            <td>Ожидаемая ошибка</td>
            <td>not_zero</td>
        </tr>
        <tr>
            <td>Максимальное время ожидания</td>
            <td>5000</td>
        </tr>
    </tbody>
</table>

#### Сброс значений

<table>
    <tbody>
        <tr>
            <td>Команда</td>
            <td>sethome</td>
        </tr>
        <tr>
            <td>Тип параметра</td>
            <td>Целочисленный</td>
        </tr>
        <tr>
            <td>Ожидаемый ответ</td>
            <td>sethome</td>
        </tr>
        <tr>
            <td>Ожидаемая ошибка</td>
            <td>Error Set Home</td>
        </tr>
        <tr>
            <td>Максимальное время ожидания</td>
            <td>25000</td>
        </tr>
    </tbody>
</table>

#### Остановка подачи

<table>
    <tbody>
        <tr>
            <td>Команда</td>
            <td>stop_feed</td>
        </tr>
        <tr>
            <td>Ожидаемый ответ</td>
            <td>stop_feed</td>
        </tr>
        <tr>
            <td>Ожидаемая ошибка</td>
            <td>dont stop me now!</td>
        </tr>
        <tr>
            <td>Максимальное время ожидания</td>
            <td>1000</td>
        </tr>
    </tbody>
</table>

### Управление производством

#### Использовать инструмент

Данная команда позволяет использовать инструмент который передаётся через параметр

<table>
    <tbody>
        <tr>
            <td>Команда</td>
            <td>use_tool</td>
        </tr>
        <tr>
            <td>Ожидаемый ответ</td>
            <td>pushed</td>
        </tr>
        <tr>
            <td>Тип параметра</td>
            <td>Целочисленный</td>
        </tr>
        <tr>
            <td>Ожидаемая ошибка</td>
            <td>Tool press</td>
        </tr>
        <tr>
            <td>Максимальное время ожидания</td>
            <td>5000</td>
        </tr>
    </tbody>
</table>
