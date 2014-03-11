import tornado.ioloop
import tornado.web
from tornado.httpclient import AsyncHTTPClient
from tornado import gen
import json
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
api_key = "YOU API KEY HERE"

class MainHandler(tornado.web.RequestHandler):
    @gen.coroutine
    def get(self):
        url = "https://www.googleapis.com/mapsengine/v1/tables/12421761926155747447-06672618218968397709/features?version=published&key={0}".format(api_key)
        response = yield gen.Task(
            AsyncHTTPClient().fetch,url)

        clean_response = CleanResponse().scrub_it(response)

        self.render("templates/main.html", 
                    all_locations=clean_response)


class StatesHandler(tornado.web.RequestHandler):
    @gen.coroutine
    def get(self):
        clean_obj = CleanResponse()
        async_client = AsyncHTTPClient()
        nsw_url = "https://www.googleapis.com/mapsengine/v1/tables/12421761926155747447-06672618218968397709/features?version=published&key={0}&where=State='NSW'".format(api_key)
        logger.info("Getting NSW")
        raw_nsw = yield gen.Task(
            async_client.fetch,nsw_url)
        
        nsw = clean_obj.scrub_it(raw_nsw)

        qld_url = "https://www.googleapis.com/mapsengine/v1/tables/12421761926155747447-06672618218968397709/features?version=published&key={0}&where=State='QLD'".format(api_key)
        logger.info("Getting QLD")
        raw_qld = yield gen.Task(
            async_client.fetch,qld_url)

        qld = clean_obj.scrub_it(raw_qld)
        
        act_url = "https://www.googleapis.com/mapsengine/v1/tables/12421761926155747447-06672618218968397709/features?version=published&key={0}&where=State='ACT'".format(api_key)
        logger.info("Getting ACT")
        raw_act = yield gen.Task(
            async_client.fetch,act_url)

        act = clean_obj.scrub_it(raw_act)

        vic_url = "https://www.googleapis.com/mapsengine/v1/tables/12421761926155747447-06672618218968397709/features?version=published&key={0}&where=State='VIC'".format(api_key)
        logger.info("Getting VIC")
        raw_vic = yield gen.Task(
            async_client.fetch,vic_url)

        vic = clean_obj.scrub_it(raw_vic)
        
        tas_url = "https://www.googleapis.com/mapsengine/v1/tables/12421761926155747447-06672618218968397709/features?version=published&key={0}&where=State='TAS'".format(api_key)
        logger.info("Getting TAS")
        raw_tas = yield gen.Task(
            async_client.fetch,tas_url)

        tas = clean_obj.scrub_it(raw_tas)

        sa_url = "https://www.googleapis.com/mapsengine/v1/tables/12421761926155747447-06672618218968397709/features?version=published&key={0}&where=State='SA'".format(api_key)
        logger.info("Getting SA")
        raw_sa = yield gen.Task(
            async_client.fetch,sa_url) 

        sa = clean_obj.scrub_it(raw_sa) 

        self.render("templates/states.html", 
                    nsw=nsw,
                    qld=qld,
                    act=act,
                    vic=vic,
                    tas=tas,
                    sa=sa)  


class StateHandler(tornado.web.RequestHandler):
    @gen.coroutine
    def get(self, abbv):
        states = {
            "NSW": "New South Whales", 
            "QLD": "Queensland", 
            "ACT": "Australian Capital Territory", 
            "VIC": "Victoria", 
            "TAS": "Tasmania", 
            "SA": "South Australia"
        }
        st = abbv.upper()
        url = "https://www.googleapis.com/mapsengine/v1/tables/12421761926155747447-06672618218968397709/features?version=published&key={0}&where=State='{1}'".format(api_key, st)
        response = yield gen.Task(
            AsyncHTTPClient().fetch,url)

        clean_response = CleanResponse().scrub_it(response)

        self.render("templates/single_state.html", 
                    locations=clean_response,
                    name=states[st])


class CleanResponse(object):

    def scrub_it(self, response):
        clean = json.loads(response.body.decode("utf-8"))
        if "features" in clean:
        	return clean["features"]
        else:
        	return [clean["error"]]


routes = [
    (r"/", MainHandler),
    (r"/states", StatesHandler),
    (r"/state/(.*)", StateHandler)
]

application = tornado.web.Application(routes)
if __name__ == "__main__":
    application.listen(8000)
    tornado.ioloop.IOLoop.instance().start()
