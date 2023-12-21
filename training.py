import pandas as pd
import matplotlib.pyplot as plt
from tqdm import tqdm


def normalize_data(data):
    """normalize the data"""
    return (data - data.mean()) / data.std()


def denormalize_elem(m, b, data):
    """de-normalize datas"""
    b = -m * data.km.mean() * data.price.std() / data.km.std() +\
        b * data.price.std() + data.price.mean()
    m = (m * data.price.std()) / data.km.std()
    return m, b


def gradient_descent(m_now, b_now, points, L):
    """compute gradient descent from datas of xi for km and price"""
    m_gradient = 0
    b_gradient = 0
    n = len(points)
    for i in range(n):
        x = points.iloc[i].km
        y = points.iloc[i].price
        m_gradient += -(1/n) * x * (y - (m_now * x + b_now))
        b_gradient += -(1/n) * (y - (m_now * x + b_now))

    m = m_now - m_gradient * L
    b = b_now - b_gradient * L
    return m, b


def loss_function(m, b, points):
    """compute absolute error"""
    total_error = 0
    m, b = denormalize_elem(m, b, points)
    for i in range(len(points)):
        x = points.iloc[i].km
        y = points.iloc[i].price
        total_error += (y - (m * x + b)) ** 2

    return total_error / float(len(points))


def main():
    """main function"""
    try:
        data = pd.read_csv('data.csv')
        data_n = normalize_data(data)
        errors = []
        m = 0
        b = 0
        L = 0.001
        epochs = 10000
        for i in tqdm(range(epochs)):
            m, b = gradient_descent(m, b, data_n, L)
            err = loss_function(m, b, data)
            errors.append(err)

        # de-normalize
        m, b = denormalize_elem(m, b, data)

        print(f"m={m}, b={b}")
        # saving thetas
        f = open("thetas.txt", "w+")
        f.write(f"{m},{b}")
        f.close

        # show graph with datas and linear regression
        plt.scatter(data.km, data.price)
        plt.plot(list(range(0, 250000)),
                 [m * x + b for x in range(0, 250000)], color='red')
        plt.xlabel('mileage')
        plt.ylabel('price')
        plt.show()

        # graph for errors
        plt.plot(list(range(0, 10000)), errors)
        plt.xlabel('nb of iterations')
        plt.ylabel('cost')
        plt.show()
    except AssertionError as error:
        print(f"{AssertionError.__name__}: {error}")
    except FileNotFoundError as error:
        print(f"{FileNotFoundError.__name__}: {error}")
    except Exception as error:
        print(f"An unexpected error occurred: {error}")
    return


if __name__ == "__main__":
    main()
