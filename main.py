import tornado.ioloop
import tornado.web
from tornado.httpclient import AsyncHTTPClient, HTTPRequest
from tornado import gen
from rauth import OAuth1Service
import json

class MainHandler(tornado.web.RequestHandler):
    @gen.coroutine
    def get(self):
        url = "https://www.googleapis.com/mapsengine/v1/tables/12421761926155747447-06672618218968397709/features?version=published&key=<INSERT KEY HERE>"
        response = yield gen.Task(
            AsyncHTTPClient().fetch,url)

        clean_response = CleanResponse().scrub_it(response)

        self.render("templates/main.html", 
                    all_locations=clean_response)  

class StateHandler(tornado.web.RequestHandler):
    @gen.coroutine
    def get(self):
        clean_obj = CleanResponse()
        nsw_url = "https://www.googleapis.com/mapsengine/v1/tables/12421761926155747447-06672618218968397709/features?version=published&key=AIzaSyCoV5gw7diiTdKznvnWTMMIjGYoIRFXPAA&where=State='NSW'"
        raw_nsw = yield gen.Task(
            AsyncHTTPClient().fetch,nsw_url)
        
        nsw = clean_obj.scrub_it(raw_nsw)

        qld_url = "https://www.googleapis.com/mapsengine/v1/tables/12421761926155747447-06672618218968397709/features?version=published&key=AIzaSyCoV5gw7diiTdKznvnWTMMIjGYoIRFXPAA&where=State='QLD'"
        raw_qld = yield gen.Task(
            AsyncHTTPClient().fetch,qld_url)

        qld = clean_obj.scrub_it(raw_qld)
        act_url = "https://www.googleapis.com/mapsengine/v1/tables/12421761926155747447-06672618218968397709/features?version=published&key=AIzaSyCoV5gw7diiTdKznvnWTMMIjGYoIRFXPAA&where=State='ACT'"
        raw_act = yield gen.Task(
            AsyncHTTPClient().fetch,act_url)

        act = clean_obj.scrub_it(raw_act)

        vic_url = "https://www.googleapis.com/mapsengine/v1/tables/12421761926155747447-06672618218968397709/features?version=published&key=AIzaSyCoV5gw7diiTdKznvnWTMMIjGYoIRFXPAA&where=State='VIC'"
        raw_vic = yield gen.Task(
            AsyncHTTPClient().fetch,vic_url)

        vic = clean_obj.scrub_it(raw_vic)
        tas_url = "https://www.googleapis.com/mapsengine/v1/tables/12421761926155747447-06672618218968397709/features?version=published&key=AIzaSyCoV5gw7diiTdKznvnWTMMIjGYoIRFXPAA&where=State='TAS'"
        raw_tas = yield gen.Task(
            AsyncHTTPClient().fetch,tas_url)

        tas = clean_obj.scrub_it(raw_tas)

        sa_url = "https://www.googleapis.com/mapsengine/v1/tables/12421761926155747447-06672618218968397709/features?version=published&key=AIzaSyCoV5gw7diiTdKznvnWTMMIjGYoIRFXPAA&where=State='SA'"
        raw_sa = yield gen.Task(
            AsyncHTTPClient().fetch,sa_url) 

        sa = clean_obj.scrub_it(raw_sa) 

        self.render("templates/states.html", 
                    nsw=nsw,
                    qld=qld,
                    act=act,
                    vic=vic,
                    tas=tas,
                    sa=sa)   


class CleanResponse(object):

    def scrub_it(self, response):
        clean = json.loads(response.body.decode("utf-8"))
        if "features" in clean:
        	return clean["features"]
        else:
        	return [clean["error"]]


routes = [
    (r"/", MainHandler),
    (r"/states", StateHandler),
]


application = tornado.web.Application(routes)
if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
