import h5py
import numpy as np

def load_dataset():
    train_data = h5py.File(r'data\train_catvnoncat.h5', 'r')
    train_set_x_orig = np.array(train_data['train_set_x'][:]) # признаки
    train_set_y_orig = np.array(train_data['train_set_y'][:]) # метки классов

    test_data = h5py.File(r'data\test_catvnoncat.h5', 'r')
    test_set_x_orig = np.array(test_data['test_set_x'][:]) # признаки
    test_set_y_orig = np.array(test_data['test_set_y'][:]) # метки классов

    classes = np.array(test_data['list_classes'][:]) # the list of classes
    classes = np.array(list(map(lambda x: x.decode('utf-8'), classes)))

    train_set_y = train_set_y_orig.reshape(train_set_y_orig.shape[0])
    test_set_y = test_set_y_orig.reshape(test_set_y_orig.shape[0])
    return train_set_x_orig, train_set_y, test_set_x_orig, test_set_y, classes

def main():
    train_set_x_orig, train_set_y, test_set_x_orig, test_set_y, classes = load_dataset()

if __name__ == '__main__':
    main()
