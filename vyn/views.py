from flask import Flask, json, render_template
from scapy.layers.inet import traceroute

app = Flask(__name__)
app.config.from_object("config")


@app.route('/')
def index():
    return "Hello world !"




    # Run trace route.
    result, _ = traceroute([domain], dport=[80,443], maxttl=20, retry=-2)

    # Convert to a dot graph.
    dot = result.graph(string=True)

    # Project simple details of the routes taken.
    routes = [(tcp.dst, ip.sprintf("%dst%:%sport%")) for tcp, ip in result]

    # Cache and return the result.
    result = json.dumps({
        "graph": dot,
        "routes": routes
    })

    cached_trace_routes[domain] = result
    return result

if __name__ == "__main__":
    app.run()