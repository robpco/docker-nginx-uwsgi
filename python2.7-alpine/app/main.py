def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return ["Hello World from a default uWSGI Python 2.7 app in an\
            Alpine-Linux Docker container with Nginx (default)"]
