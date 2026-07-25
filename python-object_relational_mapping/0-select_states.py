#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa
"""
import sys
import MySQLdb

if __name__ == "__main__":
    # الحصول على معلومات الاتصال من مدخلات سطر الأوامر (Arguments)
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    # الاتصال بقاعدة البيانات MySQL
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_user,
        passwd=mysql_password,
        db=db_name
    )

    # إنشاء مؤشر (Cursor) لتنفيذ أوامر SQL
    cursor = db.cursor()

    # تنفيذ الاستعلام لجلب كل الولايات وترتيبها تصاعدياً حسب الـ id
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # جلب جميع النتائج
    rows = cursor.fetchall()

    # طباعة النتائج بالشكل المطلوب
    for row in rows:
        print(row)

    # إغلاق المؤشر والاتصال بقاعدة البيانات
    cursor.close()
    db.close()
