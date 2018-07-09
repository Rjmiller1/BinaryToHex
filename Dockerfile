# Set the base image

FROM python:2.7

# Dockerfile author / maintainer

MAINTAINER Name rsmiller1@mix.wvu.edu

ADD BinaryToHexConverter.py bitConversion.py dataFormat.py /

CMD [ "python", "./BinaryToHexConverter.py" ]