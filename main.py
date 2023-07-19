from website import create_app

app = create_app()

# Only if we run this file and not if we import, then we will execute the line below
if __name__ == '__main__':
    # debug = True will indicate that everytime the code is changed, the webserver will be refreshed
    app.run(debug = True)