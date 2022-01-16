from jrdb.jrdb import download

# Download data from JRDB web site (ex. SED)
loader = Download.JrdbDownloader()
text_data = loader.load('KYI211226.zip')

# parse
parser = parse.JrdbDataParser()
df = parser.parse(text_data, 'KYI')   # return pandas DataFrame
