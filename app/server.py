def run():
    """
    Run the server
    """
    from app import app, resources
    app.run(debug=True, host='0.0.0.0')
