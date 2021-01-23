import falcon
import subprocess as sb
class QuoteResource:
	def on_get(self,req,resp):
		data=str(req.stream.read())
		p=sb.Popen(['python'],['script.py'],stdout=sb.PIPE)
		ans=p.communicate()
		resp.media=ans
api=falcon.API()
api.add_route('/quote',QuoteResource())
