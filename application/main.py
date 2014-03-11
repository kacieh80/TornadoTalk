import tornado.ioloop
import tornado.web
from tornado.httpclient import AsyncHTTPClient
from tornado import gen
import json
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
api_key = "YOUR KEY HERE"
states = {
            "NSW": "New South Whales", 
            "QLD": "Queensland", 
            "ACT": "Australian Capital Territory", 
            "VIC": "Victoria", 
            "TAS": "Tasmania", 
            "SA": "South Australia"
        }
api_url = "https://www.googleapis.com/mapsengine/v1/tables/12421761926155747447-06672618218968397709/features?version=published&key={0}&where=State='{1}'"


class MainHandler(tornado.web.RequestHandler):
    @gen.coroutine
    def get(self):
        url = "https://www.googleapis.com/mapsengine/v1/tables/12421761926155747447-06672618218968397709/features?version=published&key={0}".format(api_key)
        response = yield gen.Task(
            AsyncHTTPClient().fetch,url)

        clean_response = scrub_it(response)

        self.render("templates/main.html", 
                    all_locations=clean_response)


class StatesHandler(tornado.web.RequestHandler):
    @gen.coroutine
    def get(self):
        async_client = AsyncHTTPClient()

        output = []
        for k,v in states.items():
            logger.info("Getting {0}".format(k))
            task = gen.Task(self.get_state_data, k, async_client)
            output.append(task)

        results = yield output
        results = dict(results)

        self.render("templates/states.html", **results)  

    @gen.coroutine
    def get_state_data(self, state, client):
        url = api_url.format(api_key, state)
        output = yield gen.Task(client.fetch, url)
        logger.info("Got {0}".format(state))
        return (state.lower(), scrub_it(output))


class StateHandler(tornado.web.RequestHandler):
    @gen.coroutine
    def get(self, abbv):
        st = abbv.upper()
        url = "https://www.googleapis.com/mapsengine/v1/tables/12421761926155747447-06672618218968397709/features?version=published&key={0}&where=State='{1}'".format(api_key, st)
        response = yield gen.Task(
            AsyncHTTPClient().fetch,url)

        clean_response = scrub_it(response)

        self.render("templates/single_state.html", 
                    locations=clean_response,
                    name=states[st])


def scrub_it(response):
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

application = tornado.web.Application(routes, debug=True)
if __name__ == "__main__":
    application.listen(8000)
    tornado.ioloop.IOLoop.instance().start()
