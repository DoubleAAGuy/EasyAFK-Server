from flask import Flask, request, jsonify

app = Flask(__name__)

# Example function that concatenates two strings
def process_strings(str1, str2):
    return f"Processed: {str1} + {str2}"
import main

@app.route('/process', methods=['POST'])
def process():
    data = request.get_data()
    
    # Extract the two string inputs
    decoded_str = data.decode('utf-8')
    # Split the string by comma
    parts = decoded_str.split(',')
    print(parts)
    # Further split the second part by colon and slash
    name = parts[0]
    address = parts[1].split('/')[1]
    ip, port = address.split(':')
    game_version = parts[2]

    
    
    # print(str1)
    # print(str2)
    # if not str1 or not str2:
    #     return jsonify({'error': 'Both str1 and str2 are required'}), 400
    
    # # Call the function
    
    result = main.ready(name, ip,port, game_version)
    
    # return jsonify({'result': result})
    return result

if __name__ == '__main__':
    PORT = 80
    app.run(host='0.0.0.0', port=PORT, debug=True)
