FROM python:3.6.7

RUN mkdir -p /usr/src/scrapy_bole

COPY .  /usr/src/scrapy_bole/

WORKDIR /usr/src/scrapy_bole/

#防止requests超时，含数据库需要
RUN pip --default-timeout=100 install -U requests
#防止requests超时
#放最后
ADD requirements.txt /usr/src/scrapy_bole/
RUN pip install -r requirements.txt


CMD [ "sh", "./run_scrapy.sh"]
