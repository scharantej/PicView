## Flask Application Design

### HTML Files

- **index.html**: This file will serve as the main page of the application and display the images and their captions. It should include the necessary HTML elements to display the images and their corresponding captions.

### Routes

- **index**: This route will be associated with the `index.html` file and will serve as the entry point for the application. It will render the `index.html` file, displaying the images and their captions.

```python
@app.route("/")
def index():
    return render_template("index.html")
```