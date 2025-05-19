import falcon
import json
from scoring import add_event, get_trending
from constants import TRENDING_KEY

class AddEventResource:
    def on_post(self, req, resp):
        try:
            print("Got a new Add Event Request")
            body = req.media
            item_id = body.get("item_id")
            event_time = body.get("event_time")
            weight = body.get("weight", 1.0)

            if not item_id or not event_time:
                resp.status = falcon.HTTP_400
                resp.media = {"error": "item_id and event_time are required"}
                return

            add_event(TRENDING_KEY, item_id, int(event_time), float(weight))
            resp.status = falcon.HTTP_200
            resp.media = {"message": "Event added successfully"}

        except Exception as e:
            resp.status = falcon.HTTP_500
            resp.media = {"error": str(e)}

class TrendingResource:
    def on_get(self, req, resp):
        try:
            count = int(req.get_param("count") or 10)
            items = get_trending(TRENDING_KEY, count)
            result = [{"item_id": item.decode(), "score": round(score, 6)} for item, score in items]
            resp.status = falcon.HTTP_200
            resp.media = result
        except Exception as e:
            resp.status = falcon.HTTP_500
            resp.media = {"error": str(e)}

# Falcon app setup
app = falcon.App()
app.add_route('/add_event', AddEventResource())
app.add_route('/trending', TrendingResource())

# For dev testing only
if __name__ == "__main__":
    from wsgiref import simple_server
    httpd = simple_server.make_server('127.0.0.1', 8000, app)
    print("Serving on http://127.0.0.1:8000")
    httpd.serve_forever()
