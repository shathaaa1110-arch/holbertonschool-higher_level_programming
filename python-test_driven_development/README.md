# Python Test-Driven Development — التطوير المدفوع بالاختبارات

## ما هو TDD؟

**Test-Driven Development** هو أسلوب برمجي يقوم على مبدأ بسيط:

```
اكتب الاختبار أولاً  →  شاهد الفشل  →  اكتب الكود  →  شاهد النجاح  →  أعد التحسين
```

بمعنى آخر: قبل أن تكتب كود الحل، تكتب اختباراً يحدد ما يُفترض أن يفعله الكود. هذا يضمن:
- أن كل جزء من الكود له غرض محدد
- أن التغييرات المستقبلية لن تكسر ما يعمل
- أن الكود موثق بأمثلة حقيقية

### نوعا الاختبار في هذا المشروع

| النوع | الأداة | الملف | الهدف |
|-------|--------|-------|-------|
| **Doctest** | `python3 -m doctest` | ملف `.txt` | أمثلة تفاعلية داخل التوثيق |
| **Unittest** | `python3 -m unittest` | ملف `.py` | اختبارات منظمة بصفوف وأساليب |

---

## هيكل المشروع

```
python-test_driven_development/
├── 0-add_integer.py
├── 2-matrix_divided.py
├── 3-say_my_name.py
├── 4-print_square.py
├── 5-text_indentation.py
├── 6-max_integer.py
├── 100-matrix_mul.py
├── 101-lazy_matrix_mul.py
└── tests/
    ├── 0-add_integer.txt
    ├── 2-matrix_divided.txt
    ├── 3-say_my_name.txt
    ├── 4-print_square.txt
    ├── 5-text_indentation.txt
    ├── 100-matrix_mul.txt
    ├── 101-lazy_matrix_mul.txt
    └── 6-max_integer_test.py
```

---

## المهام

---

### المهمة 0: جمع عددين صحيحين
**الملف:** `0-add_integer.py` | **الاختبار:** `tests/0-add_integer.txt`

#### المفهوم البرمجي
التحقق من نوع المدخلات قبل إجراء العملية. Python مرنة في الأنواع، لذا نحتاج التحقق يدوياً. الأعداد العشرية مسموحة لكن تُحوَّل إلى أعداد صحيحة.

#### الكود

```python
#!/usr/bin/python3
"""Module for adding two integers."""


def add_integer(a, b=98):
    """Add two integers or floats (cast to int).

    Raises TypeError if a or b is not int/float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
```

#### الشرح خطوة بخطوة
1. نتحقق من `a` أولاً — إذا لم يكن `int` أو `float` نرفع `TypeError`
2. نتحقق من `b` — نفس الشرط
3. نحوّل كليهما إلى `int` قبل الجمع (هذا يتعامل مع الأعداد العشرية مثل `100.3 → 100`)
4. القيمة الافتراضية لـ `b` هي `98`

#### أمثلة

```
add_integer(1, 2)        → 3
add_integer(100, -2)     → 98
add_integer(2)           → 100     ← b=98 افتراضياً
add_integer(100.3, -2)   → 98      ← 100.3 تصبح 100
add_integer(4, "School") → TypeError: b must be an integer
add_integer(None)        → TypeError: a must be an integer
```

#### تشغيل الاختبارات

```bash
python3 -m doctest -v tests/0-add_integer.txt
```

---

### المهمة 1: قسمة مصفوفة
**الملف:** `2-matrix_divided.py` | **الاختبار:** `tests/2-matrix_divided.txt`

#### المفهوم البرمجي
دالة تُطبّق عملية على هيكل بيانات متداخل (قائمة من قوائم). نحتاج التحقق من ثلاثة أشياء: نوع المصفوفة، تساوي أطوال الصفوف، ونوع المقسوم عليه.

#### الكود

```python
#!/usr/bin/python3
"""Module for dividing all elements of a matrix."""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix by div, rounded to 2 decimals."""
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or not all(
            isinstance(row, list) for row in matrix):
        raise TypeError(msg)
    for row in matrix:
        for el in row:
            if not isinstance(el, (int, float)):
                raise TypeError(msg)
    row_len = len(matrix[0])
    if not all(len(row) == row_len for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(el / div, 2) for el in row] for row in matrix]
```

#### الشرح
- نتحقق أن `matrix` قائمة من قوائم تحتوي أرقاماً فقط
- نتحقق أن جميع الصفوف لها نفس الطول
- نتحقق أن `div` رقم وليس صفراً
- نستخدم list comprehension متداخلة لتطبيق القسمة على كل عنصر
- `round(el / div, 2)` تقريب إلى منزلتين عشريتين

#### أمثلة

```python
matrix = [[1, 2, 3], [4, 5, 6]]
matrix_divided(matrix, 3)
→ [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
# المصفوفة الأصلية لم تتغير (نُعيد مصفوفة جديدة)
```

#### قواعد الأخطاء

| الحالة | الخطأ |
|--------|-------|
| المصفوفة ليست قائمة قوائم | `TypeError: matrix must be a matrix...` |
| صفوف بأطوال مختلفة | `TypeError: Each row of the matrix must have the same size` |
| `div` ليس رقماً | `TypeError: div must be a number` |
| `div == 0` | `ZeroDivisionError: division by zero` |

---

### المهمة 2: قل اسمي
**الملف:** `3-say_my_name.py` | **الاختبار:** `tests/3-say_my_name.txt`

#### المفهوم البرمجي
دالة بسيطة تُعلّمنا أهمية التحقق من نوع المدخلات حتى في أبسط الحالات، وكيفية استخدام معاملات افتراضية.

#### الكود

```python
#!/usr/bin/python3
"""Module for printing a name."""


def say_my_name(first_name, last_name=""):
    """Print 'My name is <first_name> <last_name>'."""
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
```

#### أمثلة

```
say_my_name("John", "Smith")  → My name is John Smith
say_my_name("Walter", "White") → My name is Walter White
say_my_name("Bob")             → My name is Bob      ← last_name فارغ افتراضياً
say_my_name(12, "White")       → TypeError: first_name must be a string
```

---

### المهمة 3: طباعة مربع
**الملف:** `4-print_square.py` | **الاختبار:** `tests/4-print_square.txt`

#### المفهوم البرمجي
نتعلم هنا الفرق بين `TypeError` و`ValueError`، وكيفية معالجة حالة خاصة: عدد عشري سالب يجب أن يُطلق `TypeError` لا `ValueError`.

#### الكود

```python
#!/usr/bin/python3
"""Module for printing a square of # characters."""


def print_square(size):
    """Print a square of # characters with side length 'size'."""
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
```

#### لماذا نتحقق من `float` أولاً؟
لأن `isinstance(-1.5, int)` يُعيد `False`، وسنُطلق `TypeError` بدلاً من الرسالة الصحيحة. بالتحقق من `float` السالب أولاً نضمن الرسالة الصحيحة.

#### أمثلة

```
print_square(4)   →  ####        print_square(0)  →  (لا شيء)
                     ####
                     ####
                     ####

print_square(-1)  → ValueError: size must be >= 0
print_square("4") → TypeError: size must be an integer
print_square(-1.5)→ TypeError: size must be an integer
```

---

### المهمة 4: مسافة بادئة للنص
**الملف:** `5-text_indentation.py` | **الاختبار:** `tests/5-text_indentation.txt`

#### المفهوم البرمجي
معالجة النصوص حرفاً حرفاً. بعد كل `.` أو `?` أو `:` نطبع سطرين فارغين، ونتخطى المسافات التي قد تأتي بعد هذه الرموز.

#### الكود

```python
#!/usr/bin/python3
"""Module for text indentation after . ? : characters."""


def text_indentation(text):
    """Print text with 2 newlines after each '.', '?', or ':'."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in ".?:":
            print("\n")
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1
```

#### الشرح
- نطبع كل حرف بـ `end=""` (بدون سطر جديد تلقائي)
- عند مواجهة `.?:` نطبع `"\n"` (سطر جديد + سطر فارغ = سطران)
- نتخطى المسافات التالية مباشرة لتجنب أسطر فارغة في البداية

#### مثال

```
النص: "Hello. How are you? Fine: thanks"
الناتج:
Hello.

How are you?

Fine:

thanks
```

---

### المهمة 5: أكبر عدد صحيح — Unittest
**الملف:** `6-max_integer.py` | **الاختبار:** `tests/6-max_integer_test.py`

#### المفهوم البرمجي
هذه المهمة مختلفة — الكود **موجود مسبقاً**، ومهمتنا كتابة اختبارات شاملة له باستخدام `unittest`. الهدف: تغطية جميع الحالات الممكنة.

#### الدالة الموجودة

```python
def max_integer(list=[]):
    """Find and return the max integer in a list. Returns None if empty."""
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result
```

#### ملف الاختبارات

```python
#!/usr/bin/python3
"""Unittest for max_integer([..])"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_regular_list(self):
        """Max at the end."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_at_beginning(self):
        """Max at the start."""
        self.assertEqual(max_integer([9, 3, 4, 2]), 9)

    def test_max_in_middle(self):
        """Max in the middle."""
        self.assertEqual(max_integer([1, 7, 3, 2]), 7)

    def test_one_element(self):
        """Single element list."""
        self.assertEqual(max_integer([5]), 5)

    def test_empty_list(self):
        """Empty list returns None."""
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        """All negative numbers."""
        self.assertEqual(max_integer([-1, -5, -3]), -1)

    def test_mixed_negative_positive(self):
        """Mix of negative and positive."""
        self.assertEqual(max_integer([-1, 0, 5, -10]), 5)

    def test_equal_elements(self):
        """All elements equal."""
        self.assertEqual(max_integer([3, 3, 3]), 3)

    def test_floats(self):
        """Floating point numbers."""
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)

    def test_no_argument(self):
        """No argument — uses default empty list."""
        self.assertIsNone(max_integer())
```

#### تشغيل الاختبارات

```bash
python3 -m unittest tests.6-max_integer_test
```

#### حالات الاختبار المُغطاة

| الاختبار | الهدف |
|---------|-------|
| الأكبر في النهاية | الحالة المعتادة |
| الأكبر في البداية | ألا يفترض الكود أن الأكبر في نهاية القائمة |
| الأكبر في المنتصف | اختبار المسح الكامل |
| عنصر واحد | حالة حدية |
| قائمة فارغة | يجب إعادة `None` |
| أرقام سالبة | الأكبر هو الأقل سالبية |
| خليط سالب وموجب | |
| عناصر متساوية | |
| أعداد عشرية | |
| بدون معامل | |

---

### المهمة 6 (متقدمة): ضرب مصفوفتين
**الملف:** `100-matrix_mul.py` | **الاختبار:** `tests/100-matrix_mul.txt`

#### المفهوم البرمجي
ضرب المصفوفات رياضياً: عنصر `result[i][j]` هو حاصل ضرب الصف `i` من `m_a` في العمود `j` من `m_b`.

**شرط الضرب:** عدد أعمدة `m_a` = عدد صفوف `m_b`

```
m_a (2×3) × m_b (3×2) = نتيجة (2×2)
```

#### الكود

```python
#!/usr/bin/python3
"""Module for matrix multiplication without NumPy."""


def matrix_mul(m_a, m_b):
    """Multiply two matrices m_a and m_b."""
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    for row in m_a:
        for el in row:
            if not isinstance(el, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for el in row:
            if not isinstance(el, (int, float)):
                raise TypeError("m_b should contain only integers or floats")
    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    result = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            val = sum(m_a[i][k] * m_b[k][j] for k in range(len(m_b)))
            row.append(val)
        result.append(row)
    return result
```

#### الشرح الرياضي

```
[[1, 2],   ×   [[1, 2],   =   [[1×1+2×3, 1×2+2×4],   =   [[7,  10],
 [3, 4]]        [3, 4]]        [3×1+4×3, 3×2+4×4]]        [15, 22]]
```

#### قواعد الأخطاء (مرتبة)

| الترتيب | الفحص | الخطأ |
|---------|-------|-------|
| 1 | هل هي قائمة؟ | `TypeError: m_a must be a list` |
| 2 | هل هي قائمة قوائم؟ | `TypeError: m_a must be a list of lists` |
| 3 | هل فارغة؟ | `ValueError: m_a can't be empty` |
| 4 | هل تحتوي أرقاماً فقط؟ | `TypeError: m_a should contain only integers or floats` |
| 5 | هل الصفوف متساوية الطول؟ | `TypeError: each row of m_a must be of the same size` |
| 6 | هل الأبعاد متوافقة للضرب؟ | `ValueError: m_a and m_b can't be multiplied` |

---

### المهمة 7 (متقدمة): ضرب مصفوفتين بـ NumPy
**الملف:** `101-lazy_matrix_mul.py` | **الاختبار:** `tests/101-lazy_matrix_mul.txt`

#### المفهوم البرمجي
نفس المهمة السابقة لكن باستخدام مكتبة **NumPy** — المكتبة العلمية الأشهر في Python. تتعامل NumPy مع كل التحقق والحساب بكفاءة عالية.

#### الكود

```python
#!/usr/bin/python3
"""Module for matrix multiplication using NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiply two matrices using NumPy's matmul."""
    return np.matmul(m_a, m_b)
```

#### لماذا "lazy"؟
لأن NumPy تتولى كل شيء — لا نكتب منطق التحقق أو الحساب يدوياً. `np.matmul` تُطلق أخطاءها الخاصة تلقائياً.

#### مقارنة النتائج

```python
# matrix_mul (يدوي)        # lazy_matrix_mul (NumPy)
[[7, 10], [15, 22]]        array([[ 7, 10],
                                  [15, 22]])
```

NumPy تُعيد `ndarray` بدلاً من قائمة Python عادية.

#### التثبيت

```bash
pip3 install numpy==1.15.0
```

---

## ملخص أوامر الاختبار

```bash
# تشغيل doctest لملف محدد
python3 -m doctest tests/0-add_integer.txt
python3 -m doctest -v tests/0-add_integer.txt   # مع تفاصيل

# تشغيل unittest
python3 -m unittest tests.6-max_integer_test
python3 -m unittest tests.6-max_integer_test -v  # مع تفاصيل
```

## الفرق بين Doctest و Unittest

| | Doctest | Unittest |
|-|---------|----------|
| **الموقع** | ملف `.txt` أو داخل docstring | ملف `.py` مستقل |
| **الأسلوب** | محاكاة جلسة تفاعلية | صف يرث من `TestCase` |
| **الاستخدام** | توثيق + اختبار بسيط | اختبارات معقدة ومنظمة |
| **التحقق** | المقارنة بالناتج المطبوع | دوال مثل `assertEqual`, `assertRaises` |
