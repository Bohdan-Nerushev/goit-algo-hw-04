def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as fh:
            lines = [el.strip() for el in fh.readlines()]
            count = 0
            total = 0
            average = 0
            for i in range(len(lines)):
                lines[i] = int(lines[i].split(',')[1])
                count += 1
                total += lines[i]
                average = int(total/count)
            return (f"Загальна сума {total}, Середня заробітна плата: {average}")
    except FileNotFoundError:
        return('Файл не знайдено!')
    except IndentationError:
        return('Помилка відступу!')
    except SyntaxWarning:
        return('Синтаксична помилка!')

# C:/Users/Lenovo/Desktop/qwert.txt
path = input()  # Provide the full path here
print(total_salary(path))
