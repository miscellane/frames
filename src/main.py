import logging
import os
import sys

def main():

    logger.info('frames')

    numbers = src.algorithms.numbers.Numbers()
    logger.info(numbers.series_reproducible())
    logger.info(numbers.series_variable())


if __name__ == '__main__':
    root = os.getcwd()
    sys.path.append(root)
    sys.path.append(os.path.join(root, 'src'))

    # Logging
    logging.basicConfig(level=logging.INFO,
                        format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                        datefmt='%Y-%m-%d %H:%M:%S')
    logger = logging.getLogger(__name__)

    # Libraries
    import src.algorithms.numbers

    main()
