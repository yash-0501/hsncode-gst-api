HSN Code - GST API

This API helps in getting the GST Rates by using the HSN Number.

- INSTRUCTIONS
-> After downloading/pulling this repository, create a virtual environment or activate your virtual env
-> In the terminal run command 'pip install -r requirements.txt'
-> After the command is successfull, run py manage.py runserver
-> The server is started at http://127.0.0.1:8000/
-> Once the server is started go to url: http://127.0.0.1:8000/api/<Enter Your HSN Code Here>/ , this will return 
an array of objects with commodities and gst associated with your enetered HSN Code **Enter HSN Code without <>**

Example: url = http://127.0.0.1:8000/api/9405.00.00/
        response = [
    {
        "HSN": "9405.00.00",
        "GST": 0.28,
        "Name of Commodity": "Lamps and lighting fittings including searchlights and spotlights and parts thereof, not elsewhere specified or included; illuminated signs, illuminated name-plates and the like, having a permanently fixed light source, and parts thereof not elsewhere specified or included"
    },
    {
        "HSN": "9405.00.00",
        "GST": 0.12,
        "Name of Commodity": "Hurricane lanterns, kerosene lamps/lantern, petromax, glass chimney,accessories and components thereof"
    },
    {
        "HSN": "9405.00.00",
        "GST": 0.12,
        "Name of Commodity": "LED lights or fixtures including LED lamps"
    },
    {
        "HSN": "9405.00.00",
        "GST": 0.12,
        "Name of Commodity": "LED (light emitting diode) driver and MCPCB (Metal Core Printed Circuit Board)"
    }
]

