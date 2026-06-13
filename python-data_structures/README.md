# Python - Data Structures: Lists and Tuples

This project focuses on understanding and implementing Python's fundamental data structures: lists and tuples. It covers various operations, manipulations, and best practices associated with these data types.

## Learning Objectives

Upon completion of this project, you should be able to explain:

*   What are lists and how to use them.
*   The differences and similarities between strings and lists.
*   The most common methods of lists and how to use them.
*   How to use lists as stacks and queues.
*   What are list comprehensions and how to use them.
*   What are tuples and how to use them.
*   When to use tuples versus lists.
*   What is a sequence.
*   What is tuple packing.
*   What is sequence unpacking.
*   What is the `del` statement and how to use it.

## Tasks Overview

Below is a summary of the tasks covered in this project, along with their respective solutions and explanations.


### 0. Print a list of integers

**المفهوم:** هذه المهمة تقدم مفهوم **القوائم (Lists)** في بايثون وكيفية التكرار عليها لطباعة عناصرها. القائمة هي نوع من هياكل البيانات التي يمكنها تخزين مجموعة من العناصر بترتيب معين. يمكن أن تحتوي القائمة على أنواع بيانات مختلفة، ولكن في هذه المهمة، تقتصر على الأعداد الصحيحة.

**الشرح:** تتطلب هذه المهمة كتابة دالة `print_list_integer` تأخذ قائمة من الأعداد الصحيحة وتطبع كل عدد صحيح في سطر منفصل. يتم استخدام حلقة `for` للتكرار على عناصر القائمة، ويتم طباعة كل عنصر باستخدام `print()` مع تنسيق السلسلة `{:d}` لضمان طباعة الأعداد الصحيحة بشكل صحيح.

**الكود:**
```python
#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for i in my_list:
        print("{:d}".format(i))
```

**مثال على الاستخدام:**
```python
my_list = [1, 2, 3, 4, 5]
print_list_integer(my_list)
```
**الناتج المتوقع:**
```
1
2
3
4
5
```


### 1. Secure access to an element in a list

**المفهوم:** هذه المهمة تركز على كيفية الوصول الآمن إلى عناصر القائمة باستخدام **الفهرسة (Indexing)**، مع معالجة الحالات الخاصة مثل الفهارس السالبة أو التي تتجاوز نطاق القائمة.

**الشرح:** الدالة `element_at` تأخذ قائمة `my_list` وفهرس `idx`. يجب أن تتحقق الدالة مما إذا كان الفهرس صالحًا (ليس سالبًا ولا يتجاوز طول القائمة). إذا كان الفهرس غير صالح، تعيد الدالة `None`. وإلا، فإنها تعيد العنصر الموجود في ذلك الفهرس. هذا يمنع حدوث أخطاء `IndexError` التي تحدث عند محاولة الوصول إلى فهرس غير موجود.

**الكود:**
```python
#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
```

**مثال على الاستخدام:**
```python
my_list = [1, 2, 3, 4, 5]
idx = 3
print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))
```
**الناتج المتوقع:**
```
Element at index 3 is 4
```


### 2. Replace element

**المفهوم:** تتناول هذه المهمة كيفية **تعديل عناصر القائمة (Modifying List Elements)** في بايثون في موقع محدد. القوائم في بايثون قابلة للتغيير (mutable)، مما يعني أنه يمكن تغيير عناصرها بعد إنشائها.

**الشرح:** الدالة `replace_in_list` تأخذ قائمة `my_list`، فهرس `idx`، وعنصر `element` جديد. تتحقق الدالة أولاً من صلاحية الفهرس. إذا كان الفهرس غير صالح (سالب أو خارج النطاق)، تعيد الدالة القائمة الأصلية دون تعديل. إذا كان الفهرس صالحًا، تقوم الدالة بتعيين `element` الجديد في الموضع `idx` داخل `my_list` ثم تعيد القائمة المعدلة.

**الكود:**
```python
#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list
```

**مثال على الاستخدام:**
```python
my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = replace_in_list(my_list, idx, new_element)
print(new_list)
print(my_list)
```
**الناتج المتوقع:**
```
[1, 2, 3, 9, 5]
[1, 2, 3, 9, 5]
```


### 3. Print a list of integers... in reverse!

**المفهوم:** هذه المهمة تستعرض كيفية **التكرار العكسي (Reverse Iteration)** على عناصر القائمة في بايثون. يمكن تحقيق ذلك بعدة طرق، وهنا نستخدم الدالة المدمجة `reversed()`.

**الشرح:** الدالة `print_reversed_list_integer` تأخذ قائمة `my_list` وتطبع عناصرها بترتيب عكسي، كل عدد صحيح في سطر منفصل. يتم استخدام `reversed(my_list)` لإنشاء مكرر (iterator) يعطي عناصر القائمة بدءًا من الأخير إلى الأول. يتم التحقق من أن القائمة ليست فارغة قبل البدء في الطباعة.

**الكود:**
```python
#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
        for i in reversed(my_list):
            print("{:d}".format(i))
```

**مثال على الاستخدام:**
```python
my_list = [1, 2, 3, 4, 5]
print_reversed_list_integer(my_list)
```
**الناتج المتوقع:**
```
5
4
3
2
1
```


### 4. Replace in a copy

**المفهوم:** هذه المهمة تقدم مفهوم **النسخ الضحل (Shallow Copy)** للقوائم في بايثون. عند تعديل قائمة، قد يؤثر ذلك على نسخ أخرى من القائمة إذا لم يتم التعامل معها بشكل صحيح. النسخ الضحل يسمح بتعديل نسخة دون التأثير على الأصل.

**الشرح:** الدالة `new_in_list` تأخذ قائمة `my_list`، فهرس `idx`، وعنصر `element` جديد. الهدف هو استبدال عنصر في القائمة في موضع معين دون تعديل القائمة الأصلية. يتم تحقيق ذلك عن طريق إنشاء نسخة ضحلة من `my_list` باستخدام `my_list[:]`. ثم يتم التحقق من صلاحية الفهرس. إذا كان الفهرس غير صالح، تعيد الدالة النسخة الجديدة (التي هي مطابقة للأصلية). إذا كان الفهرس صالحًا، يتم تعديل العنصر في النسخة الجديدة ثم تعاد النسخة المعدلة.

**الكود:**
```python
#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = my_list[:]
    if idx < 0 or idx >= len(my_list):
        return new_list
    new_list[idx] = element
    return new_list
```

**مثال على الاستخدام:**
```python
my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = new_in_list(my_list, idx, new_element)
print(new_list)
print(my_list)
```
**الناتج المتوقع:**
```
[1, 2, 3, 9, 5]
[1, 2, 3, 4, 5]
```


### 5. Can you C me now?

**المفهوم:** هذه المهمة تتعلق بمعالجة **السلاسل النصية (Strings)** في بايثون وكيفية إزالة أحرف معينة منها. السلاسل النصية في بايثون غير قابلة للتغيير (immutable)، مما يعني أنه لا يمكن تعديلها مباشرة. بدلاً من ذلك، يجب إنشاء سلسلة نصية جديدة تحتوي على التغييرات المطلوبة.

**الشرح:** الدالة `no_c` تأخذ سلسلة نصية `my_string` وتقوم بإزالة جميع الأحرف `c` و `C` منها. يتم تحقيق ذلك عن طريق التكرار على كل حرف في السلسلة الأصلية. إذا لم يكن الحرف `c` أو `C`، يتم إضافته إلى سلسلة نصية جديدة فارغة (`new_string`). في النهاية، تعاد السلسلة النصية الجديدة.

**الكود:**
```python
#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for char in my_string:
        if char != 'c' and char != 'C':
            new_string += char
    return new_string
```

**مثال على الاستخدام:**
```python
print(no_c("Best School"))
print(no_c("Chicago"))
print(no_c("C is fun!"))
```
**الناتج المتوقع:**
```
Best Shool
hiago
 is fun!
```


### 6. Lists of lists = Matrix

**المفهوم:** هذه المهمة تقدم مفهوم **المصفوفات (Matrices)** في بايثون، والتي يتم تمثيلها عادةً كـ **قوائم متداخلة (Nested Lists)**. كل قائمة داخلية تمثل صفًا في المصفوفة.

**الشرح:** الدالة `print_matrix_integer` تأخذ مصفوفة (قائمة من القوائم) من الأعداد الصحيحة وتطبعها. يتم التكرار على كل صف في المصفوفة، ثم يتم التكرار على كل عنصر في الصف. يتم طباعة العناصر مفصولة بمسافة، وكل صف في سطر جديد. يتم استخدام `str.format()` لطباعة الأعداد الصحيحة.

**الكود:**
```python
#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i in range(len(row)):
            if i != len(row) - 1:
                print("{:d}".format(row[i]), end=" ")
            else:
                print("{:d}".format(row[i]), end="")
        print()
```

**مثال على الاستخدام:**
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print_matrix_integer(matrix)
print("--")
print_matrix_integer()
```
**الناتج المتوقع:**
```
1 2 3
4 5 6
7 8 9
--

```

"""
### 7. Tuples addition

**المفهوم:** هذه المهمة تقدم مفهوم **الصفوف (Tuples)** في بايثون وكيفية التعامل معها. الصفوف تشبه القوائم ولكنها **غير قابلة للتغيير (immutable)**، مما يعني أنه لا يمكن تعديل عناصرها بعد إنشائها. كما أنها تستخدم للأشياء التي لا تتغير، مثل الإحداثيات أو سجلات البيانات.

**الشرح:** الدالة `add_tuple` تأخذ صفين `tuple_a` و `tuple_b` وتقوم بجمع أول عنصرين من كل صف. إذا كان الصف أصغر من عنصرين، يتم استخدام القيمة 0 للعناصر المفقودة. إذا كان الصف أكبر من عنصرين، يتم استخدام أول عنصرين فقط. تعيد الدالة صفًا جديدًا يحتوي على نتائج الجمع.

**الكود:**
```python
#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a1 = tuple_a[0] if len(tuple_a) >= 1 else 0
    a2 = tuple_a[1] if len(tuple_a) >= 2 else 0
    b1 = tuple_b[0] if len(tuple_b) >= 1 else 0
    b2 = tuple_b[1] if len(tuple_b) >= 2 else 0
    return (a1 + b1, a2 + b2)
```

**مثال على الاستخدام:**
```python
tuple_a = (1, 89)
tuple_b = (88, 11)
new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)

print(add_tuple(tuple_a, (1, )))
print(add_tuple(tuple_a, ()))
```
**الناتج المتوقع:**
```
(89, 100)
(2, 89)
(1, 89)
```


### 8. More returns!

**المفهوم:** هذه المهمة توضح كيفية إرجاع **صفوف متعددة القيم (Multiple Return Values)** من دالة في بايثون. عند إرجاع عدة قيم من دالة، يتم تجميعها تلقائيًا في صف.

**الشرح:** الدالة `multiple_returns` تأخذ سلسلة نصية `sentence`. يجب أن تعيد الدالة صفًا يحتوي على طول السلسلة النصية وحرفها الأول. إذا كانت السلسلة النصية فارغة، يجب أن يكون الحرف الأول `None`. يتم التحقق من طول السلسلة النصية باستخدام `len()`، ويتم الوصول إلى الحرف الأول باستخدام الفهرسة `sentence[0]`.

**الكود:**
```python
#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        return (0, None)
    return (len(sentence), sentence[0])
```

**مثال على الاستخدام:**
```python
sentence = "At school, I learnt C!"
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first))
```
**الناتج المتوقع:**
```
Length: 22 - First character: A
```


### 9. Find the max

**المفهوم:** هذه المهمة تتناول كيفية إيجاد **أكبر عنصر في قائمة (Finding the Maximum Element in a List)** دون استخدام الدالة المدمجة `max()`. هذا يعزز فهم التكرار الشرطي والمقارنات.

**الشرح:** الدالة `max_integer` تأخذ قائمة `my_list` من الأعداد الصحيحة. إذا كانت القائمة فارغة، تعيد الدالة `None`. وإلا، فإنها تبدأ بافتراض أن أول عنصر هو الأكبر (`max_val`). ثم تتكرر على بقية العناصر، وإذا وجدت عنصرًا أكبر، تقوم بتحديث `max_val`. في النهاية، تعيد الدالة `max_val`.

**الكود:**
```python
#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    max_val = my_list[0]
    for i in my_list:
        if i > max_val:
            max_val = i
    return max_val
```

**مثال على الاستخدام:**
```python
my_list = [1, 90, 2, 13, 34, 5, -13, 3]
max_value = max_integer(my_list)
print("Max: {}".format(max_value))
```
**الناتج المتوقع:**
```
Max: 90
```


### 10. Only by 2

**المفهوم:** هذه المهمة توضح كيفية **إنشاء قائمة جديدة بناءً على شرط (List Comprehension)**. تُستخدم List Comprehension لإنشاء قوائم جديدة بطريقة موجزة وفعالة.

**الشرح:** الدالة `divisible_by_2` تأخذ قائمة `my_list` من الأعداد الصحيحة. تعيد الدالة قائمة جديدة بنفس حجم القائمة الأصلية، حيث يحتوي كل عنصر على `True` إذا كان العدد المقابل في القائمة الأصلية قابلاً للقسمة على 2، و `False` إذا لم يكن كذلك. يتم تحقيق ذلك بكفاءة باستخدام List Comprehension.

**الكود:**
```python
#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    return [i % 2 == 0 for i in my_list]
```

**مثال على الاستخدام:**
```python
my_list = [0, 1, 2, 3, 4, 5, 6]
list_result = divisible_by_2(my_list)

i = 0
while i < len(list_result):
    print("{:d} {:s} divisible by 2".format(my_list[i], "is" if list_result[i] else "is not"))
    i += 1
```
**الناتج المتوقع:**
```
0 is divisible by 2
1 is not divisible by 2
2 is divisible by 2
3 is not divisible by 2
4 is divisible by 2
5 is not divisible by 2
6 is divisible by 2
```

"""
### 11. Delete at

**المفهوم:** هذه المهمة توضح كيفية **حذف عنصر من قائمة (Deleting an Element from a List)** في بايثون باستخدام الكلمة المفتاحية `del`. تُستخدم `del` لحذف عناصر من القوائم بناءً على الفهرس.

**الشرح:** الدالة `delete_at` تأخذ قائمة `my_list` وفهرس `idx`. إذا كان الفهرس سالبًا أو خارج النطاق، فإن الدالة لا تُجري أي تغييرات على القائمة الأصلية وتُعيدها كما هي. وإذا كان الفهرس صالحًا، تقوم الدالة بحذف العنصر الموجود في هذا الفهرس باستخدام `del my_list[idx]` ثم تُعيد القائمة المعدلة.

**الكود:**
```python
#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list
    del my_list[idx]
    return my_list
```

**مثال على الاستخدام:**
```python
my_list = [1, 2, 3, 4, 5]
idx = 3
new_list = delete_at(my_list, idx)
print(new_list)
print(my_list)
```
**الناتج المتوقع:**
```
[1, 2, 3, 5]
[1, 2, 3, 5]
```


### 12. Switch

**المفهوم:** هذه المهمة توضح طريقة بسيطة وفعالة لـ **تبديل قيم متغيرين (Swapping Variable Values)** في بايثون دون الحاجة إلى متغير مؤقت. هذه الميزة هي جزء من **تعبئة الصفوف (Tuple Packing)** و **تفريغ الصفوف (Tuple Unpacking)**.

**الشرح:** تتطلب هذه المهمة إكمال جزء من الكود لتبديل قيم المتغيرين `a` و `b`. في بايثون، يمكن تحقيق ذلك بسهولة باستخدام تعيين متعدد (multiple assignment) أو تفريغ الصفوف. يتم تعيين قيمة `b` إلى `a` وقيمة `a` إلى `b` في سطر واحد، مما يؤدي إلى تبديل قيمهما بفعالية.

**الكود:**
```python
#!/usr/bin/python3
a = 10
b = 89
a, b = b, a
print("a={:d} - b={:d}".format(a, b))
```

**مثال على الاستخدام:**
```python
# الكود أعلاه هو مثال الاستخدام نفسه
```
**الناتج المتوقع:**
```
a=89 - b=10
```

