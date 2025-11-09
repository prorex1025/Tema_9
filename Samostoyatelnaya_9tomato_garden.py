"""
Лабораторная работа 9 - Задание 5
Полиморфизм: приветствия на разных языках
"""

class RussianGreeting:
    """
    Класс для приветствия на русском языке
    """

    # Статическое свойство - не требует создания экземпляра
    greeting_word = "Привет"

    @staticmethod
    def greet():
        """
        Статический метод для приветствия на русском
        Не требует параметра self
        """
        return f"{RussianGreeting.greeting_word}! Как дела?"

    @staticmethod
    def get_language_info():
        """Информация о языке"""
        return "Русский язык - славянская языковая группа"


class EnglishGreeting:
    """
    Класс для приветствия на английском языке
    """

    greeting_word = "Hello"

    @staticmethod
    def greet():
        """
        Статический метод для приветствия на английском
        """
        return f"{EnglishGreeting.greeting_word}! How are you?"

    @staticmethod
    def get_language_info():
        """Информация о языке"""
        return "English - Germanic language group"


class FrenchGreeting:
    """
    Класс для приветствия на французском языке
    Дополнительный класс для демонстрации полиморфизма
    """

    greeting_word = "Bonjour"

    @staticmethod
    def greet():
        """Приветствие на французском"""
        return f"{FrenchGreeting.greeting_word}! Comment ça va?"

    @staticmethod
    def get_language_info():
        """Информация о языке"""
        return "Français - Romance language group"


class JapaneseGreeting:
    """
    Класс для приветствия на японском языке
    """

    greeting_word = "こんにちは"  # Konnichiwa

    @staticmethod
    def greet():
        """Приветствие на японском"""
        return f"{JapaneseGreeting.greeting_word}! お元気ですか？"  # Ogenki desu ka?

    @staticmethod
    def get_language_info():
        """Информация о языке"""
        return "日本語 - Japonic language family"


def demonstrate_greeting(greeting_class):
    """
    Универсальная функция для демонстрации приветствия
    Демонстрация полиморфизма - работает с любым классом приветствия

    Args:
        greeting_class: класс с методами greet() и get_language_info()
    """
    print(f"🌍 Язык: {greeting_class.get_language_info()}")
    print(f"🗣️ Приветствие: {greeting_class.greet()}")
    print(f"📝 Слово: '{greeting_class.greeting_word}'")
    print("-" * 50)


def multicultural_meeting(greeting_classes):
    """
    Функция для мультикультурной встречи
    Полиморфизм позволяет обрабатывать разные классы одинаково

    Args:
        greeting_classes: список классов приветствий
    """
    print("\n🎉 МУЛЬТИКУЛЬТУРНАЯ ВСТРЕЧА")
    print("=" * 50)

    for i, greeting_class in enumerate(greeting_classes, 1):
        print(f"\nУчастник {i}:")
        demonstrate_greeting(greeting_class)


def test_polymorphism():
    """Тестирование полиморфизма"""
    print("=== ДЕМОНСТРАЦИЯ ПОЛИМОРФИЗМА ===")

    # Список классов приветствий
    greeting_classes = [
        RussianGreeting,
        EnglishGreeting,
        FrenchGreeting,
        JapaneseGreeting
    ]

    # Индивидуальные приветствия
    print("1. ИНДИВИДУАЛЬНЫЕ ПРИВЕТСТВИЯ:")
    for greeting_class in greeting_classes:
        demonstrate_greeting(greeting_class)

    # Мультикультурная встреча
    multicultural_meeting(greeting_classes)

    # Демонстрация полиморфного поведения
    print("\n2. ПОЛИМОРФНОЕ ПОВЕДЕНИЕ:")
    print("Все классы имеют одинаковый интерфейс:")

    required_methods = ['greet', 'get_language_info']
    for greeting_class in greeting_classes:
        class_name = greeting_class.__name__
        has_methods = all(hasattr(greeting_class, method) for method in required_methods)
        status = "✅" if has_methods else "❌"
        print(f"   {status} {class_name}: {has_methods}")

    print(f"\nОбъяснение:")
    print("ПОЛИМОРФИЗМ позволяет использовать разные классы