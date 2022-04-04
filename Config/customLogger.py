import logging

class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename=r"C://Users//SauravSharma//Pytest//Pytest_pom_dd_sauce_demo//Logs//tes.log",
                                    format='%(asctime)s: %(levelname)s: (levelname)s: %(message)s'
                                    )

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger