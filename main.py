from website import create_app

app = create_app()

# Only if we run this file and not importing the file, then we will execute the line below
# Only run the web server if we run the file, not importing
if __name__ == '__main__':
    # debug = True will indicate that everytime the code is changed, the webserver will be refreshed
    # Turn this off during production
    app.run(debug = True)