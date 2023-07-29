import secrets
import numpy as np


class Numbers:

    def __init__(self) -> None:
        
        constant = 256
        self.__variable = secrets.randbits(k=constant)
        self.__constant = constant

    def __series_reproducible(self):

        generator = np.random.default_rng(seed=self.__constant)

        return generator.random(size=(16, 1))

    def exc(self) -> np.ndarray:

        return self.__series_reproducible()
