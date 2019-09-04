class ART:
    Y = []

    def __init__(self, I, alpha = 0.001, rho = 0.5, beta = 1):
        self.I     = I
        self.alpha = alpha
        self.rho   = rho
        self.beta  = beta