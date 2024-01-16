

# Напишіть функцію, яка відображає порожній або заповнений
# квадрат із певним символом.
# Функція приймає в якості параметрів довжину сторони квадрата,
# символ та змінну логічного типу:
# - якщо вона дорівнює True, квадрат заповнений;
# - якщо False, квадрат порожній.

# Вхідні параметри (можна замінити input()-функцією)
symbol = '#' # задаємо символ яким буде намальований квадрат
length = 10 # задаємо протяжність його сторони
filled = False # True # задаємо логічну змінну

def draw(symbol, length, filled): # оголошуємо функцію яка буде приймати три параметри
    # якщо змінна filled дорівнює True
    # це означає що ми хочемо заповнений квадрат
    if filled == True:
        # тут все просто - малюємо його двома вкладеними циклами
        # я демонстрував подбне на занятті
        for i in range(0, length): # цикл для кожн. строки у квадраті
            for t in range(0, length): # цикл для кожн. символу у строці
                print(symbol, end='  ') # малюємо символ та параметр end замінюємо на пробіл замість переводу строки
            print() # прінт для переводу строки
    elif filled == False:
        # якщо квадрат хочемо незаповнений
        # намалюємо частинами
        k = str(symbol + '  ') # сформуємо строку для верхньої і нижньої сторони
        print(k * length) # малюємо верх
        for i in range(0, length - 2): # цикл для середини квадрату
            print(symbol, ' ' * (length + 2 * (length - 1) - 4), symbol) # формуємо середні строки
            # формула трохи складна, але тільки так ми намалюєио нормальний квадрат
        print(k * length) # малюємо низ

draw(symbol, length, filled) # викликаємо функцію та передаємо у неї параметри
# подумайте і оптимізуйте функцію
#

