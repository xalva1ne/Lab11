class Teacher:
    # Статическое свойство - общее количество учителей
    teachers = 0

    def __init__(self, name, subject, experience):
        # Публичные свойства
        self.name = name
        self.subject = subject
        self.experience = experience

        # Приватное свойство
        self.__salary = 0

        # Увеличиваем общее количество учителей при создании нового объекта
        Teacher.teachers += 1

    def set_salary(self, salary):
        # Метод для установки приватного свойства
        self.__salary = salary

    def get_salary(self):
        # Метод для получения приватного свойства
        return self.__salary

    def info(self):
        # Метод для отображения информации об учителе
        print(f"Имя: {self.name}, Предмет: {self.subject}, Стаж: {self.experience} лет, "
              f"Зарплата: {self.get_salary()}")

    @staticmethod
    def total_teachers():
        # Статический метод для отображения общего количества учителей
        print(f"Общее количество учителей: {Teacher.teachers}")


# Создаем несколько объектов класса Teacher
teacher1 = Teacher("Иванов", "Математика", 10)
teacher2 = Teacher("Петрова", "Физика", 5)


# Устанавливаем зарплату для учителей
teacher1.set_salary(50000)
teacher2.set_salary(45000)


# Выводим информацию о каждом учителе
teacher1.info()
teacher2.info()


# Выводим общее количество учителей
Teacher.total_teachers()
