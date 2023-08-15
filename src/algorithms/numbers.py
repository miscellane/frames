"""
numbers.py
"""
import secrets
import numpy as np
import pandas as pd


class Numbers:

    def __init__(self) -> None:
        """
        Constructor
        """

        self.__size = (16, 1)
        constant = 256
        self.__variable = secrets.randbits(k=constant)
        self.__constant = constant

    def series_reproducible(self) -> np.ndarray:
        """
        A reproducible series
        """

        generator = np.random.default_rng(seed=self.__constant)

        return generator.random(size=self.__size)
    
    def series_variable(self) -> pd.DataFrame:
        """
        A more or less irreproducible series
        """

        generator = np.random.default_rng(seed=self.__variable)

        return pd.DataFrame(data={'number': generator.random(size=self.__size).squeeze()})
