from faker import Faker
import random
import pymysql
fake = Faker(locale='zh_CN')
gen_num = 100 # 生成一百条数据
conn = pymysql.connect(host="localhost", port=3306, user="root", password="root", db="contact",
                       charset="utf8")
cursor = conn.cursor()
for i in range(gen_num):
    name = fake.name()
    sex = random.choice(['男','女'])
    tel = fake.phone_number()
    birth = fake.date(pattern='%Y-%m-%d',end_datetime=None)
    address = fake.address()
    specialize_id = random.randint(1, 10)
    sql = """insert into app_contact 
    values(null,'%s','%s','%s','%s','%s','%d')""" % (name,sex,tel,birth,address,specialize_id)
    print(sql)
    cursor.execute(sql)
conn.commit()
cursor.close()
conn.close()