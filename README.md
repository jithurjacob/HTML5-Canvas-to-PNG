# HTML5 Canvas to PNG 
JS and Python scripts for converting HTML5 Canvas to PNG

You need to add the JS scripts in frontend to obtain the base64 data from the Canvas element. This base64 data then needs to be sent to server via AJAX or if needed, you can directly add it as an img tag. In backend we need to strip the "data:image/png;base64," from the data. Then using "binascii" library we can convert the base64 data to PNG.
