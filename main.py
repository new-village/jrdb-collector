import logging
from jrdb import download, parse
from internal import azure_blob_storage


if __name__ == "__main__":
    # Load logger config & Set Logger
    logging.basicConfig(level='INFO', format='%(asctime)s [%(levelname)s] %(message)s')
    logger = logging.getLogger()

    # Download data from JRDB web site (ex. SED)
    loader = download.JrdbDownloader()
    text_data = loader.load('KYI211226.zip')

    # parse
    parser = parse.JrdbDataParser()
    df = parser.parse(text_data, 'KYI')   # return pandas DataFrame

    # Load configuration file from Azure Blob Storage
    az = azure_blob_storage()
    az.save("KYI211226.df", df)

    # rtn = az.load("KYI211226.df")
    # print(rtn)
