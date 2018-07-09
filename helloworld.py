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
