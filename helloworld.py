import tensorflow as tf


# hello = tf.constant("hello tf!")
# sess = tf.Session()
# print(sess.run(hello))

# 定义一个常量
data1 = tf.constant(2,dtype=tf.int32)
# 定义一个变量
data2 = tf.Variable(10,name="var")
print(data1)
print(data2)
sess = tf.Session()
print(sess.run(data1))
# 变量的初始化
init = tf.global_variables_initializer()
sess.run(init)
print(sess.run(data2))
sess.close()#关闭方式一
# 关闭方式二：
# with sess:
#     sess.run(data2)

# TensorFlow的实质：张量tensor+计算图grahps
# tensor数据（常量、变量）
# op操作，算数运算，赋值
# grahps数据操作的过程
# session：所有的计算图都要放在session中执行，运算的交互环境

# 四则运算
# 常量
data1 = tf.constant(6)
data2 = tf.constant(2)
dataAdd = tf.add(data1,data2)
dataMul = tf.multiply(data1,data2)
dataSub = tf.subtract(data1,data2)
dataDiv = tf.divide(data1,data2)
with tf.Session() as sess:
    print(sess.run(dataAdd))
    print(sess.run(dataMul))
    print(sess.run(dataSub))
    print(sess.run(dataDiv))
print("end")


# 变量
data1 = tf.Variable(6)
data2 = tf.Variable(2)
dataAdd = tf.add(data1,data2)
dataCopy = tf.assign(data2,dataAdd)
dataMul = tf.multiply(data1,data2)
dataSub = tf.subtract(data1,data2)
dataDiv = tf.divide(data1,data2)
# 先定义变量，再调用global_variables_initializer，完成初始化
init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    print(sess.run(dataAdd))
    print(sess.run(dataMul))
    print(sess.run(dataSub))
    print(sess.run(dataDiv))
    print("sess.run(dataCopy)",sess.run(dataCopy))
    print("dataCopy.eval()",dataCopy.eval())
    print("tf.get_default_session()",tf.get_default_session().run(dataCopy))