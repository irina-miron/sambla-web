def log_transform(x):
        x = np.abs(x)
        return np.log(x + 1)
