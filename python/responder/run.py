from pathlib import Path
import responder

def parentdir(path='.', layer=0):
    return Path(path).resolve().parents[layer]

BASE_DIR = parentdir(__file__, 0)

# static_dir => dist
api = responder.API(static_dir=str(BASE_DIR.joinpath('dist')), static_route='/')

api.add_route("/", static=True)

@api.route("/api/accounts")
def customer(req, resp):
    result = {
            "id": "1",
            "name": "tanino",
            "email": "tanino@example.jp",
            }
    resp.media = {
            "status": 200,
            "result": [result],
            }

if __name__ == '__main__':
    api.run(address='0.0.0.0')
