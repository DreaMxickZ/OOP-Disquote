import uvicorn
if __name__ == "__main__":
    # uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True, ssl_keyfile=None, ssl_certfile=None)
    # uvicorn.run("main:app", host="localhost", port=8080,reload=True, ssl_keyfile=None, ssl_certfile=None)
    uvicorn.run("main:app", host="localhost", port=8080,
                reload=True, reload_dirs="./", workers=4,
                ssl_keyfile=None, ssl_certfile=None)
