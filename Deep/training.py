import tensorflow as tf


def train_step(x, y, model, loss_object, optimizer):
    with tf.GradientTape() as tape:
        y_pred = model(x)
        loss = loss_object(y, y_pred)
    gradients = tape.gradient(loss, model.trainable_variables)
    optimizer.apply_gradients(zip(gradients, model.trainable_variables))

    return loss


def test_step(x, y, model, loss_object):
    y_pred = model(x)
    t_loss = loss_object(y, y_pred)

    return t_loss
