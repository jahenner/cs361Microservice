# cs361Microservice

Communication contract
To request data from the server, you must establish a tcp socket connection to the server. An example is given in client.py file. You need to send the following information as JSON: principal, rate_of_interest, number (how many times to compound within a year), time.
example: {'principal': 15000, 'rate_of_interest': 0.03, 'number': 12, 'time': 30}

The server will then return data as JSON in the following format.
{ 'end_calculation': 36852.63,
    'error': { 'ok': True, 'msg': 'OK' }
}
end_calculation will return a float rounded to nearest 100ths place.
error will contain a dictionary with keys 'ok' and 'msg'
ok will be a boolean value indicating if anything went wrong during the calculation
msg will be a string with a short message on what went wrong.

UML Diagram
![image](https://user-images.githubusercontent.com/76822904/180844917-311dd781-4367-4262-8e46-f7596469b168.png)
