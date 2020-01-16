import tensorflow as tf
import numpy as np

w = tf.Variable([1], dtype=tf.float32)
b = tf.Variable([1], dtype=tf.float32)

x = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)

line_model = w * x + b
with tf.name_scope("loss_model"):
    loss = tf.reduce_sum(tf.square(line_model - y))
    tf.summary.scalar("loss", loss)
optimizer = tf.train.AdamOptimizer(0.01)
train = optimizer.minimize(loss)
x_train = np.linspace(1, 100, 99)
y_train = 6 * x_train + 5
y_train = y_train + np.random.random([len(x_train)])
sess = tf.Session()
init = tf.global_variables_initializer()
sess.run(init)

merged = tf.summary.merge_all()
writer = tf.summary.FileWriter(r'C:\work\work_space\TensorFlow\tmp\tensorflow', sess.graph)
# sess.run(train, feed_dict={x: x_train, y: y_train})
#
# print('W: %s b: %s loss: %s' % (sess.run(w), sess.run(
#     b), sess.run(loss, {x: x_train, y: y_train})))

for i in range(10000):
    # sess.run(train, {x: x_train, y: y_train})
    summary, _ = sess.run([merged, train], {x: x_train, y: y_train})
    writer.add_summary(summary, i)

# 打印一下训练后的结果
    print('W: %s b: %s loss: %s' % (sess.run(w), sess.run(
            b), sess.run(loss, {x: x_train, y: y_train})))







