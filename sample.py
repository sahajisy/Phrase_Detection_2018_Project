import falcon
#import subprocess as sb
class QuoteResource:
    def on_get(self,req,resp):
        quote={'quote':("tve always been more intersted in"),'author':'abc abc abc'}
        resp.media=quote

api=falcon.API()
api.add_route('/quote',QuoteResource())
